# 🚒 Schéma de rotation d'astreinte (On-call Rotation)

Ce fichier présente une proposition de schéma d'astreinte pour une équipe SRE/DevSecOps, inspirée des outils comme **Opsgenie**, **PagerDuty** ou **Incident.io**.

L'objectif est d'assurer une **couverture 24/7** des incidents critiques avec une **charge humaine répartie et supportable**, tout en favorisant le **blameless incident management**.

---

## ⌚ Périmètre de l'astreinte

- **Services couverts :** production, monitoring, alerting, pipeline CI/CD, infrastructure
- **Types d'incidents concernés :** S1 (Critique), S2 (Majeur)
- **Canal d'alerte :** webhook → Opsgenie → appel + SMS + e-mail

---

## 🤜 Modèle de rotation

### 👥 Équipe

- Alice (SRE)
- Bob (DevOps)
- Charlie (Cloud Architect)
- Diane (SecOps)

### ⏳ Fréquence

- **Rythme :** Hebdomadaire
- **Rotation le lundi à 09h00 UTC**
- **Durée de la rotation :** 7 jours pleins
- **Astres appelables :**
  - 1 **Primary on-call**
  - 1 **Secondary on-call** (fallback si pas de réponse dans les 10 minutes)

---

## 📕 Exemple de planning de rotation

| Semaine        | Primary     | Secondary   |
|----------------|-------------|-------------|
| 1 (01/04 - 07/04) | Alice       | Bob         |
| 2 (08/04 - 14/04) | Bob         | Charlie     |
| 3 (15/04 - 21/04) | Charlie     | Diane       |
| 4 (22/04 - 28/04) | Diane       | Alice       |

---

## 🔧 Escalade

1. **Alert déclenchée** (monitoring ou utilisateur)
2. Notification Opsgenie vers **Primary on-call** (Appel + SMS + Email)
3. Si pas de réponse sous 10 minutes → **Secondary on-call** est alerté
4. Si toujours aucune réponse sous 20 minutes → **Escalade manager** est contacté

---

## ✉️ Bonnes pratiques

- Un channel Slack/Teams dédié aux incidents actifs
- Mode "On-call" activé sur les téléphones pros (pas de notifications silencieuses)
- Une **checklist d'astreinte** distribuée à chaque prise de garde
- Un **hand-off meeting** rapide le lundi pour transfert de contexte
- Temps passé en astreinte suivi et compensé (récup, prime ou jour off)

---

## ✨ Vision SRE

> L'astreinte n'est pas un sacrifice, c'est une responsabilité collective organisée. Elle fait partie intégrante de la culture de la fiabilité.

Un bon schéma d'astreinte doit être **prévisible, bien documenté et humainement tenable**.

---

Tu peux automatiser ce roulement via des intégrations Opsgenie/PagerDuty et exporter un calendrier public (.ics) lié aux rotations.