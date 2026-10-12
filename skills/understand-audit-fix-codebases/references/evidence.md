# Evidence, findings, and continuity

## Defect quality gate

Before counting a defect or repairing it, establish:

1. The inspected file/symbol and current code state.
2. A reachable entry, realistic preconditions, callers, and consumers.
3. The expected contract, grounded in requirements, public behavior, tests, or callers.
4. Actual behavior, established by reproduction or a complete deterministic trace.
5. An attempt to refute it: validation, guards, permissions, flags, transactions,
   runtime behavior, deployment conditions, and contrary evidence.
6. The impact and legitimate behavior that a correction must preserve.

A TODO, scanner warning, missing test, old package version, naming preference, or
suspicious line is a lead, not proof. Existing tests may already catch the problem.
Implementation shows behavior, not necessarily intent. Ask or label uncertainty
when an ambiguous business contract changes the conclusion.

## Separate dimensions

| Dimension | Values / interpretation |
| --- | --- |
| Category | Functional, Security, Both; keep Maintainability/Hardening suggestions separate |
| Confidence | Confirmed: reproduced or fully demonstrated; Probable: strong reachable case with an unresolved decisive piece; Possible: hypothesis |
| Method | Dynamic, Static, Mixed; state actual checks |
| Severity | Critical, High, Medium, Low; justify impact, preconditions, and scope |
| Exposure | Verified, Conditional, Unknown, or Not applicable; code proof does not prove production exposure |
| Priority | Repair order considering severity, dependencies, exposure, and user goals |

Critical involves severe compromise, major irreversible loss, or widespread critical
unavailability under credible conditions. High affects core behavior or significant
access/data. Medium is limited or recoverable impact; Low is a bounded defect with
a practical workaround. Do not infer severity from a weakness name. Do not assign
defect severity to stylistic suggestions.

Distinguish source code, observed execution, documentation, user requirements,
inference, and unknowns. Use concise labels where useful. Provide evidence and short
rationale, not hidden reasoning.

## Finding record

Keep original IDs and source report identity. For new findings use BUG-001, BUG-002,
and so on without collisions. Group duplicates by root cause and surface; preserve
affected routes/consumers and link duplicate IDs instead of renumbering.

Include ID/title; category/confidence/severity/method; revision and locations;
expected versus actual behavior; contract; preconditions and flow; impact; reproduction
or deterministic proof; refutation; existing coverage; repair direction; and observable
verification. Verify line numbers before citing them.

For security add actor capabilities, trust boundary, controls reviewed, exposure,
redacted evidence, and verified advisory/taxonomy references when useful. Never invent
CVE/CWE IDs, affected ranges, CVSS scores, or compliance claims. If using CVSS, record
version, vector, source/calculation, and assumptions; otherwise omit the score.

## Coverage and results

Track components/contracts and scenarios as Reviewed, Partial, Blocked, Excluded,
or Not applicable, with evidence/reasons. No search match does not prove absence.
Sampling does not establish complete coverage. An empty findings list is not a
security guarantee.

Separate executed, static, blocked, and irrelevant checks. Classify failures as
baseline, introduced, environmental, or unresolved only with evidence. A passing mock
does not prove integration; simulation does not establish physical hardware behavior.

## Stable handoff

Reports identify version, date, root, mode, requested/effective scope, exclusions,
profiles, code state, checks, limits, and workspace changes. With Git, record commit
and relevant local modifications. Without it, use bounded inventory/hashes. A commit
does not identify a dirty working tree.

Revalidate saved context and selected findings against current code. Map stale and
duplicate findings explicitly. Preserve the input report. Record code correction
separately from deployment, data repair, or secret rotation still pending. A saved
report is a handoff artifact, not permanent model memory.
