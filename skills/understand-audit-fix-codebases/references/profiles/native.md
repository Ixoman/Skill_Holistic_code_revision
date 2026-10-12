# Native code, unsafe regions, FFI, and embedded systems

Apply to C/C++, unsafe code, native interfaces, drivers, firmware, and hardware-facing
components within the authorized scope. Use available analysis without assuming
access to the target device or permission to flash/run on it.

- Inspect ownership/lifetime, buffer bounds, use-after-free, double release,
  initialization, numeric conversion/alignment, and undefined behavior.
- Trace locks, atomics, memory ordering, races, interrupt/reentrancy behavior,
  deadlines, cancellation, and shutdown.
- Check FFI/ABI types, lengths, layout/packing, encoding, ownership transfer, and errors.
- Use existing analyzers/sanitizers when relevant. Use bounded fuzzing for parsers or
  formats in an isolated harness; inspect effects first.
- Do not treat successful compilation as proof of memory safety, thread safety, or
  real-time timing. Distinguish simulation from actual device evidence.
- After repair, check legitimate/boundary inputs, resource ownership, ABI/protocol
  compatibility, and affected callers. Hardware execution or firmware deployment
  requires authority and a suitable environment; document any missing evidence.
