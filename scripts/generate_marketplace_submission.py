#!/usr/bin/env python3
import sys
import os
from pathlib import Path
import yaml
import requests


def load_marketplace_slugs() -> set[str]:
    url = "https://app.roocode.com/api/marketplace/modes"
    try:
        txt = requests.get(url, timeout=20).text
        data = yaml.safe_load(txt)
    except Exception as e:
        print(f"[error] failed to fetch marketplace modes: {e}", file=sys.stderr)
        return set()
    slugs: set[str] = set()
    for item in data.get("items", []):
        content = item.get("content")
        if isinstance(content, str):
            try:
                mode = yaml.safe_load(content)
                s = mode.get("slug")
                if s:
                    slugs.add(str(s))
            except Exception:
                pass
    return slugs


def pick_largest_modes(source_path: Path, exclude_slugs: set[str], top_n: int = 5):
    data = yaml.safe_load(source_path.read_text(encoding="utf-8"))
    modes = data.get("customModes", []) or []

    def size(m):
        return sum(len((m.get(k) or "")) for k in ("roleDefinition", "customInstructions", "whenToUse"))

    candidates = [m for m in modes if m.get("slug") and m["slug"] not in exclude_slugs]
    candidates.sort(key=size, reverse=True)
    return candidates[:top_n]


def make_item(mode: dict) -> dict:
    slug = mode["slug"]
    display_name = (mode.get("name") or slug).strip()
    # Use first line of roleDefinition as description
    rd = (mode.get("roleDefinition") or "").strip()
    description = rd.split("\n", 1)[0] or display_name

    # Build single-mode content YAML
    content_obj = {
        "slug": slug + ("-jtg" if not slug.endswith("-jtg") else ""),
        "name": display_name,
        "roleDefinition": mode.get("roleDefinition", ""),
        "groups": mode.get("groups", ["read", "edit", "browser", "command", "mcp"]),
    }
    if mode.get("whenToUse"):
        content_obj["whenToUse"] = mode["whenToUse"]
    if mode.get("customInstructions"):
        content_obj["customInstructions"] = mode["customInstructions"]

    content_yaml = yaml.safe_dump(content_obj, sort_keys=False, allow_unicode=True).rstrip()

    # Simple tags guess (optional)
    tags: list[str] = []
    lower_blob = (slug + " " + display_name + " " + rd).lower()
    for t in [
        "architecture",
        "security",
        "testing",
        "devops",
        "database",
        "seo",
        "docs",
        "ml",
        "ai",
        "compliance",
        "governance",
        "performance",
    ]:
        if t in lower_blob:
            tags.append(t)
    tags = sorted(set(tags))[:6]

    item = {
        "id": f"jtg-{slug}",
        "name": f"{display_name} (JTGSYSTEMS)",
        "description": description[:300],
        "author": "JTGSYSTEMS.COM",
        "authorUrl": "https://jtgsystems.com",
        "content": content_yaml,
    }
    if tags:
        item["tags"] = tags
    return item


def write_submission(items: list[dict], out_yaml: Path, out_issue: Path):
    # YAML items file
    lines: list[str] = ["items:"]
    for it in items:
        lines.append(f"  - id: {it['id']}")
        lines.append(f"    name: {it['name']}")
        lines.append(f"    description: {it['description']}")
        lines.append(f"    author: JTGSYSTEMS.COM")
        lines.append(f"    authorUrl: https://jtgsystems.com")
        if it.get("tags"):
            lines.append("    tags: [" + ", ".join(it["tags"]) + "]")
        lines.append("    content: |-")
        for ln in it["content"].splitlines():
            lines.append("      " + ln)
    out_yaml.parent.mkdir(parents=True, exist_ok=True)
    out_yaml.write_text("\n".join(lines) + "\n", encoding="utf-8")

    # Issue markdown
    title = "JTGSYSTEMS.COM: Submit 5 New Large Custom Modes Not in Marketplace"
    body = [
        "What kind of feedback?\n- Suggestion for new custom mode",
        "Item Type:\n- Custom Mode",
        "Description:",
        "Please add the following modes to the Roo Code Marketplace. Each item includes author credit and a single-mode YAML content block that follows the official schema.",
        "",
        "```yaml",
        *lines,
        "```",
    ]
    out_issue.write_text(f"# {title}\n\n" + "\n".join(body) + "\n", encoding="utf-8")


def main():
    # Use the active global custom_modes.yaml by default
    source = Path.cwd() / "custom_modes.yaml"
    if not source.exists():
        print(f"[error] could not find {source}", file=sys.stderr)
        sys.exit(1)

    exclude = load_marketplace_slugs()
    selected = pick_largest_modes(source, exclude, top_n=5)
    if not selected:
        print("[error] no modes selected", file=sys.stderr)
        sys.exit(2)

    items = [make_item(m) for m in selected]

    out_dir = Path(__file__).resolve().parents[1] / "submissions"
    out_yaml = out_dir / "marketplace-modes-jtgsystems.yaml"
    out_issue = out_dir / "issue-marketplace-jtgsystems.md"
    write_submission(items, out_yaml, out_issue)
    print(f"[ok] wrote:\n - {out_yaml}\n - {out_issue}")


if __name__ == "__main__":
    main()

