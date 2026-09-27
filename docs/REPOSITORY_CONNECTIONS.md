# Microsoft Sentinel Repository Connections

This repository intentionally does not contain Azure credentials or a hand-built Azure deployment workflow.

## Branch model

- `main` = generated catalog for the team; contains all clients under `Clients/`.
- `deploy/<client-alias>` = isolated deployable content for exactly one Sentinel workspace.

Never connect a customer Sentinel workspace to `main`.

## For each real Sentinel workspace

1. Confirm `deploy/<client-alias>` exists and contains only that client's intended `Solutions/...` content.
2. Create the Microsoft Sentinel repository connection to this repository and that specific deployment branch.
3. Select Analytics rules as the content type.
4. Let Sentinel create its workflow on that branch.
5. Keep the generated workflow and `.sentinel` state intact. The source publisher updates only `Solutions/` on existing deployment branches.

The branch boundary exists because Microsoft Sentinel deploys repository content when a connection is created; it avoids relying on a folder-scope customization that would only be available after the initial workflow is generated.
