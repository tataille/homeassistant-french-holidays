# Notes de version — French Holidays v0.1.3

> Brouillon à utiliser lors de la prochaine release. La version publiée reste **0.1.2** tant que la release v0.1.3 n’a pas été créée.

## Améliorations

- Traduit les régions proposées dans le formulaire selon la langue de Home Assistant.
- Affiche un titre français pour l’étape de configuration et des noms de région lisibles pour les nouvelles entrées.
- Documente les deux compteurs avant les vacances scolaires et l’unité `d` (« jour ») affichée par Home Assistant.

## Vérification

- Ajoute un test qui vérifie que les deux compteurs indiquent 10 jours avant les vacances scolaires dans le scénario couvert.

## Mise à jour

Installez la mise à jour depuis HACS ou remplacez le dossier `custom_components/french_holidays`, puis redémarrez Home Assistant. Conservez l’entrée de configuration existante.
