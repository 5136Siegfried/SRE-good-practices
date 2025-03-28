# 📏 SLI, SLO et Budget d'erreur : piloter la fiabilité

Le cœur du métier SRE n’est pas de viser une fiabilité parfaite, mais de **piloter la fiabilité avec lucidité**.

Pour cela, on utilise trois concepts clés :

- **SLI** (Service Level Indicator) : une métrique mesurable de la qualité de service
- **SLO** (Service Level Objective) : un objectif sur ce SLI
- **Budget d'erreur** : la marge acceptable de défaillance

---

## 📊 1. Qu’est-ce qu’un SLI ?

> "On ne peut pas gérer ce qu’on ne mesure pas."

Un **SLI** est un indicateur mesurable, calculé objectivement sur une période donnée.

### Exemples de SLI :
- **Disponibilité** d’un service (requêtes 200 / total)
- **Latence** sous 300 ms (pour X% des requêtes)
- **Taux d’erreurs** (4xx/5xx)
- **Fraîcheur des données** (temps depuis dernière sync réussie)

Un bon SLI est **pertinent pour l’utilisateur final**, pas seulement pour les ops.

---

## 🎯 2. Qu’est-ce qu’un SLO ?

Un **SLO** est une **cible contractuelle interne** sur une métrique SLI. Il permet de fixer un niveau de qualité **souhaité mais atteignable**.

### Exemples de SLO :
- 99.9% des requêtes HTTP doivent retourner un 200 en <300ms
- 99.95% de disponibilité du service frontend sur 30 jours
- Moins de 0.1% d’échec de job CI/CD sur 7 jours

> L’objectif n’est pas la perfection, mais une **zone de confort maîtrisée**.

---

## 🔥 3. Le Budget d’erreur

> "Un service peut échouer — s’il sait à quel point."

Le **budget d’erreur** est ce qu’il reste **entre le SLO et 100%**.

### Exemples :
- SLO : 99.9% → budget d’erreur = 0.1% → soit ~43 minutes/mois
- SLO : 99.99% → budget d’erreur = 0.01% → soit ~4 minutes/mois

### Pourquoi c’est clé :
- Si tu **dépasses ton budget**, tu **gèles les déploiements** pour stabiliser
- Si tu **es largement sous ton budget**, tu **peux prendre plus de risques** (features, refacto, etc.)

C’est un **levier de pilotage entre l’innovation et la stabilité**.

---

## 🛠️ Implémenter SLO et SLI

### En pratique :
- Tu définis un SLI (requêtes 2xx, latence…)
- Tu fixes un SLO (ex : 99.9% sur 30 jours)
- Tu monitors via Prometheus, Datadog, Sentry…
- Tu exposes l'état du SLO dans un dashboard
- Tu déclenches une alerte **si le budget d'erreur est consommé trop vite**

> 🔍 Un bon alerting ne dit pas "tout va mal" mais "on ne tiendra pas notre promesse".

---

## 📚 Bonnes pratiques

- 🚦 SLO != SLA : l’un est interne, l’autre contractuel
- 🎯 Ne vise pas trop haut au début : 99.9% est déjà exigeant
- 🧠 Implique produit & dev dans la définition des SLO (partagés)
- 📉 Révise tes SLO régulièrement (équipe, tech, usage changent)
- 🧭 Expose les SLO dans des dashboards lisibles par tous

---

## 🧠 En résumé

```
[SLI] = une mesure (latence, erreurs...)
[SLO] = un objectif (99.9%)
[Budget] = la tolérance d'échec restante
```

C’est **le GPS de la fiabilité** : il ne garantit pas que tu ne te perdras jamais, mais il te dit **quand tu t’éloignes trop de la route.**
