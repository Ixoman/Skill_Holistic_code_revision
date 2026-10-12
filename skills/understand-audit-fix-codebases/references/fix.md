# FIX — revalidation and remediation

Apply the common guardrails and evidence rules. Read security guidance for security
findings or trust-boundary changes and the profiles affected by the proposed repair.

## Establish repair input and authorization

Accept a report, issue/ticket, reproducible symptom, failing test, or explicit defect
description. If the user has provided no identifiable problem, ask for one or offer
AUDIT; do not silently turn FIX into unrestricted cleanup.

Explicit IDs define the selected scope. If the user asks to fix an entire report,
triage every reported defect and repair only those confirmed against current code.
Probable/Possible candidates need validation before promotion. Hardening, style,
and independent enhancements are not automatically selected as repairs.

Record the current baseline and preserve pre-existing changes. Trace enough context
to understand the target contracts; do not require full onboarding for a local fix.

## Revalidate every selected item

Even a previously confirmed report may be stale. Record original ID/confidence,
current evidence, reproduction/proof, root cause, dependencies, and disposition:
Valid, Promoted, Stale, Duplicate, False positive, or Blocked.

Find the real callers, controls, deployment assumptions, and consumers. Do not repair
code solely to match a report's recommendation. A complete deterministic static
chain can confirm a defect when execution is unavailable; declare remaining validation
limits. Unknown production exposure does not negate a demonstrated code defect.

Account for every selected ID. A blocked group must not stop independent valid groups.

## Plan the smallest complete causal repair

For each cause, identify affected entry points, downstream consumers, public API/error
semantics, data formats, transactions, caches, concurrency, security, and compatibility.
Choose the minimum change that restores the intended contract across the affected
paths. Include indispensable same-cause corrections while explaining their relation.
Record independent discoveries separately instead of expanding repair scope.

Use the existing stack and conventions. A necessary local refactor or minimal
dependency/lockfile correction is allowed; avoid unrelated modernization. For data
schema changes, validate compatibility and rollback in disposable data. Executing
production migrations or repairing live records requires separate effective authority.

## Verify before and after

Where feasible, reproduce the original failure before editing and show the same
scenario succeeding afterward. Test externally observable behavior, not source text
that mirrors the patch. Use existing meaningful coverage where sufficient.

Select checks based on the contract and affected consumers: normal use, boundary/error
cases, other callers, retry/concurrency behavior, older formats/versions, and resource
cleanup. For security, verify both unauthorized rejection and legitimate authorized
success, including alternate identities/tenants and equivalent routes as applicable.

Do not add a test just to satisfy a quota. If a meaningful check cannot run, explain
what blocks it and whether that prevents verified closure. Static proof, compilation,
mocked calls, and real integrations establish different things; label them accurately.

Implement in coherent causal groups. After each group, run the relevant safe checks,
inspect the actual diff, and compare to baseline. Fix patch-induced failures before
moving that group to complete. Undo only your identifiable changes if needed. Do not
hide failures by relaxing assertions or security controls.

Run required project gates when safe and available. Broaden validation only for a
concrete residual risk or required gate; reuse results for unchanged code. Distinguish
baseline failures, introduced failures, environment issues, and unresolved outcomes.
With Git, inspect relevant diffs/whitespace; without it, compare protected content.

## Counter-review and closure

Re-read the patch from the perspective of other callers and legitimate users. Try to
refute the repair: incomplete routes, rejection of valid input, weakened checks, stale
state, races, changed error/serialization contracts, leaked resources, and tests that
prove only their mocks. Use independent review only when actually performed.

Assign a final state to each selected ID:

- Resolved and verified: defect confirmed, correction present, relevant verification
  supports the claim, and no required material check remains blocked.
- Implemented; validation pending: correction exists but material verification is missing.
- Discarded with evidence: stale, false positive, or already resolved; state which.
- Duplicate of ID: retain the link and relevant affected surfaces.
- Blocked: input, authority, environment, or a material contract decision is missing.

Use the remediation template. List changed files and causes, checks/results, remaining
risks, operational follow-ups, and final workspace state. A code patch does not imply
deployment, credential rotation, or live-data repair. Finish after every selected ID
has a disposition and all feasible required checks/counter-review are complete.
