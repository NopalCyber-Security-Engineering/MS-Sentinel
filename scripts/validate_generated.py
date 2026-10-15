#!/usr/bin/env python3
from pathlib import Path
import json

ROOT = Path(__file__).resolve().parents[1]
errors = []


def load_json(path):
    try:
        return json.loads(path.read_text(encoding="utf-8-sig"))
    except Exception as exc:
        errors.append(f"{path}: invalid JSON: {exc}")
        return None


inventory_manifests = sorted(ROOT.glob("Inventory/*/manifest.json"))
inventory_rules = []
for manifest_path in inventory_manifests:
    manifest = load_json(manifest_path)
    if manifest is None:
        continue

    rules = sorted((manifest_path.parent / "Rules").glob("*.json"))
    inventory_rules.extend(rules)
    if manifest.get("display_name") != manifest_path.parent.name:
        errors.append(f"{manifest_path}: display_name must match its inventory directory")
    if not manifest.get("client"):
        errors.append(f"{manifest_path}: missing client identifier")
    if manifest.get("platform") != "microsoft-sentinel":
        errors.append(f"{manifest_path}: expected platform microsoft-sentinel")
    if manifest.get("rule_count") != len(rules):
        errors.append(
            f"{manifest_path}: rule_count is {manifest.get('rule_count')}, found {len(rules)} rule files"
        )
    for path in rules:
        load_json(path)

arm_files = sorted(ROOT.glob("SentinelContent/Analytic Rules/*.json"))
for path in arm_files:
    doc = load_json(path)
    if doc is None:
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
        errors.append(f"{path}: generated rule must be disabled")
    if not p.get("query"):
        errors.append(f"{path}: empty query")

if not inventory_manifests and not arm_files:
    errors.append("no Sentinel inventory or deployment content found")

if errors:
    print("VALIDATION FAILED")
    for error in errors:
        print(" -", error)
    raise SystemExit(1)
print(
    "VALIDATION PASSED: "
    f"{len(inventory_manifests)} inventory manifest(s), "
    f"{len(inventory_rules)} native inventory rule(s), "
    f"{len(arm_files)} deployable ARM template(s)"
)
