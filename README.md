# MS-Sentinel

Generated Microsoft Sentinel deployment repository.

**Do not hand-edit generated rule JSON.** Edit the source Sigma rule or Sentinel platform configuration in `Sigma-Rules`, then rebuild/publish.

## Layout

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

Every generated analytics rule is disabled by default.

## Live deployment model

When a real Microsoft Sentinel workspace is connected through Content management / Repositories, let Microsoft create the repository deployment workflow. Scope that generated workflow to exactly one `Clients/<client-alias>` root. Do not create a shared custom Azure deployment credential in this repository just to bypass Sentinel Repositories.

See `docs/REPOSITORY_CONNECTIONS.md`.
