# MS-Sentinel

Generated Microsoft Sentinel deployment repository.

**Do not hand-edit generated rule JSON.** Edit the source Sigma rule or Sentinel platform configuration in `Sigma-Rules`, then rebuild/publish.

## `main` branch = generated catalog

```text
Clients/
  <client-alias>/
    Solutions/
      <Solution>/
        Analytic Rules/
          <generated ARM template>.json
_build/
  build-manifest.json
```

Catalog client roots belong on `main`; deployment branches do not retain unrelated client content.

## `deploy/<client>` branches = live deployment boundaries

Each client/workspace gets an isolated branch containing only that client's deployable `SentinelContent/Analytic Rules/` content. `deploy/client-a` is the Leah OnMicrosoft deployment boundary.

**Connect Microsoft Sentinel to the relevant `deploy/<client>` branch, not to `main`.**

Every generated analytics rule is disabled by default.

See `docs/REPOSITORY_CONNECTIONS.md`.
