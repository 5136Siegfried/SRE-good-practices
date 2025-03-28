# ✅ Philosophie de l'approche CI/CD

Voir le fichier [ci.yml](https://github.com/5136Siegfried/SRE-good-practices/blob/main/.github/workflows/ci.yml).


## Objectif

La mise en place d'un pipeline CI est une pratique fondamentale en SRE et DevSecOps. Elle permet de garantir que tout changement dans le code est **testé, analysé et validé automatiquement**, réduisant les risques d'incidents en production. L'approche ici présentée vise à poser une base saine, modulaire et sécurisée pour tout projet SRE.

---

## Structure du pipeline

Ce pipeline est divisé en trois blocs clés, exécutés à chaque `push` ou `pull_request` sur la branche `main` :

### 1. **Lint & Validation**
- Lint YAML (via `yamllint`) pour garantir une syntaxe propre sur la configuration et la documentation.
- Lint des scripts Shell (via `shellcheck`) pour assurer la portabilité, la lisibilité et l'évitement des erreurs classiques.

**Pourquoi ?**
> Un code propre est un code sûr. Ces outils permettent de détecter des erreurs silencieuses avant même les tests.

### 2. **Validation Terraform**
- Initialisation du projet
- Vérification du formatage (`fmt -check`)
- Validation syntaxique (`terraform validate`)

**Pourquoi ?**
> L'infrastructure-as-code doit être traitée avec le même niveau d'exigence que le code applicatif. Cette étape garantit que les fichiers sont valides avant tout plan ou déploiement.

### 3. **Scan de sécurité (Trivy)**
- Analyse des vulnérabilités critiques et hautes sévérités dans le code et les dépendances.

**Pourquoi ?**
> Intégrer la sécurité dès le développement, c'est le principe même du DevSecOps. Trivy permet une analyse rapide, non intrusive, et efficace.

---

## Philosophie : CI comme premier rempart de fiabilité

- ❄️ **Simplicité lisible** : le pipeline est clair, modulaire, facilement extensible.
- 🔌 **Automatisé mais explicite** : chaque étape peut être comprise et relancée individuellement.
- 🛡️ **Culture DevSecOps** : lint, tests et sécurité sont traités ensemble, sans sacrifier la qualité.
- ✅ **Adaptable à tout stack** : Python, Shell, Terraform sont supportés ici, mais le modèle est ouvert à d'autres technos (Go, Node, Ansible, Docker, etc.)

---

## Prochaines évolutions possibles

- Ajout de tests unitaires pour scripts Python/Bash
- Ajout de `tflint`, `checkov`, `tfsec` pour renforcer les vérifications IaC
- Intégration d'un cache pour accélérer les workflows
- Envoi des résultats sur Slack/Discord en cas d'échec

---

> Cette première CI constitue le socle de qualité logicielle sur lequel le reste du projet peut s'appuyer, à la manière des tests unitaires pour un code applicatif.