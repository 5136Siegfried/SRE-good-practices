# 🚨 Astreinte : fonctionnement

L’astreinte est un pilier central dans l’approche SRE. Elle garantit une couverture humaine en cas d’incident en dehors des heures normales, tout en incarnant la culture de la fiabilité opérationnelle.

---

## 🧭 Objectifs de l’astreinte

- Assurer une **prise en charge rapide** des incidents critiques
- **Réduire le temps de rétablissement** (MTTR)
- **Stabiliser** les systèmes en urgence (runbook, fallback, rollback)
- Transmettre un retour d’expérience exploitable pour l’amélioration continue

---

## 👥 Organisation d’une rotation on-call

| Rôle           | Description                                         |
|----------------|-----------------------------------------------------|
| Primary        | Responsable de la première réponse aux alertes     |
| Secondary      | Prend le relais si le primary ne répond pas        |
| Escalade       | Manager technique ou SRE senior de dernier recours |

### 🗓️ Exemple de rotation (hebdomadaire)
- Lundi 09h → Lundi 09h suivant
- Planning anticipé sur 4 à 8 semaines
- Publication sur calendrier partagé (.ics, Slack, Notion…)

### 🧪 Répartition équitable
- Chaque SRE assure entre **1 et 2 semaines** d’astreinte toutes les 6 à 8 semaines
- Astreinte compensée : prime, récupération, ou temps dédié post-garde

---

## 🛠️ Outils et support

- **Outil de dispatch** : Opsgenie, PagerDuty, VictorOps
- **Monitoring + alerting** : Prometheus, Grafana, Loki, Elastic, Sentry…
- **Runbooks d’intervention rapide**
- **Checklist d’astreinte** (prise de garde, fin de garde)
- **Accès d’urgence** (bastion, VPN, comptes restreints avec délai d’expiration)

---

## ⛑️ Logique de premiers secours

L’objectif n’est pas de tout réparer, mais :
- De **limiter l’impact immédiat** pour les utilisateurs
- D’**identifier la zone de problème** (base, réseau, app, cloud)
- D’**informer** les équipes avec clarté
- D’**agir en sécurité** avec un périmètre défini

> L’astreinte, c’est du secourisme système : protéger, alerter, intervenir.

---

## 🔄 Déroulement d’une alerte

1. 🔔 Alerte déclenchée → système ou utilisateur
2. 📞 Notification vers le primary (call + SMS + push)
3. ⏱️ Si pas de réponse → fallback vers le secondary en < 10 min
4. 🧑‍💼 Si toujours inactif → Escalade
5. 🛠️ Stabilisation du service
6. 📝 Log de l’incident et actions réalisées
7. 🩺 Postmortem dans les 72h (S1/S2)

---

## 📣 Communication et transparence

- Un channel `#incident-active` dédié
- Nommer un **incident commander** si la gravité est élevée
- Journaliser toutes les actions visibles par l’équipe
- Clôturer proprement avec un résumé (impact, cause, correctif, prochaines actions)

---

## 🧠 Enrichissement continu

- Chaque incident nourrit la base de **runbooks**
- Les alertes trop fréquentes → **refactor ou silence raisonné**
- Chaque garde donne lieu à une **rétro rapide** : ce qui a bien/mal fonctionné

---

> L’astreinte n’est pas un fardeau. C’est un contrat de confiance avec les systèmes, l’équipe et les utilisateurs.