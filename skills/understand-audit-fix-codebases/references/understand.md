# UNDERSTAND — repository immersion

Produce a reusable, evidence-backed model of the requested codebase. Do not convert
onboarding into an exhaustive bug hunt or repair task. Use the common guardrails and
evidence rules; report incidental concerns with appropriate uncertainty.

## Establish the working context

Identify the repository/workspace root, relevant local changes, accessible files,
tools, and constraints. Read the README, applicable instructions, manifests,
configuration examples with secrets redacted, and architectural documents. Compare
documentation with code; do not adopt a README's claims as observed behavior.

Discover the project type, purposes/users, languages, runtime versions, package
boundaries, entry points, build/run/test configuration, and external integrations.
Git is optional. For archives, source fragments, or multiple roots, explain scope.
Use file search before broad reading; omit generated/vendor/cache bulk from detailed
inspection unless relevant, and record meaningful exclusions. A permission error is
a coverage limitation, not grounds to change filesystem permissions.

## Build a component map

Map components, responsibilities, entry points, dependencies, data stores, public
contracts, and trust boundaries. Identify authoritative state versus cache/projection,
configuration precedence, feature flags, and ownership/lifecycle of resources.
For a monorepo, discover packages and dependency edges before prioritizing deep traces.
Do not claim every file was inspected when using sampling.

Select critical flows using user priorities, central business behavior, exposed
interfaces, state mutation, and dependency fan-out. Trace from entry through validation,
transformation, authoritative effect, response/output, and relevant consumers.
For asynchronous work include producer, queue, consumer, acknowledgement, retries,
and recovery; for a library include callers, return values, exceptions, and side effects.
Read complete causal blocks rather than stopping at search snippets.

Record invariants grounded in evidence: permissions, tenant boundaries, idempotency,
transaction boundaries, ordering, units/precision, input/output formats, compatibility,
resource ownership, and error/cancellation behavior where applicable. Do not preserve
an apparent bug as a desired contract just because the code currently implements it.

## Determine how future work can be validated

Derive run/build/test commands from project configuration and inspect execution
effects. Execute only meaningful safe checks that improve understanding. Avoid
installing packages or booting services merely to make onboarding look complete.
If execution is unavailable, report documented commands as unexecuted and explain
the missing environment. Never claim the app ran based on static inspection.

Use the relevant component profiles to identify security-sensitive boundaries and
failure/recovery behavior. Read the security reference when a deeper security claim
is needed. An onboarding security map is not a completed security audit.

Build a change-impact map: area -> producers/consumers -> contract -> likely validation
-> risks. Include public exports, schemas, event payloads, saved data, migrations,
configuration, and deployment assumptions where relevant. Inspect history only to
resolve a concrete ambiguity; do not create a lengthy chronology without purpose.

## Counter-review and handoff

Challenge the component map and flow explanations against actual callers, imports,
configuration, and tests. Identify documentary contradictions and untraced external
boundaries. Summarize the counter-review and remaining unknowns.

Use the repository context template. Lead with a short context capsule that a later
session can reuse: purpose, stack, architecture, critical contracts, development
commands, change hotspots, and limitations. Cite file/symbol evidence. Include an
ordered reading path and a coverage ledger. Do not overwrite persistent project
instructions to manufacture memory; propose any useful additions separately.

Complete when the selected critical components/flows and their dependencies are
explained with evidence, validation paths and impact risks are recorded, and remaining
gaps are explicit. If a time or access limit prevents this, label the result Partial.
Report workspace changes; source/configuration should remain at the original state.
