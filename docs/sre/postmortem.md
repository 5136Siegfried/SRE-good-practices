# 🩺 Philosophie du Postmortem Blameless

Un postmortem n'est ni un rapport d'accusation, ni un simple journal d'incident. C’est un **outil d’apprentissage collectif**, qui transforme un échec en levier d’amélioration. La culture SRE impose une approche **blameless** (sans blâme), rigoureuse, et tournée vers le progrès.

---

## 🧭 Pourquoi faire un postmortem ?

- Pour **analyser à froid** un événement critique (incident, failover, perte de données…)
- Pour **mettre à plat la réalité** du déroulement, sans interprétation émotionnelle
- Pour **identifier les causes profondes**, humaines, techniques et organisationnelles
- Pour **proposer des actions correctives** concrètes, suivies et mesurables
- Pour **renforcer la culture de fiabilité**, la documentation et les processus d’astreinte

---

## 🚫 Blameless, toujours

Un postmortem n’est **jamais un blâme individuel**. Au contraire, il repose sur le postulat :

> "Chaque personne impliquée a agi du mieux qu’elle pouvait avec les informations et les moyens dont elle disposait."

Trahir ce postulat c'est inclure des biais empechant l'évolution saine de l'équipe et de l'infra.

Il permet de **comprendre le contexte** des erreurs, de les replacer dans la chaîne systémique, et de **corriger les causes racines**, pas les humains.

---

## 📐 Structure type

Un bon postmortem suit une structure claire :

1. **Contexte et impact** : Qui a été affecté ? Quels services ? Quelle criticité ?
2. **Timeline précise** : Minute par minute, ce qui s’est passé, sans jugement
3. **Analyse des causes profondes** : Technique, monitoring, communication, dette…
4. **Actions correctives** : Court terme (hotfix) + Long terme (processus, code, infra)
5. **Enseignements** : Ce qui a bien fonctionné, ce qui a manqué
6. **Suivi** : Qui fait quoi ? Quand ? Comment on s'assure que ça ne se reproduira pas

---

## 📘 Bénéfices à long terme

- **Fiabilité accrue** : Chaque incident améliore l’infrastructure ou les alertes
- **Transparence et confiance** : On apprend à dire la vérité, même quand ça va mal
- **Capitalisation** : On crée une base de connaissances collective et utile
- **Culture positive** : On valorise l’apprentissage, pas la peur de se tromper

---

## 🧠 Astuce SRE senior

- Réalise toujours un postmortem pour un S1 ou un incident public
- N’attends pas plus de 72h après l’incident : à chaud mais lucide
- Invite toute l’équipe concernée : produit, ops, dev, comm…
- Publie-le (en interne ou externe) pour nourrir la culture de transparence

---

> *Un bon postmortem ne ferme pas un incident : il ouvre une opportunité d’amélioration continue.*