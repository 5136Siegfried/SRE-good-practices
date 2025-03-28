# 🔄 Cycle de vie d’un incident SRE

Comprendre le **cycle de vie d’un incident** est essentiel pour structurer la réponse, éviter le chaos, et transformer l’erreur en apprentissage durable.

Ce cycle formalise les étapes depuis **la détection** jusqu’à **la capitalisation**. Chaque étape peut être outillée et suivie par l’équipe SRE.

---

## ⛳ 1. Détection

> "Tu ne peux pas résoudre ce que tu ne vois pas."

### Sources de détection :
- Monitoring (Prometheus, Datadog…)
- Alertes automatisées (Opsgenie, Alertmanager)
- Signalement humain (support, dev, client…)
- Checklists manuelles (revue hebdo, métriques seuils)

### Objectifs :
- Réduire le **Time To Detect (TTD)**
- Éviter les faux positifs / alert fatigue

---

## 🚨 2. Qualification

### Sévérité à définir :
| Niveau | Impact | Exemples |
|--------|--------|----------|
| S1     | Incident critique (prod KO) | API down, perte de données, failover KO |
| S2     | Incident majeur             | Latence élevée, CI/CD bloqué, service partiel |
| S3     | Incident mineur             | Bruit, lenteur ponctuelle, bug UX |

### Action :
- Valider que l’alerte est légitime
- Classer l’incident pour activer le bon protocole (astreinte, war room…)

---

## 🧑‍💻 3. Réponse active

### Objectifs :
- **Stabiliser la situation** rapidement
- **PROTEGER LA DONNEE**
- **Informer les parties concernées** (canal incident Slack, tableau statut public…)
- **Documenter les actions** dès le début (même si elles échouent)

### Responsables :
- On-call SRE / équipe produit
- Escalade si nécessaire

> "Ne pas comprendre n’empêche pas d’agir. Mais chaque action doit être traçable."

---

## 🧩 4. Résolution technique

### Méthodes :
- Application d’un correctif (hotfix, rollback, scale, reboot…)
- Rétablissement d’un service (failover, reroute, bypass…)
- Vérification du retour à la normale (métriques, logs, retours clients…)

### But :
- **Restaurer un état stable**, même si temporaire ou dégradé
- **Minimiser l’impact global**

---

## 📘 5. Postmortem (à froid)

### Structure :
- Timeline précise
- Causes racines (techniques, humaines, organisationnelles)
- Actions correctives (immédiates et préventives)
- Enseignements et suggestions

> "Pas de blâme. Pas de mystère. Pas d’oubli."

### Objectifs :
- Partager l’expérience à l’équipe
- Mettre à jour les runbooks, checklists, alertes
- Aligner les priorités tech avec les réalités terrain

---

## 📚 6. Capitalisation

Un incident n’est clos que s’il a **fait progresser la fiabilité** du système :

- Mise à jour de la documentation (runbook, checklists, infra)
- Actions correctives intégrées dans le backlog / sprint
- Suivi d'exécution des tâches post-incident
- Communication transverse (newsletter interne, formation, démo)

> "Chaque incident est une formation qui coûte cher. Autant l'utiliser."

---

## 🧠 Synthèse visuelle (simplifiée)

```
[Détection] → [Qualification] → [Réponse] → [Résolution] → [Postmortem] → [Capitalisation]
```

flowchart LR
    A[Détection] --> B[Qualification]
    B --> C[Réponse active]
    C --> D[Résolution technique]
    D --> E[Postmortem]
    E --> F[Capitalisation]
    F --> G[Prévention future]


Chaque étape est une opportunité : de réaction, de communication, de compréhension et de transformation durable.
