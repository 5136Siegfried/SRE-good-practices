L’astreinte est un **système vivant** qui touche à la fois l’humain, le technique, l’organisationnel et le contractuel.

---

## 🔧 **1. Technique**
### 📦 Mise en œuvre
- [x] Schéma de rotation
- [ ] Checklist d’astreinte (outils, accès, vérifs à faire en début de garde)
- [ ] Runbooks d'urgence (actions rapides : redémarrage, scale, purge, etc.)
- [ ] Escalade automatisée (via Opsgenie, Alertmanager, etc.)
- [ ] Détection & déclenchement (qui alerte ? comment ? sur quoi ?)

### 💾 Préparation de la base
- [ ] Procédure de **snapshot/sauvegarde rapide**
- [ ] Accès à un environnement de **dégradé / fallback**
- [ ] Scripts d’init système à distance (ex : `terraform apply -target`, restart K8s, etc.)

---

## 🧑‍🤝‍🧑 **2. Humain & Organisation**
- [ ] Définition des rôles : on-call, backup, escalation manager
- [ ] Planification long terme (éviter les astreintes abusives ou non anticipées)
- [ ] Politique de récupération (jour off, primes, rotations douces)
- [ ] Formation à l’astreinte : onboarding on-call (technique + éthique)
- [ ] Gestion de la fatigue, burn-out et droit à la déconnexion
- [ ] Communication inter-équipes (dev, ops, produit, support)

---

## 🧠 **3. Culture & Vision**
- [x] Philosophie de l’astreinte (déjà rédigée)
- [ ] Astreinte comme outil d’apprentissage (postmortem systématique)
- [ ] Mise en valeur des actions on-call dans la carrière (feedback, reconnaissance)
- [ ] Astreinte “évolutive” : chaque incident rend l’infra plus résiliente
- [ ] Réduction progressive du besoin d’astreinte (automatisation, SLO…)

---

## 🔐 **4. Sécurité & Fiabilité**
- [ ] Accès restreints temporisés (vault, sudoers, bastions)
- [ ] Audit log des actions on-call
- [ ] Journal de décision (wiki ou doc de ce qui a été fait et pourquoi)
- [ ] Checklist de sécurité avant fin d’astreinte

---

## 📚 **5. Documentation à produire**
| Type | Description |
|------|-------------|
| `oncall-checklist.md` | Ce que doit faire un on-call en début et fin de garde |
| `runbooks/*.md` | Procédures spécifiques (reboot service X, failover DB, etc.) |
| `handoff-template.md` | Trame de passation de garde |
| `oncall-tooling.md` | Outils recommandés (CLI, dashboards, bots, alerting, etc.) |
| `oncall-fatigue.md` | Précautions, bonnes pratiques, droit à la déconnexion |

---
