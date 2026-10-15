# Microsoft Sentinel Repository Connections

This repository intentionally does not contain Azure credentials or a hand-built Azure deployment workflow.

## Branch model

- `main` = native rule inventory for inspection and source-control persistence under `Inventory/`.
- `deploy/<client-alias>` = isolated deployable content for exactly one Sentinel workspace.

Never connect a customer Sentinel workspace to `main`.

## For each real Sentinel workspace

1. Confirm `deploy/<client-alias>` exists and contains only that client's intended `SentinelContent/Analytic Rules/` content.
2. Create the Microsoft Sentinel repository connection to this repository and that specific deployment branch.
3. Select Analytics rules as the content type.
4. Let Sentinel create its workflow on that branch.
5. Keep the Sentinel-generated GitHub workflow intact. The source publisher updates only `SentinelContent/` on existing deployment branches and preserves all other branch files.

The branch boundary exists because Microsoft Sentinel deploys repository content when a connection is created; it avoids relying on a folder-scope customization that would only be available after the initial workflow is generated.
