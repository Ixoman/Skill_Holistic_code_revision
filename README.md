# Understand, Audit, and Fix Codebases

[English](README.md) | [Español](README.es.md)

**Version:** 1.0.2 · **Creator and maintainer:** Samuel Quintero

**Repository:** [Ixoman/Skill_Holistic_code_revision](https://github.com/Ixoman/Skill_Holistic_code_revision)
· [Releases](https://github.com/Ixoman/Skill_Holistic_code_revision/releases)
· [Build status](https://github.com/Ixoman/Skill_Holistic_code_revision/actions)

An Agent Skill for understanding unfamiliar codebases, reviewing correctness and
security, and repairing validated defects while preserving legitimate behavior.
It works through the coding agent's available tools and permissions.

The skill is authored in English. Responses and reports follow the user's requested
language. This repository provides documentation in English and Spanish.

## Choose the work you need

| Mode | Work | Default output |
| --- | --- | --- |
| **Understand** | Trace architecture, contracts, critical flows, validation paths, and change impact | `REPO_CONTEXT.md` |
| **Audit** | Investigate bugs and applicable security, challenge false positives, and report evidence | `AUDIT_REPORT.md` |
| **Fix** | Revalidate identified issues, repair confirmed causes, and check legitimate behavior and regressions | `REMEDIATION_REPORT.md` |

Understand and Audit preserve application source and configuration. Fix performs
scoped causal changes. An explicit request can authorize a sequence of modes.
An optional interview asks one material question at a time; clear requests proceed
without an obligatory questionnaire.

## Install

Obtain the complete `skills/understand-audit-fix-codebases/` folder, or extract its
versioned distribution ZIP. Copy that folder into one location supported by your client:

| Client and scope | Entry point after installation |
| --- | --- |
| Copilot project | `.github/skills/understand-audit-fix-codebases/SKILL.md` |
| Copilot user | `~/.copilot/skills/understand-audit-fix-codebases/SKILL.md` |
| Codex project | `.agents/skills/understand-audit-fix-codebases/SKILL.md` |
| Codex user | `~/.agents/skills/understand-audit-fix-codebases/SKILL.md` |

Keep `references/`, `assets/`, and `agents/` beside `SKILL.md`. Avoid duplicate
installation copies and accidental wrapper folders. A supporting client and approved
workspace access are required; discovery and available tools vary by host.

## Use

```text
Use Understand, Audit, and Fix Codebases in interview mode for this repository.

Use Understand, Audit, and Fix Codebases to understand this codebase before we change it.

Use Understand, Audit, and Fix Codebases to audit this component for correctness
and security. Report evidence and coverage gaps without implementing repairs.

Use Understand, Audit, and Fix Codebases to revalidate AUDIT_REPORT.md and fix
confirmed defects. Preserve legitimate behavior and existing local changes.
```

Use the client’s skill selector or supported explicit invocation. The skill does
not provide a separate command-line parser.

## Coverage and guardrails

Nine component profiles cover web, services, libraries, automation, data, installed
clients, native code, infrastructure, and AI integrations. Mixed repositories can
combine profiles; review depth depends on accessible code, contracts, tools, and scope.

Findings require current evidence, reachable conditions, a contract, attempted
refutation, and impact. Confidence, severity, evidence method, and production exposure
are recorded separately. Repairs inspect consumers and verify both rejection and
legitimate use when security is involved.

The workflow preserves existing work, examines execution effects, redacts secrets,
and respects permission boundaries. Written guardrails guide behavior; the host
enforces actual access. The skill makes no promise of bug-free software, complete
security coverage, certification, or identical performance across models.

## Repository and versioning

The installable skill lives under [`skills/understand-audit-fix-codebases/`](skills/understand-audit-fix-codebases/).
Human documentation and distribution tooling stay outside that folder.

- [Design and guardrails / Diseño y guardrails](docs/DESIGN.md)
- [Validation record / Registro de validación](docs/VALIDATION.md)
- [Versioning and releases / Versionado y releases](docs/RELEASES.md)
- [Changelog / Historial](CHANGELOG.md)

Build the versioned ZIP with Python 3.10 or later, using only the standard library:

```sh
python scripts/build_release.py --check
python scripts/build_release.py
```

Output: `dist/understand-audit-fix-codebases-1.0.2.zip` and its `.sha256` file.
`VERSION` and `metadata.version` must agree. The intended Git tag is `v1.0.2`.

The release workflow checks the package and publishes its ZIP/checksum when version
or skill sources change on `main`. It tags the exact source commit and preserves an
existing same-version package; a changed package requires a version bump. GitHub
Actions supplies a short-lived repository token. No personal token is required.
See the build status and Releases pages for actual execution/publication results.

**License:** not specified. **Support:** use this repository's issues; never include
credentials, private code, or production data in a public report.

## Primary documentation

- [GitHub Copilot: Agent Skills](https://docs.github.com/en/copilot/how-tos/copilot-on-github/customize-copilot/customize-cloud-agent/add-skills)
- [OpenAI: Build skills](https://learn.chatgpt.com/docs/build-skills)
- [Source index bundled with the skill](skills/understand-audit-fix-codebases/references/sources.md)

Product documentation was rechecked on October 12, 2026. Organizational policies
and the installed client's behavior still need validation in the intended environment.
