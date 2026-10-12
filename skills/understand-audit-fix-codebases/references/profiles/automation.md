# Scripts, CLI, macros, and automation

Apply to shell, PowerShell, Python, VBA, scheduled jobs, and similar automation.
Trace arguments/stdin/environment, validation, paths, transformations, subprocesses,
writes, stdout/stderr, and exit codes.

- Check quoting, expansion, command/argument injection, paths containing spaces or
  Unicode, separators, symlinks, temporary paths, permissions, and working directory.
- Check missing/empty inputs, open/locked files, partial output, replacement behavior,
  interruption, repeated execution, rollback where required, and resource cleanup.
- Treat stdout/stderr and exit codes as public contracts for callers and schedulers.
  A script can have real side effects without a web interface or authentication.
- In macros, inspect workbook/worksheet scope, active selection, events, cells,
  formulas, formats, error paths, application state, and restoration of settings.
  Do not silently operate on the currently selected sheet when the contract names one.
- Inspect help/import/startup paths before execution; they may run application code.
- After repair, use disposable fixtures to verify valid inputs, intended failures,
  filenames, repeated runs, and preservation of unrelated/pre-existing files.
- Do not assume Git, a build command, Bash on Windows, Excel availability, or server
  access. Explain when host-specific execution cannot be checked.
