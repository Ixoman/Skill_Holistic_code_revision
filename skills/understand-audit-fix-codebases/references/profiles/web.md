# Web, frontend, static sites, and browser extensions

Apply to browser interfaces, server-rendered pages, SPAs, static sites, forms, service
workers, and extensions. Combine with Services for backend behavior.

- Trace routing, links, forms, validation, hydration, state updates, and visible output.
  Identify the authoritative validation/authorization boundary; UI checks alone may
  not enforce a server-side contract.
- Check loading/error/empty states, back/forward navigation, stale requests, canceled
  work, session changes, shared caches/storage, and UI/backend disagreement.
- Check functional keyboard access and relevant viewport sizes when they affect the
  requested behavior. Separate accessibility defects from aesthetic preferences;
  do not claim a full accessibility certification from selected checks.
- Trace untrusted data into HTML/URLs/scripts/styles and other output contexts.
  Review XSS, CSRF when ambient credentials apply, cookie attributes, redirects,
  origins/CORS, appropriate CSP, bundles, external resources, and postMessage handling.
- For extensions, inspect manifest permissions, content/background scripts, origin
  boundaries, messaging, and storage exposure. For offline workers, inspect cache
  invalidation and account isolation.
- After repair, verify authorized success, expected rejection, navigation, and other
  consumers of the changed state/contract. Distinguish code inspection from actual
  browser behavior. Do not require backend controls for a site with no backend.
