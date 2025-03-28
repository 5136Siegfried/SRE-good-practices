import os

structure = {
    "sre/ci.md": "# 📦 Philosophie CI/CD\n\nÀ compléter.",
    "sre/oncall.md": "# 🚨 Astreinte : fonctionnement\n\nÀ compléter.",
    "sre/oncall-checklist.md": "# ✅ Checklist d'astreinte on-call\n\nÀ compléter.",
    "sre/postmortem.md": "# 🩺 Postmortem blameless\n\nÀ compléter.",
    "devsecops/security-pipeline.md": "# 🔐 Sécurité des pipelines CI/CD\n\nÀ compléter.",
    "devsecops/secrets.md": "# 🔐 Gestion des secrets et accès\n\nÀ compléter.",
    "infra/terraform-modules.md": "# 🏗️ Modules Terraform\n\nÀ compléter.",
    "infra/ansible.md": "# ⚙️ Automatisation avec Ansible\n\nÀ compléter.",
    "observability/prometheus.md": "# 📈 Prometheus et alerting\n\nÀ compléter.",
    "observability/grafana.md": "# 📊 Dashboards Grafana\n\nÀ compléter.",
    "contribute.md": "# 🤝 Contribuer au projet\n\nÀ compléter.",
    "team.md": "# 👤 À propos / Auteur\n\nÀ compléter.",
    "index.md": "# 🌐 Good Practices SRE & DevSecOps\n\nBienvenue dans la documentation vivante.\n\nÀ compléter."
}

base_path = "docs"

for path, content in structure.items():
    full_path = os.path.join(base_path, path)
    os.makedirs(os.path.dirname(full_path), exist_ok=True)
    if not os.path.exists(full_path):
        with open(full_path, "w") as f:
            f.write(content)
        print(f"✅ Créé : {full_path}")
    else:
        print(f"⏩ Déjà présent : {full_path}")
