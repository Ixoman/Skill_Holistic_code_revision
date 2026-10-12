# Security across applicable components

In AUDIT, include relevant security even without a separate security emphasis. In
UNDERSTAND, map sensitive boundaries without claiming a completed security audit.
In FIX, validate affected controls and legitimate behavior. Do not assume a project
has a server, login, network, tenant model, database, or deployment.

## Threat context

Identify assets, human/service actors, privileges, local/remote inputs, storage,
outputs, and trust boundaries. Include imports, build scripts, plugins, and tooling.
For each boundary establish what the actor controls, the invariant to preserve,
where enforcement occurs, and the failure behavior. Repo configuration is not proof
of deployed configuration. The absence of an optional control is not automatically
a vulnerability; show the applicable scenario, requirement, and impact.

## Applicable review dimensions

| Dimension | Investigate |
| --- | --- |
| Inputs/outputs | Parsing, canonicalization, contextual validation/encoding, injection, serialization, unsafe deserialization |
| Identity/authority | Authentication, action/object/property permissions, least privilege, tenant/process isolation, revocation, context changes |
| Data/secrets | Storage, transit, cryptographic usage, key handling, logs/errors, exports, caches, artifacts, backups |
| Files/processes/network | Path traversal, links, temporary files, permissions, command/argument injection, outbound destinations, IPC |
| Business/state integrity | Replay, double effects, atomicity, idempotency, race/TOCTOU, partial success and recovery |
| Availability | CPU/memory/disk/connections, quotas, size/depth limits, timeouts, cancellation, resource release |
| Configuration/infrastructure | Defaults, exposure, identities, environment separation, flags, TLS, build/release configuration |
| Supply chain | Direct/transitive and vendored dependencies, lockfiles, install hooks, toolchains, pipelines, artifact integrity |
| Detection/recovery | Relevant audit events, protected logs, alerting where required, recovery, restoration of data and permissions |

For each applicable surface record control, scenario, evidence, and coverage status.
Do not mark an inaccessible surface safe or not applicable. Avoid universal control
checklists detached from a project's actual threat model.

## Evidence and tool use

Combine tracing with available relevant static analysis, dependency/secret scanning,
property testing, bounded fuzzing, or runtime instrumentation. Inspect effects before
execution; use synthetic inputs and isolation. No scanners or external services are
mandatory. A scanner alert needs reachability, configuration, control, and impact
analysis. A clean scanner result is limited to that scanner's checks.

For known vulnerabilities, consult the original advisory and verify affected/resolved
versions, actual resolved dependency, configuration, and relevant use. Distinguish
vulnerable presence, reachable vulnerable usage, and exploitable exposure. Development
dependencies can affect build/distribution; do not dismiss them solely by category.
When offline, mark advisory verification pending instead of inventing facts.

Use the versioned primary references indexed in sources.md when they resolve a real
question. Confirm exact CWE/CVE/standard IDs before using them. Use CVSS only with a
documented vector/version and justified assumptions. This workflow is not a security
certification, penetration-test authorization, or compliance assessment by default.

## Repair verification

Demonstrate expected rejection and successful authorized use. Consider other tenants,
identities, entry points, configuration states, and compatible versions. Keep reports
redacted. Separate code changes from operational actions such as deployment, rotating
exposed credentials, revoking sessions, restoring permissions, or repairing data.
Do not mark those actions complete when only the repository changed.
