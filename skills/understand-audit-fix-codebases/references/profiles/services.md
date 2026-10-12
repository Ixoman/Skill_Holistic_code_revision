# APIs, workers, distributed systems, and synchronization

Trace input, identity/authority where present, business rule, authoritative commit,
cache/projection/outbox/event, integration, response/acknowledgement, and recovery.

- Check action/object/property authorization, tenant/service identity isolation,
  webhook signatures, replay protection, endpoint inventory, serialization/errors,
  outbound targets/SSRF, and resource limits as applicable.
- Verify transactions, idempotency, ordering, duplicate delivery, retry policies,
  timeouts, and compatibility with older clients, queued payloads, and persisted data.
- For local-first systems, identify local/remote sources of truth, conflict resolution,
  invalidation, outbox processing, revocation, and reconnection behavior.
- Examine pending work across session, permission, device, and flag changes.
- Select relevant failure interleavings: retry/double submit; concurrent actors;
  late/out-of-order response; failure before commit; failure after commit but before
  projection/ack/response; shutdown/restart; schema upgrade/restore; timeout then retry.
  Use deterministic hooks/barriers where available; a sleep alone does not establish
  an intended ordering.
- Inspect all affected stores/projections, not only the HTTP result or visible UI.
  A mock of an external service establishes only the mocked contract.
- After repair, verify legitimate actors and denied actors, repeat delivery, affected
  consumers, partial failures, and resource cleanup. Label deployed behavior unknown
  when only repository configuration is available.
