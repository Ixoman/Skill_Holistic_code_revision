# Audit report

## Summary and scope
Skill version; date; root; requested/effective scope; profiles; exclusions; code state;
base/head for a diff; coverage limits; counts by confidence/category/severity.

## System and contract map
Critical components, flows, trust boundaries, and expected behavior sources.

## Confirmed findings
For each: ID/title; category/confidence/severity with rationale; method; locations and
revision; contract; expected/actual; reachable preconditions/flow; impact and consumers;
reproduction/static proof; refutation; existing tests; repair direction; regression
check; exposure/actor/controls if security-related; remaining limitations.

## Probable findings and possible hypotheses
Keep separate from confirmed counts. State the evidence needed to resolve each.

## Hardening and maintainability suggestions
Keep non-defect suggestions separate and explain their optional scope.

## Coverage and validation
Component/contract/scenario | Coverage status | Evidence | Limit
Command/check | Executed/static/blocked | Actual result | Interpretation

## Counter-review and discarded candidates
Candidate | Contrary evidence | Disposition
Describe actual self-review or separate reviewer and scope; no invented independence.

## Repair order, gaps, and final state
Dependencies/priorities, outstanding decisions, unverified surfaces, actual workspace
changes, and report path. Do not claim absence of all defects or security certification.
