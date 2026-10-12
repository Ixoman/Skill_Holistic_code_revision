# Infrastructure, containers, CI/CD, and release configuration

Trace source configuration, inputs/defaults, identities, build, produced artifact,
intended deployment, and rollback. Distinguish repository intent from live state.

- Inspect runner/token/service permissions, secrets, untrusted contributions and
  inputs, trusted sources, environment separation, and exposed storage/services.
- Check dependency/image references, integrity and appropriate pinning, lifecycle
  scripts, toolchains, shared caches, artifact publication, and release provenance.
- Review fail-open defaults, known drift, rollout/rollback compatibility, and coupled
  schema/data migrations. Do not assume a lockfile or immutable tag proves trust.
- Inspect plan/dry-run tools before executing: they can load code, contact providers,
  refresh state, invoke hooks, or write files.
- After repair, validate available syntax/schema and a safe isolated plan or affected
  build checks. State which provider/runtime behavior was not exercised.
- Deployment, changing actual cloud permissions, releasing artifacts, rotating
  secrets, and production rollback are separate operational actions requiring
  effective authority. Editing configuration does not complete those actions.
