# 💡 Good Practices – SRE & DevSecOps

![MkDocs](https://img.shields.io/badge/docs-built%20with%20MkDocs-blue.svg)
![Material for MkDocs](https://img.shields.io/badge/theme-Material%20for%20MkDocs-4caabc?logo=material-design)
![License](https://img.shields.io/github/license/5136Siegfried/sre-good-practices)
[![CI Status](https://github.com/5136Siegfried/sre-good-practices/actions/workflows/ci.yml/badge.svg)](https://github.com/5136Siegfried/sre-good-practices/actions/workflows/ci.yml)
[![Deploy-docs](https://github.com/5136Siegfried/sre-good-practices/actions/workflows/deploy.yml/badge.svg)](https://github.com/5136Siegfried/sre-good-practices/actions/workflows/deploy.yml)
[![Documentation](https://img.shields.io/badge/Docs-View%20Online-0a9396.svg)](https://5136Siegfried.github.io/sre-good-practices/)


> Une vitrine de mes compétences, convictions et bonnes pratiques en ingénierie de fiabilité et sécurité cloud.

## 👋 Présentation

Bienvenue ! Je m'appelle **Siegfried Sekkai**, ingénieur Cloud & DevSecOps, passionné par la fiabilité, l'observabilité, l'automatisation et la sécurité. Après un parcours de 8 ans dans l'informatique allant de l'intégration à des missions d'infra Cloud pour de grand compte en passant par de l'expat dans l'industrie auto allemande (QA) et une plongée dans l'entreprenariat IA, Educational Tech, l'e-commerce durable et l'associatif bordelais, je résume ici quelques enseignements et bonnes pratiques.
Etant en parallèle dans le secourisme (Protecion Civile, CSOR, Réserviste, acteur politique des Solidarités) et l'ingénieurie pédagogique, je propose cette vitrine de bonnes pratiques pour renforcer notre culture du risque.
Ce dépôt est à la fois un **starter kit** et un **guide de bonnes pratiques** couvrant l'ensemble du cycle de vie SRE.

## 🎯 Objectifs

- Centraliser des **bonnes pratiques** éprouvées dans l’écosystème Cloud / DevOps / SRE.
- Fournir des **exemples concrets** (infra, monitoring, sécurité, incident response…).
- Démontrer une **culture de la fiabilité, du pragmatisme et de la documentation**.
- Partager une vision DevSecOps **centrée sur l’impact, l'agilité,la scalabilité et l’humain.**

---

## 🧭 Arborescence

| Dossier                | Contenu |
|------------------------|---------|
| `infra/`               | Exemples d'infrastructure as code (Terraform, Ansible…) |
| `observability/`       | Dashboards Grafana, config Prometheus, logs, alerting |
| `incident-management/` | Méthodes de gestion d'incidents, postmortems, runbooks |
| `security/`            | Gestion des secrets, CI/CD sécurisée, threat modeling |
| `tools/`               | Scripts et helpers utiles (bash, Python…) |
| `docs/`                | Architecture, principes SRE, documentation technique |

---
✅ Déploiement sur GitHub Pages (Checklist)
Étape	Description	Statut
🔧 1. Type de site	Site statique généré avec MkDocs Material	✅
🗂️ 2. Branche de déploiement	gh-pages doit être configurée comme source dans Settings > Pages	🔲
🔁 3. Déploiement local	Commande manuelle : mkdocs gh-deploy --clean --force	🔲
⚙️ 4. CI/CD automatique	.github/workflows/deploy.yml configure le déploiement à chaque push sur main	🔲
🌐 5. URL du site	https://5136Siegfried.github.io/sre-good-practices/	🔲
🧼 6. Pas de /docs dans GitHub Pages	Ne pas utiliser /docs comme source (ça affiche les .md bruts)	🔲
🕒 7. Propagation DNS	Après déploiement, attendre jusqu’à 60s avant que le site ne soit servi	🔲
🧪 8. Vérification post-déploiement	Recharger la page avec Ctrl + F5 pour forcer l’actualisation	🔲
🚫 9. Erreur 404 ?	Refaire mkdocs gh-deploy --clean --force puis re-check Settings > Pages	🔲
---

## 🔧 Technologies & Stack

- **Cloud**: AWS, GCP, Azure
- **IaC**: Terraform, Ansible
- **Observabilité**: Prometheus, Grafana, Loki, ELK
- **CI/CD**: GitHub Actions, GitLab CI, ArgoCD
- **Sécurité**: Vault, Trivy, Snyk, OPA, Kyverno
- **Containerisation**: Docker, Kubernetes, Helm

---

## 📘 Philosophie SRE

- _"You build it, you run it"_
- Priorité à l’**automatisation** des tâches récurrentes
- Mesure permanente par des **SLOs réalistes**
- **Postmortems blameless** systématiques
- **Infrastructure modulaire**, versionnée et observable

---

## 🧪 Envie de contribuer ?

Ce repo est avant tout un espace de partage. Si tu veux proposer une bonne pratique, un outil ou une amélioration : **PRs bienvenues !**

---

## 🧠 Ressources à suivre

- [Google SRE Handbook](https://sre.google/books/)
- [Awesome SRE (GitHub)](https://github.com/dastergon/awesome-sre)
- [The Twelve-Factor App](https://12factor.net/)
- [OWASP DevSecOps Guide](https://owasp.org/www-project-devsecops-guideline/)

---

## 📬 Contact

Tu veux discuter d’architecture, d’outillage ou de culture SRE ?
Ping-moi ici ou sur [LinkedIn](https://www.linkedin.com/in/siegfried-sekkai).

---
