# ✅ Checklist d'Astreinte On-Call

Ce document sert de référence opérationnelle pour toute personne prenant une garde d’astreinte. Il vise à garantir une prise de poste efficace, une réponse rapide aux incidents, et une passation claire. Cette checklist doit être suivie **à chaque début et fin de garde**, et sert également de trace en cas d'incident majeur.

---

## 🕘 Avant la prise de garde

### 🔐 Accès & Préparation
- [ ] Accès VPN/bastion fonctionnel ✅ Testé manuellement
- [ ] Accès aux consoles cloud / outils internes (Kubernetes, CI/CD, monitoring...) ✅ Vérifié avec un collègue si doute
- [ ] Accès à Opsgenie (ou autre outil d'alerte) validé ✅ Notifications push activées
- [ ] Vérification des droits nécessaires (read/write sur les environnements concernés) ✅ Essai sur une ressource test
- [ ] Connexion testée aux outils CLI (`kubectl`, `terraform`, `vault`, `gh`, etc.) ✅ Contexte à jour et authentification OK

### 🧰 Environnement local prêt
- [ ] Terminal configuré (alias, contexte K8s, profils cloud)
- [ ] Dashboards Grafana ouverts en favoris (infrastructure, app critique, DB, etc.)
- [ ] Runbooks accessibles (via Notion, Confluence ou repo cloné localement)
- [ ] Bloc-notes / markdown pour journaliser chaque action pendant la garde

### 🤝 Handoff avec l'on-call précédent
- [ ] Points chauds ou incidents en cours notés dans le journal
- [ ] Déploiements prévus, maintenances planifiées ou événements sensibles mentionnés
- [ ] Alertes récurrentes ou flaky connues (ex : CPU spike nocturne sur pod X)
- [ ] Vérification du statut du dernier incident clos (correctif validé ou non)

---

## 🚨 En cas d'incident

### 🔍 Réaction immédiate
- [ ] Identifier la sévérité (S1 : critique, S2 : impact utilisateur, S3 : bruit)
- [ ] Vérifier que l’alerte est légitime (bruit, duplication, ou réel problème)
- [ ] Se connecter à l'environnement concerné (cluster, VM, pipeline, etc.)
- [ ] Suivre les runbooks dès que possible (ne pas improviser sans trace)
- [ ] Éviter tout changement irréversible sans appel à un collègue si possible

### 💬 Communication
- [ ] Annoncer l’incident dans le canal dédié #incident-active (Slack, Teams…)
- [ ] Utiliser la structure "QUI / QUOI / QUAND / PROCHAIN PAS"
- [ ] Taguer le rôle d’escalade ou le secondary-oncall si besoin
- [ ] Mettre à jour un thread d’incident avec les timestamps, actions et rollback éventuel

### 🧩 Action
- [ ] Stabiliser le système (relancer, redémarrer, isoler le problème)
- [ ] Réduire l’impact utilisateur (désactivation temporaire de feature, trafic coupé vers un pod, etc.)
- [ ] Restaurer les services critiques (base de données, API principales, CI/CD)
- [ ] Déclencher un fallback si nécessaire (système de secours, replica, cache…)

---

## 🧾 Fin de garde

### 📝 Journal de garde
- [ ] Récapitulatif des incidents rencontrés (même mineurs)
- [ ] Actions réalisées + liens vers logs / commits / tickets JIRA/GitHub
- [ ] Difficultés techniques rencontrées (même si résolues à chaud)
- [ ] Retour subjectif : fatigue, charge, suggestions d’amélioration

### 📤 Handoff vers le prochain on-call
- [ ] Problèmes non résolus clairement identifiés et escaladés
- [ ] Runbooks à mettre à jour signalés (et créés si besoin)
- [ ] Suggestions d’automatisation ou d’alerte à optimiser listées
- [ ] Copie du journal envoyée à l’équipe SRE ou sauvegardée dans l’espace dédié

---

## 🧠 Rappel : l’astreinte est une mission de soin
Ce que tu fais ici a de l’impact. Tu protèges la continuité d’un système vivant.
Tu n’es pas seul.e. Tu n’as pas à tout réparer. Mais tu es le premier bouclier.

> “Stabilise. Informe. Transmets.”

---

## 📌 Ressources utiles (à adapter selon ton contexte)

- Runbooks : `docs/runbooks/`
- Accès rapide Grafana : `https://grafana.example.com`
- Portail Opsgenie : `https://app.opsgenie.com/`
- Bastion SSH : `bastion.company.net`
- Journal de garde modèle : `templates/oncall-log.md`
- Escalade manager : `+33 6 xx xx xx xx` / `escalade@example.com`

---

> Cette checklist est évolutive. Si une étape manque ou peut être améliorée, propose un patch ou une issue.