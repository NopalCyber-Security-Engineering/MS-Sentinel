# MS-Sentinel

Microsoft Sentinel native inventory and Git-backed deployment repository.

**Do not hand-edit managed rule JSON.** Inventory snapshots and deployment artifacts are published by Detection-Platform.

## `main` branch = native inventory

```text
Inventory/
  Leah OnMicrosoft/
    manifest.json
    Rules/
      <native rule>.json
```

The inventory is a read-back snapshot for inspection and source-control persistence. It is not a deployment tree, and Microsoft Sentinel must not be connected to `main`.

## `deploy/<client>` branches = live deployment boundaries

Each client/workspace gets an isolated branch containing only that client's deployable `SentinelContent/Analytic Rules/` content. `deploy/client-a` is the Leah OnMicrosoft deployment boundary.

**Connect Microsoft Sentinel to the relevant `deploy/<client>` branch, not to `main`.**

Managed deployment artifacts are disabled by default.

See `docs/REPOSITORY_CONNECTIONS.md`.
