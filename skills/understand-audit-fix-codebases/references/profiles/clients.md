# Mobile, desktop, games, and installed clients

Apply to native/hybrid apps, Flutter/Dart, desktop software, games, and plugins. Infer
the actual stack and lifecycle from manifests, configuration, and code. Combine with
Web, Services, Native, or Data when those components exist.

- Trace startup, navigation/scenes, state, persistence, background work, and shutdown.
  Inspect installation/update behavior, OS permissions, local secrets, databases,
  configuration, and separation between accounts.
- Check IPC, deep links, URL handlers, JS/native bridges, plugin loading, and the
  authority of the process handling privileged actions.
- Examine suspend/resume, crashes, restarts, connectivity changes, device changes,
  UI disposal while work is pending, and release of graphics/audio/file resources.
- For games, trace game/scene state, save/load, time handling, and client/server
  authority where present. Do not assume every game has a backend.
- For Flutter or other reactive clients, follow state subscriptions, async completion,
  cancellation/disposal, and persistence through UI lifecycles using the actual framework.
- After repair, check saved-data compatibility, authorized use, denied permissions,
  repeated events, restart/resume, offline recovery, and resource release.
- A simulator/emulator, a widget test, and a physical device establish different
  evidence. State hardware/platform combinations not verified.
