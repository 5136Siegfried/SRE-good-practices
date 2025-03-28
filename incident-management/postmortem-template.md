🩻 Template de Postmortem (Blameless)
=====================================

Un postmortem doit permettre de comprendre, d'apprendre, et d'améliorer les systèmes --- sans chercher de coupable.

Ce modèle suit une approche "blameless", rigoureuse et actionnable.

* * * * *

📌 Contexte
-----------

-   **Titre de l'incident :**
-   **ID de l'incident (facultatif) :**
-   **Date & heure (début - fin) :**
-   **Durée totale de l'impact :**
-   **Responsable de la rédaction :**
-   **Participants à la résolution :**

* * * * *

📉 Impact
---------

-   **Services affectés :**
-   **Utilisateurs impactés :**
-   **Description de l'impact (fonctionnel, technique, business) :**
-   **Gravité (S1/S2/S3...) :**

* * * * *

🕰️ Timeline détaillée
----------------------

| Heure | Événement |
| --- | --- |
| HH:MM | Détection de l'incident |
| HH:MM | Début de l'investigation |
| HH:MM | Hypothèse posée / Action testée |
| HH:MM | Identification de la cause |
| HH:MM | Déploiement du correctif |
| HH:MM | Retour à la normale |

* * * * *

🔍 Causes racines (RCA)
-----------------------

-   **Cause technique :**
-   **Défaut de détection / monitoring ?**
-   **Processus ou communication contributifs ?**
-   **Dette technique ou faiblesse connue ?**

* * * * *

🛠️ Actions correctives
-----------------------

### Immédiates (hotfix)

-   [ ]  Description de l'action 1
-   [ ]  Description de l'action 2

### Préventives (long terme)

-   [ ]  Ajout de tests / validations
-   [ ]  Amélioration du monitoring / alerting
-   [ ]  Documentation / runbook à créer
-   [ ]  Revue d'architecture ou post-déploiement

* * * * *

💬 Retours & enseignements
--------------------------

-   Ce qui a bien fonctionné :
    -   ...
-   Ce qui aurait pu mieux se passer :
    -   ...
-   Frictions organisationnelles ou techniques :
    -   ...
-   Idées pour fluidifier l'incident next time :
    -   ...

* * * * *

✅ Validation & suivi
--------------------

-   [ ]  Postmortem relu et validé par l'équipe SRE
-   [ ]  Actions suivies et assignées dans le backlog
-   [ ]  Ajout à la base de connaissance / documentation

* * * * *

> *"Les erreurs sont inévitables. Apprendre et s'améliorer est un choix."*