#!/usr/bin/env python3
"""
Verify compiled .roomodes and individual custom_modes.d/ files for quality issues.

Checks:
- YAML parseability
- Required schema fields (slug, name, roleDefinition, groups)
- Slug format (a-zA-Z0-9- only, no double dashes)
- Duplicate slugs
- description != roleDefinition (they should differ)
- roleDefinition length (should be substantial)
- whenToUse not a circular placeholder
- No unsupported fields (emoji, category, version, lastUpdated)
- Groups are valid (read, edit, browser, command, mcp)
"""
import re
import sys
from pathlib import Path

try:
    import yaml
except ImportError:
    print("ERROR: PyYAML required. Install with: pip install pyyaml")
    sys.exit(1)

REPO_ROOT = Path(__file__).parent.parent
REQUIRED_KEYS = {"slug", "name", "roleDefinition", "groups"}
ALLOWED_KEYS = {"slug", "name", "roleDefinition", "description", "whenToUse", "customInstructions", "groups", "source"}
ALLOWED_GROUPS = {"read", "edit", "browser", "command", "mcp"}
SLUG_PATTERN = re.compile(r'^[a-zA-Z0-9-]+$')
PLACEHOLDER_WHEN = re.compile(r'^Use when you need .* expertise\.$', re.IGNORECASE)


def verify_mode(mode: dict, source: str) -> list:
    """Return list of issue strings for a single mode."""
    issues = []
    slug = mode.get("slug", "UNKNOWN")
    prefix = f"[{source}] {slug}"

    # Required fields
    missing = REQUIRED_KEYS - set(mode.keys())
    if missing:
        issues.append(f"{prefix}: MISSING required fields: {missing}")

    # Slug format
    if not SLUG_PATTERN.match(slug):
        issues.append(f"{prefix}: INVALID slug format: '{slug}'")
    if "--" in slug:
        issues.append(f"{prefix}: DOUBLE DASH in slug: '{slug}'")

    # Unsupported fields
    extra = set(mode.keys()) - ALLOWED_KEYS
    if extra:
        issues.append(f"{prefix}: UNSUPPORTED fields: {extra}")

    # Groups
    groups = mode.get("groups", [])
    if not isinstance(groups, list):
        issues.append(f"{prefix}: groups is not a list")
    else:
        # Each entry is either a simple permission name (str) or the
        # schema-valid array form [edit, {fileRegex, description}].
        invalid_groups = []
        for g in groups:
            if isinstance(g, list):
                if len(g) != 2 or g[0] != "edit" or not isinstance(g[1], dict):
                    invalid_groups.append(f"malformed array-form group: {g!r}")
            elif g not in ALLOWED_GROUPS:
                invalid_groups.append(g)
        if invalid_groups:
            issues.append(f"{prefix}: INVALID groups: {invalid_groups}")
        if not groups:
            issues.append(f"{prefix}: EMPTY groups list")

    # Description vs roleDefinition
    desc = (mode.get("description") or "").strip()
    role = (mode.get("roleDefinition") or "").strip()
    if desc and role and desc == role:
        issues.append(f"{prefix}: IDENTICAL description and roleDefinition")

    # roleDefinition length
    if role and len(role) < 150:
        issues.append(f"{prefix}: SHORT roleDefinition ({len(role)} chars)")

    # Placeholder whenToUse
    when = (mode.get("whenToUse") or "").strip()
    if when and PLACEHOLDER_WHEN.match(when):
        issues.append(f"{prefix}: PLACEHOLDER whenToUse")

    # Empty fields
    for field in ["name", "slug", "roleDefinition"]:
        val = (mode.get(field) or "").strip()
        if not val:
            issues.append(f"{prefix}: EMPTY {field}")

    return issues


def verify_compiled(path: Path) -> tuple[int, list]:
    """Verify a compiled file (.roomodes or custom_modes.yaml)."""
    issues = []
    try:
        with open(path) as f:
            data = yaml.safe_load(f)
    except yaml.YAMLError as e:
        return 0, [f"YAML PARSE ERROR in {path}: {e}"]

    if not isinstance(data, dict) or "customModes" not in data:
        return 0, [f"MISSING customModes key in {path}"]

    modes = data.get("customModes", [])
    slugs = []
    for mode in modes:
        if not isinstance(mode, dict):
            issues.append(f"[{path}] Non-dict entry in customModes")
            continue
        slugs.append(mode.get("slug", "UNKNOWN"))
        issues.extend(verify_mode(mode, str(path.name)))

    # Duplicate slugs
    seen = set()
    for slug in slugs:
        if slug in seen:
            issues.append(f"[{path.name}] DUPLICATE slug: {slug}")
        seen.add(slug)

    return len(modes), issues


def verify_individual_files() -> tuple[int, list]:
    """Verify all custom_modes.d/*/*.yaml files."""
    issues = []
    total = 0
    d = REPO_ROOT / "custom_modes.d"
    for f in sorted(d.rglob("*.yaml")):
        try:
            with open(f) as fh:
                data = yaml.safe_load(fh)
        except yaml.YAMLError as e:
            issues.append(f"[{f}] YAML PARSE ERROR: {e}")
            continue

        if not isinstance(data, dict) or "customModes" not in data:
            issues.append(f"[{f}] MISSING customModes wrapper")
            continue

        modes = data.get("customModes", [])
        for mode in modes:
            total += 1
            rel = f.relative_to(REPO_ROOT)
            issues.extend(verify_mode(mode, str(rel)))

    return total, issues


def main():
    print("=" * 60)
    print("Custom Modes Verifier")
    print("=" * 60)

    all_issues = []

    # Verify compiled files
    for filename in [".roomodes", "custom_modes.yaml"]:
        path = REPO_ROOT / filename
        if path.exists():
            count, issues = verify_compiled(path)
            print(f"\n{filename}: {count} modes")
            all_issues.extend(issues)
        else:
            print(f"\n{filename}: NOT FOUND")

    # Verify individual files
    print("\ncustom_modes.d/ individual files:")
    count, issues = verify_individual_files()
    print(f"  {count} modes")
    all_issues.extend(issues)

    # Report
    print(f"\n{'=' * 60}")
    if not all_issues:
        print("✅ ALL CHECKS PASSED")
        return 0

    # Categorize
    categories = {}
    for issue in all_issues:
        cat = issue.split(":")[-1].strip().split()[0]
        categories.setdefault(cat, []).append(issue)

    print(f"❌ {len(all_issues)} issues found:\n")
    for cat in sorted(categories.keys()):
        items = categories[cat]
        print(f"  {cat}: {len(items)}")
        for item in items[:5]:
            slug = item.split(":")[0].split("]")[-1].strip()
            print(f"    - {slug}")
        if len(items) > 5:
            print(f"    ... and {len(items) - 5} more")

    # Write full report
    report_path = REPO_ROOT / "verify_report.txt"
    with open(report_path, "w") as f:
        f.write(f"Custom Modes Verification Report\n")
        f.write(f"{'=' * 60}\n")
        f.write(f"Total issues: {len(all_issues)}\n\n")
        for issue in sorted(all_issues):
            f.write(f"{issue}\n")
    print(f"\nFull report written to: {report_path}")

    return 1


if __name__ == "__main__":
    sys.exit(main())
