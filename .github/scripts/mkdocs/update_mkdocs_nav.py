import os
import yaml

MKDOCS_YML = "mkdocs.yml"
DOCS_DIR = "docs"

EXCLUDE = {"index.md"}

def collect_docs():
    result = []
    for root, _, files in os.walk(DOCS_DIR):
        md_files = [f for f in files if f.endswith(".md") and f not in EXCLUDE]
        for f in md_files:
            path = os.path.join(root, f)
            rel_path = os.path.relpath(path, DOCS_DIR)
            display = rel_path.replace(".md", "").replace("_", " ").title()
            parts = rel_path.split(os.sep)

            if len(parts) == 1:
                result.append({display: rel_path})
            else:
                folder = parts[0].title()
                entry = {parts[-1].replace(".md", "").replace("_", " ").title(): rel_path}
                existing = next((item for item in result if isinstance(item, dict) and folder in item), None)
                if existing:
                    existing[folder].append(entry)
                else:
                    result.append({folder: [entry]})
    return result

def update_mkdocs_nav():
    with open(MKDOCS_YML, 'r') as f:
        config = yaml.safe_load(f)

    new_nav = [{"Accueil": "index.md"}] + collect_docs()
    config['nav'] = new_nav

    with open(MKDOCS_YML, 'w') as f:
        yaml.dump(config, f, allow_unicode=True, sort_keys=False)

    print("✅ mkdocs.yml updated with new navigation")

if __name__ == "__main__":
    update_mkdocs_nav()
