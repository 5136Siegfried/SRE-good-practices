# ✅ Philosophie de l'approche CI/CD

Voir le fichier [ci.yml](https://github.com/5136Siegfried/SRE-good-practices/blob/main/.github/workflows/ci.yml).


## 🚀 Le rôle de la CI/CD en SRE

Le pipeline CI/CD (Continuous Integration / Continuous Delivery) n’est pas un outil secondaire : c’est **le point d’entrée vers la fiabilité**. Il représente le premier maillon de la chaîne SRE.

Dans une approche SRE, la CI/CD permet de :
- Vérifier la **qualité du code** dès son intégration
- Automatiser la **validation de l’infrastructure** (IaC)
- Appliquer les **tests de sécurité en amont** (DevSecOps)
- Réduire le **toil** en livrant plus souvent avec moins de risques

> « Ce n’est pas le déploiement du vendredi qui est risqué, c’est de ne pas savoir ce qu’il va faire et si on peut l'annuler. »

---

## ✅ Ce qu’on valide en premier : qualité et sécurité

Une bonne CI commence petit mais solide :

### Lint & format
- YAML (`yamllint`), Shell (`shellcheck`), Python (`ruff`)…
- Terraform : `terraform fmt -check` + `validate`

### Sécurité (DevSecOps)
- Scan de vulnérabilités (`trivy`, `tfsec`, `checkov`)
- Analyse des dépendances (`pip-audit`, `npm audit`, etc.)
- Secrets exposés (`gitleaks`, `detect-secrets`)

### Tests automatisés
- Unitaires sur les scripts critiques
- Test de syntaxe/plan sur les modules Terraform

---

## 🔁 Ce qu’on automatise ensuite

- **Build & push d’artefacts** : conteneurs, fichiers `.tfstate`, templates
- **Validation de déploiement** : staging > prod via environnements GitHub Actions ou GitOps (FluxCD/ArgoCD)
- **Notification d’incidents** : alertes en cas d’échec critique
- **Mise à jour auto de documentation technique**

> Le pipeline devient un agent actif de la fiabilité.

---

## 🔐 CI comme rempart de sécurité (DevSecOps)

L'intégration continue est aussi un point de **surveillance sécurité** :

- Vérifie que les **politiques sont respectées** (ex : tag obligatoire, image from scratch…)
- Bloque les **patterns dangereux connus**
- Empêche le **shadow IT** (déploiement sauvage hors pipeline, on vous voit les PR sur les IAM au milieu d'un chore: typo )
- Documente les **actions humaines** (audit trail complet)

---

## 📏 CI/CD & Scalabilité

Un pipeline bien conçu est :
- **Modulaire** (jobs indépendants, workflows réutilisables)
- **Paramétrable** (par branches, env, secrets…)
- **Décentralisable** (chaque équipe peut l’étendre)
- **Observable** (logs, alertes, durées, ratios d’échec)

---

## 🧠 Astuce SRE senior

- Documente tes workflows : qui déclenche quoi, sous quelle condition ?
- Ajoute des alertes en cas d’**absence de déploiement** (symptôme de bug silencieux)
- Crée une **politique de merge** claire (tests obligatoires ? review obligatoire ?)
- Ajoute une **vérification de commit convention** (conventional commits)
- pense à activer un mode maintenance dans ta CI pour les changements majeurs.

---

## 🧩 Exemple de stack CI DevSecOps

| Étape         | Outil(s) recommandés                |
|---------------|-------------------------------------|
| Lint & format | yamllint, shellcheck, ruff          |
| IaC check     | terraform fmt/validate, tflint      |
| Sécurité      | trivy, tfsec, gitleaks              |
| Tests         | pytest, bats, terratest             |
| CI engine     | GitHub Actions, GitLab CI, CircleCI |
| Notifications | Slack, Discord, Opsgenie            |

---

> « Une bonne CI/CD ne ralentit pas les devs. Elle leur évite d’appuyer sur un bouton rouge par erreur. »
