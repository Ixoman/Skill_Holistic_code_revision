# SQL, ETL, notebooks, migrations, and analytical code

Trace source data, schemas, parsing, transformations, aggregation, persistence, and
consumption. Use synthetic or approved data; avoid copying production records.

- Check nulls, duplicates, decimal/money precision, units, timezone boundaries,
  ordering, join cardinality, filtering, constraints, and partition/batch boundaries.
- Verify transaction boundaries, idempotency, checkpoints, restart/recovery, and
  compatibility with existing schemas and data. Check content and counts; a successful
  query or pipeline exit is not proof of correct results.
- In notebooks, inspect cell dependencies, hidden state, and clean-kernel execution
  where safe and available. Separate model/statistical claims from code correctness.
- Review injection, privileges, costly queries, sensitive logs/exports, caches, and
  retention requirements grounded in actual policy.
- For migrations, inspect forward/backward compatibility and rollback constraints.
  Validate on disposable data; do not apply to a shared/production database merely
  because the migration command is available.
- After repair, check empty/boundary cases, historical formats, precision, duplicate
  handling, repeat runs, and downstream consumers. Do not invent business formulas,
  statistical assumptions, or retention periods.
