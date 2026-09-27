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

The checked-in `demo-client-01` ... `demo-client-05` roots are placeholders proving multi-workspace fan-out. They are not real customer mappings.

## `deploy/<client>` branches = live deployment boundaries

Each client/workspace gets an isolated branch containing only that client's deployable `Solutions/...` tree.

**Connect Microsoft Sentinel to the relevant `deploy/<client>` branch, not to `main`.**

Every generated analytics rule is disabled by default.

See `docs/REPOSITORY_CONNECTIONS.md`.
