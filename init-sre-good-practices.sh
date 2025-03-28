#!/bin/bash

echo "📁 Création de l'arborescence du projet SRE/DevSecOps..."

mkdir -p \
  infra/terraform/example-setup \
  infra/ansible/playbooks \
  observability/grafana-dashboards \
  observability/prometheus \
  observability/loki \
  incident-management \
  security \
  tools/scripts \
  docs/architecture \
  .github/workflows

# Fichiers README pour chaque dossier
touch \
  infra/README.md \
  observability/README.md \
  incident-management/README.md \
  security/README.md \
  tools/README.md \
  docs/README.md

# Fichier example init
echo "# Exemple de module Terraform" > infra/terraform/example-setup/main.tf
echo "# Exemple de playbook Ansible" > infra/ansible/playbooks/hardening.yml
echo "# Exemple de dashboard Grafana" > observability/grafana-dashboards/README.md
echo "# Exemples de règles Prometheus" > observability/prometheus/rules.yml
echo "# Exemple de pipeline CI/CD" > .github/workflows/ci.yml
echo "# Template de postmortem" > incident-management/postmortem-template.md
echo "# Bonnes pratiques CI/CD sécurisées" > security/ci-cd-hardening.md
echo "# Script de nettoyage de ressources" > tools/scripts/cleanup-old-resources.sh
echo "# Documentation d'architecture" > docs/architecture/overview.md

echo "✅ Structure de base créée avec succès."
