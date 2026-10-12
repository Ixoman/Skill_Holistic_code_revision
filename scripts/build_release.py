#!/usr/bin/env python3
"""Check and package the skill using the Python standard library."""

from __future__ import annotations

import argparse
import hashlib
import json
import os
from pathlib import Path
import re
import stat
import sys
import tempfile
import zipfile


SKILL_NAME = "understand-audit-fix-codebases"
SEMVER = re.compile(
    r"(0|[1-9][0-9]*)\.(0|[1-9][0-9]*)\.(0|[1-9][0-9]*)"
    r"(?:-(?:0|[1-9][0-9]*|[0-9]*[A-Za-z-][0-9A-Za-z-]*)"
    r"(?:\.(?:0|[1-9][0-9]*|[0-9]*[A-Za-z-][0-9A-Za-z-]*))*)?"
    r"(?:\+[0-9A-Za-z-]+(?:\.[0-9A-Za-z-]+)*)?"
)
FORBIDDEN = {".git", "node_modules", "__pycache__", ".pytest_cache", "dist", "build"}


def check_package(repository: Path) -> tuple[str, dict[str, bytes], int]:
    skill_root = repository / "skills" / SKILL_NAME
    if skill_root.is_symlink() or not skill_root.is_dir():
        raise ValueError("The skill source must be a regular directory.")

    files: dict[str, bytes] = {}
    for path in sorted(skill_root.rglob("*")):
        relative = path.relative_to(skill_root)
        if any(part in FORBIDDEN or part == ".env" or part.startswith(".env.")
               for part in relative.parts):
            raise ValueError(f"Excluded source path: {relative.as_posix()}")
        mode = path.lstat().st_mode
        if stat.S_ISLNK(mode):
            raise ValueError(f"Symlink is not distributable: {relative.as_posix()}")
        if stat.S_ISDIR(mode):
            continue
        if not stat.S_ISREG(mode):
            raise ValueError(f"Non-regular source: {relative.as_posix()}")
        if path.stat().st_size > 5_000_000:
            raise ValueError(f"File exceeds 5 MB: {relative.as_posix()}")
        files[relative.as_posix()] = path.read_bytes()

    if not files or len(files) > 100 or sum(map(len, files.values())) > 25_000_000:
        raise ValueError("Package exceeds the file-count/size limits or is empty.")
    if "SKILL.md" not in files:
        raise ValueError("SKILL.md is missing.")
    text = files["SKILL.md"].decode("utf-8")
    header = re.match(r"\A---[ \t]*\r?\n(.*?)\r?\n---[ \t]*(?:\r?\n|$)", text, re.S)
    if header is None or not text[header.end():].strip():
        raise ValueError("SKILL.md needs frontmatter and a non-empty instruction body.")
    frontmatter = header.group(1)
    name = re.search(r"^name: *([a-z0-9]+(?:-[a-z0-9]+)*) *$", frontmatter, re.M)
    version_match = re.search(r"^  version: *(['\"])([^'\"]+)\1 *$", frontmatter, re.M)
    if name is None or name.group(1) != SKILL_NAME or version_match is None:
        raise ValueError("Skill name or quoted metadata.version is invalid.")
    version = version_match.group(2)
    if not SEMVER.fullmatch(version):
        raise ValueError("metadata.version must be SemVer.")
    if (repository / "VERSION").read_text(encoding="utf-8").strip() != version:
        raise ValueError("Version mismatch: VERSION and metadata.version must agree.")

    link_count = 0
    for relative, data in files.items():
        if not relative.endswith(".md"):
            continue
        for target in re.findall(r"\[[^\]]*\]\(([^)\s]+)\)", data.decode("utf-8")):
            if target.startswith(("#", "https:", "http:", "mailto:")):
                continue
            destination = ((skill_root / relative).parent / target.split("#")[0]).resolve()
            if not destination.is_relative_to(skill_root.resolve()) or not destination.is_file():
                raise ValueError(f"Missing/escaping relative file link in {relative}: {target}")
            link_count += 1
    return version, files, link_count


def build_package(repository: Path, version: str, files: dict[str, bytes]) -> Path:
    output = repository / "dist"
    if output.is_symlink():
        raise ValueError("The output directory must not be a symlink.")
    output.mkdir(exist_ok=True)
    archive = output / f"{SKILL_NAME}-{version}.zip"
    with tempfile.NamedTemporaryFile(dir=output, suffix=".zip.tmp", delete=False) as handle:
        temporary = Path(handle.name)
    try:
        with zipfile.ZipFile(temporary, "w", compression=zipfile.ZIP_DEFLATED, compresslevel=9) as bundle:
            for relative, data in sorted(files.items()):
                info = zipfile.ZipInfo(f"{SKILL_NAME}/{relative}", date_time=(1980, 1, 1, 0, 0, 0))
                info.create_system = 3
                info.compress_type = zipfile.ZIP_DEFLATED
                permissions = 0o755 if data.startswith(b"#!") or relative.endswith(".sh") else 0o644
                info.external_attr = (stat.S_IFREG | permissions) << 16
                bundle.writestr(info, data)
        with zipfile.ZipFile(temporary) as bundle:
            if bundle.testzip() is not None:
                raise ValueError("Archive integrity verification failed.")
            if set(bundle.namelist()) != {f"{SKILL_NAME}/{path}" for path in files}:
                raise ValueError("Archive manifest verification failed.")
            for relative, data in files.items():
                if bundle.read(f"{SKILL_NAME}/{relative}") != data:
                    raise ValueError(f"Archive bytes differ: {relative}")
        os.replace(temporary, archive)
    finally:
        temporary.unlink(missing_ok=True)

    digest = hashlib.sha256(archive.read_bytes()).hexdigest()
    checksum = archive.with_suffix(".zip.sha256")
    with tempfile.NamedTemporaryFile(dir=output, suffix=".sha256.tmp", mode="w",
                                     encoding="utf-8", delete=False) as handle:
        handle.write(f"{digest}  {archive.name}\n")
        checksum_temporary = Path(handle.name)
    try:
        os.replace(checksum_temporary, checksum)
    finally:
        checksum_temporary.unlink(missing_ok=True)
    return archive


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true", help="Check source/package consistency without writing output.")
    args = parser.parse_args()
    repository = Path(__file__).resolve().parents[1]
    try:
        version, files, link_count = check_package(repository)
        result = {"version": version, "files": len(files),
                  "uncompressed_bytes": sum(map(len, files.values())),
                  "relative_file_links": link_count, "check": "passed"}
        if not args.check:
            archive = build_package(repository, version, files)
            result["archive"] = str(archive.relative_to(repository))
            result["sha256"] = hashlib.sha256(archive.read_bytes()).hexdigest()
        print(json.dumps(result, indent=2))
        return 0
    except (ValueError, OSError, UnicodeError, zipfile.BadZipFile) as error:
        print(f"Package check failed: {error}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    sys.exit(main())
