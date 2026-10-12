# Libraries, SDKs, packages, and algorithms

Trace preconditions, transformations, results, exceptions, and side effects. Establish
contracts from public documentation, callers, tests, and supported compatibility.

- Check empty/boundary inputs, numeric precision/overflow, invalid values, aliasing,
  mutation, iterators, cancellation, lifetime, and resource cleanup where applicable.
- A documented in-place operation may mutate its input legitimately. Do not rewrite
  it as a pure operation solely because mutation looks suspicious.
- Follow public exports and consumers; examine API signatures, types, error semantics,
  serialization, ordering, and version compatibility beyond the edited function.
- Verify package contents, imports/exports, initialization side effects, optional
  dependencies, and the affected supported runtime combinations.
- Prefer behavioral edge cases or properties that express the actual invariant.
  Include integration checks when the defect depends on a real consumer/resource.
- Distinguish algorithmic complexity from measured production performance. Do not
  invent workloads, accuracy targets, or numerical tolerance requirements.
- After repair, prove the original case and affected normal/boundary behavior. Do not
  force authentication or transaction checks onto a pure local algorithm.
