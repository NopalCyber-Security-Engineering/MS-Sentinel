#!/usr/bin/env python3
from pathlib import Path
import json
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
files = sorted(ROOT.glob("Clients/*/Solutions/*/Analytic Rules/*.json"))
if not files:
    print("VALIDATION FAILED: no generated Sentinel ARM templates found")
    raise SystemExit(1)

errors = []
for path in files:
    try:
        doc = json.loads(path.read_text(encoding="utf-8"))
    except Exception as exc:
        errors.append(f"{path}: invalid JSON: {exc}")
        continue
    resources = doc.get("resources", [])
    if len(resources) != 1:
        errors.append(f"{path}: expected exactly one resource")
        continue
    r = resources[0]
    if r.get("type") != "Microsoft.OperationalInsights/workspaces/providers/alertRules":
        errors.append(f"{path}: unexpected resource type")
    if r.get("apiVersion") != "2025-09-01":
        errors.append(f"{path}: expected apiVersion 2025-09-01")
    if r.get("kind") != "Scheduled":
        errors.append(f"{path}: expected Scheduled rule")
    p = r.get("properties", {})
    if p.get("enabled") is not False:
        errors.append(f"{path}: generated demo rule must be disabled")
    if not p.get("query"):
        errors.append(f"{path}: empty query")

if errors:
    print("VALIDATION FAILED")
    for error in errors:
        print(" -", error)
    raise SystemExit(1)
print(f"VALIDATION PASSED: {len(files)} generated Sentinel ARM template(s)")
