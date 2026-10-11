# Titre du sujet HACF

French Holidays : jours fériés et vacances scolaires dans Home Assistant

# Message prêt à publier

Bonjour à tous,

Je viens de publier **French Holidays**, une intégration native Home Assistant issue du portage de mon module **node-red-french-holidays**.

L’idée : adapter facilement vos automatisations aux jours fériés et aux vacances scolaires, directement depuis Home Assistant.

Vous choisissez votre **académie** pour les vacances scolaires et votre **région** pour les jours fériés. Ces deux choix sont indépendants. L’intégration fournit **23 entités** avec des noms en français, notamment :

- jour férié aujourd’hui et demain ;
- prochain jour férié et sa date ;
- vacances scolaires en cours et date de fin ;
- prochaines vacances, dates et compte à rebours ;
- week-end et jour ouvré.

Elle se configure depuis l’interface et fonctionne **sans Node-RED ni MQTT**. Les calendriers proviennent des sources officielles et sont conservés dans un cache persistant après un premier chargement réussi.

Deux exemples concrets sont disponibles : [notification de réveil les jours ouvrés hors vacances scolaires et chauffage adapté aux vacances](https://github.com/tataille/homeassistant-french-holidays/blob/main/docs/AUTOMATIONS.md).

**Installation manuelle, sans HACS**

Prérequis : Home Assistant **2026.1 ou plus récent**.

1. Téléchargez [le ZIP de la version 0.1.2](https://github.com/tataille/homeassistant-french-holidays/releases/download/v0.1.2/homeassistant-french-holidays-v0.1.2.zip).
2. Décompressez l’archive et copiez `custom_components/french_holidays` dans le dossier `custom_components` de votre configuration.
3. Vérifiez le chemin `/config/custom_components/french_holidays/manifest.json`.
4. Redémarrez Home Assistant.
5. Dans **Paramètres → Appareils et services → Ajouter une intégration**, recherchez **French Holidays**.

Pour Home Assistant Docker, utilisez le dossier de l’hôte monté sur `/config`.

L’installation via HACS comme dépôt personnalisé est également possible : ajoutez `https://github.com/tataille/homeassistant-french-holidays` avec le type **Intégration**. [La demande d’ajout au catalogue HACS est en attente d’examen](https://github.com/hacs/default/pull/11829).

**Quelques précisions**

Les dates scolaires sont actuellement interprétées en Europe/Paris. Nantes est la configuration testée ; des retours sur les autres académies, notamment ultramarines, seront utiles. Les jours fériés sont sélectionnés indépendamment selon la région. Une migration depuis les capteurs MQTT du module Node-RED demande d’adapter les références aux nouvelles entités.

[Projet et documentation](https://github.com/tataille/homeassistant-french-holidays) · [Signaler un problème](https://github.com/tataille/homeassistant-french-holidays/issues)

Si vous l’essayez, je suis intéressé par vos retours sur votre académie, votre région et vos usages en automatisation. En cas de problème, précisez les versions de Home Assistant et de l’intégration.

Merci !

---

Avant publication : joindre une **vraie capture de votre tableau de bord**, en masquant les informations personnelles. Cette dernière note est destinée à l’auteur et ne fait pas partie du message à publier.
