# AUDIT — bugs and security

Apply the common guardrails, evidence rules, security reference, and relevant profiles.
Investigate the requested scope; deliver findings without source repairs.

## Frame the audit

Record root, code state, baseline local changes, scope, priorities, exclusions,
available validation, and prior reports. Default to functional correctness and
applicable security within scope. Keep style/maintainability suggestions separate.
Identify public contracts, critical flows, trust boundaries, and high-impact state.

For a diff/PR audit, identify the exact base/head or the requested working-tree diff.
If that cannot be inferred reliably, ask. Trace changed code through unchanged callers
and consumers, but distinguish newly introduced, pre-existing, and origin-unverified
defects. Do not attribute a historical bug to the PR without baseline evidence.

Build a coverage ledger before searching only for likely bugs. Track component,
contract, relevant scenarios, evidence, and coverage status. Prioritize by impact and
reachability; do not impose quotas of files, findings, or test cases.

## Trace and challenge behavior

Trace a reachable input through validation, authority checks, business rules, effects,
output, and consumers. Include durable state, projections, asynchronous work, and
failure recovery when present. Establish the expected behavior from evidence.

Choose pertinent scenarios: valid use; empty/boundary/malformed input; repetition;
concurrency; cancellation; resource exhaustion; partial failures; stale state; changes
of identity/permissions/configuration; retries after timeout; prior-format data;
upgrade/recovery; and producer/consumer compatibility. Select high-risk combinations,
not the Cartesian product of every scenario.

Treat tests, static analysis, scanners, TODOs, logs, and historical findings as leads.
Apply the defect quality gate to each candidate. Search actively for controls and
contrary evidence. Reproduce safely with existing tools or construct a complete static
proof. Record exactly which steps were executed; do not run a destructive exploit to
obtain evidence already established by source and isolated tests.

For performance, connect a reachable workload to meaningful complexity, measurements,
or resource impact. Missing memoization or an extra loop is not automatically a bug.
For dependencies, separate package presence, affected version, vulnerable usage,
and exploitability; inspect development/build exposure as well as runtime exposure.

## Counter-review

Perform a second pass over the component/contract map, not only the candidate list.
Challenge assumptions about defaults, callers, permissions, flags, transaction
boundaries, error paths, and legitimate behavior. Review cross-component effects and
routes equivalent to the reported route. Track discarded candidates with reasons.

Use a separate reviewer only when available and permitted; otherwise perform and
identify a self-counter-review. Do not claim independence from a change of persona.
Stop repeated passes when they do not resolve a concrete risk or missing requirement.

## Deliver and finish

Use the audit report template. Separate Confirmed, Probable, Possible, and non-defect
suggestions; never count hypotheses as confirmed bugs. Preserve original finding IDs,
deduplicate by cause without losing surfaces, and propose repair order with rationale.

Include evidence, refutation, expected/actual behavior, impact, repair direction,
observable regression checks, executed/static/blocked checks, coverage/exclusions,
and final workspace state. Preserve prior reports unless updating them was requested.

Complete when the selected scope has a coverage disposition, critical reachable
contracts have been traced or explicitly blocked, and each reported candidate has
passed the relevant evidence/refutation gate. Label incomplete coverage Partial.
No findings is an acceptable result; it does not establish absence of all defects.
