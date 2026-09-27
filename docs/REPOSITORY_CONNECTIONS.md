# Microsoft Sentinel Repository Connections

This repository intentionally does not contain Azure credentials or a hand-built Azure deployment workflow.

For each real Sentinel workspace:

1. Create the Microsoft Sentinel repository connection to this GitHub repository.
2. Let Sentinel generate its deployment workflow.
3. Edit that generated workflow so both its push path and deployment directory are scoped to the matching root, for example:

```text
Clients/client-a/**
```

and:

```text
${{ github.workspace }}/Clients/client-a
```

4. Repeat for the other workspaces using different client roots.

This provides centralized generated content while preventing a change for one client from being deployed to every Sentinel workspace.

Before doing this, replace the five `demo-client-*` roots in the source project with verified client aliases and rule assignments.
