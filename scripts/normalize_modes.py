import os
import re
import json
from datetime import datetime

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def load_json(path):
    try:
        with open(path, 'r', encoding='utf-8') as f:
            return json.load(f)
    except Exception:
        return None


def save_json(path, data):
    with open(path, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
        f.write("\n")


def clean_text(txt: str) -> str:
    if not isinstance(txt, str):
        return txt
    out = txt
    # Remove ' - ULTRON ...' from markdown headings
    def _clean_heading(line: str) -> str:
        if line.lstrip().startswith('#') and 'ULTRON' in line:
            return re.sub(r"\s+-\s+ULTRON[^\n]*", "", line)
        return line

    lines = out.splitlines()
    lines = [_clean_heading(ln) for ln in lines]
    out = "\n".join(lines)

    # Replace standalone ULTRON tokens
    out = re.sub(r"\bULTRON\b\s*", "", out)
    # Collapse multiple spaces introduced by removals
    out = re.sub(r"[ \t]{2,}", " ", out)
    # Tidy spaces before punctuation
    out = re.sub(r"\s+([,.;:!?])", r"\1", out)
    return out


def normalize_mode(mode: dict) -> dict:
    # Name: drop ULTRON suffix or mentions
    name = mode.get('name', '')
    name = re.sub(r"\s*ULTRON\s*$", "", name, flags=re.IGNORECASE)
    mode['name'] = name

    # Slug: remove -ultron suffix
    slug = mode.get('slug', '')
    if isinstance(slug, str) and slug.endswith('-ultron'):
        mode['slug'] = slug[:-7]

    # Clean textual fields
    for key in ('roleDefinition', 'whenToUse', 'customInstructions'):
        if key in mode:
            mode[key] = clean_text(mode[key])

    return mode


def walk_mode_files():
    for root, dirs, files in os.walk(REPO_ROOT):
        if not root.endswith('-modes'):
            continue
        for fn in files:
            if not fn.endswith('.json'):
                continue
            if fn in {'.vscode', 'cline_custom_modes.json'}:
                continue
            path = os.path.join(root, fn)
            yield path


def rename_if_needed(path: str) -> str:
    dirname, basename = os.path.split(path)
    if basename.endswith('-ultron.json'):
        new_basename = basename.replace('-ultron.json', '.json')
        new_path = os.path.join(dirname, new_basename)
        if os.path.exists(new_path):
            return path
        os.rename(path, new_path)
        return new_path
    return path


def build_master_index():
    categories_meta = {
        'ai-modes': ("Artificial Intelligence & Machine Learning", "Advanced AI/ML development and intelligent systems"),
        'advanced-development-modes': ("Advanced Development", "Emerging technologies and specialized development"),
        'business-modes': ("Business Strategy & Management", "Strategy, product, marketing, and operations"),
        'creative-modes': ("Creative & Design", "Creative direction, design, and content"),
        'data-modes': ("Data Science & Analytics", "Analytics, modeling, and insights"),
        'development-modes': ("Software Development", "Full-stack development and engineering"),
        'education-modes': ("Education & Training", "Learning and instructional design"),
        'engineering-modes': ("Infrastructure & Engineering", "Cloud, DevOps, and platform engineering"),
        'finance-modes': ("Finance & Investment", "Financial analysis and planning"),
        'health-modes': ("Health & Wellness", "Healthcare and wellness"),
        'legal-modes': ("Legal & Compliance", "Law, compliance, and governance"),
        'research-modes': ("Research & Science", "Scientific research and methodology"),
        'security-modes': ("Cybersecurity & Risk", "Security, risk, and compliance"),
        'seo-modes': ("Search Engine Optimization", "Technical SEO and content optimization"),
    }

    categories = {}
    total = 0
    for root, dirs, files in os.walk(REPO_ROOT):
        if not root.endswith('-modes'):
            continue
        rel_dir = os.path.relpath(root, REPO_ROOT)
        title, desc = categories_meta.get(rel_dir, (rel_dir, ""))
        modes = []
        for fn in sorted(files):
            if not fn.endswith('.json'):
                continue
            if fn in {'.vscode', 'cline_custom_modes.json'}:
                continue
            path = os.path.join(root, fn)
            data = load_json(path)
            if not data or 'customModes' not in data:
                continue
            for m in data['customModes']:
                slug = m.get('slug')
                name = m.get('name')
                role = m.get('roleDefinition', '')
                desc_text = ''
                if isinstance(role, str) and role:
                    s = role.strip()
                    end = s.find('.')
                    desc_text = s if end == -1 else s[: end + 1]
                    desc_text = desc_text.strip()
                modes.append({
                    'slug': slug,
                    'name': name,
                    'file': os.path.relpath(path, REPO_ROOT),
                    'description': desc_text,
                })
                total += 1
        if modes:
            categories[rel_dir] = {
                'title': title,
                'description': desc,
                'modes': modes,
            }

    return {
        'masterIndex': {
            'title': 'Custom Modes Collection',
            'version': '2.1.0',
            'generated': datetime.utcnow().strftime('%Y-%m-%dT%H:%M:%SZ'),
            'totalModes': total,
            'categories': categories,
        }
    }


def main():
    changed_files = []
    renamed = []
    for path in list(walk_mode_files()):
        data = load_json(path)
        if not data or 'customModes' not in data:
            continue
        original = json.dumps(data, ensure_ascii=False, sort_keys=True)
        for i, m in enumerate(data['customModes']):
            data['customModes'][i] = normalize_mode(m)
        updated = json.dumps(data, ensure_ascii=False, sort_keys=True)
        if updated != original:
            save_json(path, data)
            changed_files.append(path)
        new_path = rename_if_needed(path)
        if new_path != path:
            renamed.append((path, new_path))

    index = build_master_index()
    index_path = os.path.join(REPO_ROOT, '00-MASTER-INDEX.json')
    save_json(index_path, index)
    changed_files.append(index_path)

    print("Updated files:")
    for f in changed_files:
        print(" -", os.path.relpath(f, REPO_ROOT))
    if renamed:
        print("Renamed:")
        for a, b in renamed:
            print(" -", os.path.relpath(a, REPO_ROOT), '→', os.path.relpath(b, REPO_ROOT))


if __name__ == '__main__':
    main()
