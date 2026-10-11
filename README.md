# French Holidays — v0.1.1

Intégration personnalisée Home Assistant en Python, indépendante de Node-RED.
Configuration proposée : **académie Nantes (zone B)** et **jours fériés Martinique**.
Ces choix sont indépendants : le calendrier scolaire est celui de Nantes, pas celui de Martinique.

## Installation manuelle — Home Assistant Docker

1. Copier le dossier `custom_components/french_holidays` de cette archive dans
   le dossier de configuration Home Assistant : `/config/custom_components/french_holidays`.
   Copier depuis l’hôte dans le répertoire monté sur `/config` du conteneur.
2. Redémarrer Home Assistant (par exemple `docker restart homeassistant`, si c’est le nom du conteneur).
3. Paramètres → Appareils et services → Ajouter une intégration → **French Holidays**.
4. Confirmer **Nantes** et **martinique**, proposés par défaut.

Aucune entrée YAML n’est nécessaire. `examples/configuration.json` décrit les paramètres,
ce n’est pas un fichier à importer dans Home Assistant. Ne pas modifier `.storage` à la main.
Pour changer de combinaison dans cette version, supprimer l’entrée et la recréer.

## HACS

Une fois ce projet publié dans votre dépôt GitHub, l’ajouter comme dépôt personnalisé
HACS de type **Intégration**, installer French Holidays et redémarrer.
Dépôt : `tataille/homeassistant-french-holidays`. Le projet n’est pas référencé
officiellement dans HACS.

## Entités

| Type | Nom |
|---|---|
| binary_sensor | Public holiday |
| binary_sensor | Public holiday tomorrow |
| binary_sensor | School holidays |
| binary_sensor | School holidays tomorrow |
| binary_sensor | Weekend |
| binary_sensor | Working day |
| sensor | Next public holiday |
| sensor | Next public holiday date |
| sensor | Days until school holidays |
| sensor | School holiday name |

Les identifiants réels sont générés par Home Assistant à partir du nom de l’appareil.
Les retrouver dans la fiche de l’intégration avant de les utiliser dans une automatisation.
Le prochain jour férié est strictement après aujourd’hui, comme dans Node-RED. Le compteur vaut zéro pendant les vacances.
Le nom des vacances est inconnu hors vacances. Un jour ouvré signifie ici lundi à vendredi,
hors jour férié : il ne reflète pas votre contrat ni vos congés.

## Sources et dates

- https://calendrier.api.gouv.fr/jours-feries/martinique.json
- https://data.education.gouv.fr/explore/dataset/fr-en-calendrier-scolaire/
- Documentation architecture : https://developers.home-assistant.io/docs/integration_fetching_data/

Actualisation distante quotidienne, contrôle horaire et recalcul à minuit dans le
fuseau configuré dans Home Assistant. Les dates scolaires sont interprétées en Europe/Paris,
car les dates métropolitaines du jeu officiel sont encodées en UTC à la veille du jour civil.
Le jour de départ est inclus et la reprise est exclue. Ce sont des états par jour,
pas une gestion du départ après la classe ni du cas des élèves sans cours le samedi.

Cache persistant via Home Assistant Store. En cas de panne, réutilisation des dernières
réponses valides et attribut `cached_data: true`. Sans cache au premier démarrage, l’intégration
réessaie via Home Assistant. Un millésime absent ou un calendrier scolaire dépassé produit
un état inconnu plutôt qu’un faux « pas de vacances ». Le cache n’est pas embarqué dans le ZIP.
Une connexion Internet est donc nécessaire pour le premier chargement.

## Validation et limites

Exécuter `python -m unittest discover -s tests -v` et
`python -m compileall -q custom_components`.
Tests du moteur : bornes scolaires, UTC/Paris, Martinique, changement d’année,
week-end, compteur et données manquantes. Les workflows fournissent Hassfest et HACS.
Cette v0.1.1 doit être testée dans votre Home Assistant avant utilisation opérationnelle.
Les tests du moteur ne remplacent pas les tests d’intégration du config flow et des pannes HTTP.
Pas encore d’entités calendar ni de diagnostics. Les champs Node-RED sont couverts selon la table ci-dessous, avec les différences de dates et de valeurs absentes décrites.
Licence Apache-2.0.

Les entités disposent d’icônes et de noms traduits en français et anglais.

## Correspondance Node-RED — 23 entités

Les 10 entités existantes gardent leurs unique_id. 13 capteurs sont ajoutés.
Les dates Home Assistant sont de vrais capteurs date (ISO), affichés selon la langue
utilisateur, au lieu de chaînes JJ/MM/AAAA. Les données absentes sont inconnues (`None`),
pas `-1`. La période actuelle signifie aujourd’hui : Node-RED peut aussi renseigner
son nom et sa fin dès la veille si demain est en vacances. Ici les capteurs actuels
restent inconnus jusqu’au début, et les capteurs prochaines vacances couvrent la veille.

| Champ Node-RED | Clé d’entité Home Assistant |
|---|---|
| day (dimanche=0, samedi=6) | sensor / day |
| isPublicHoliday | binary_sensor / public_holiday |
| isTomorrowPublicHoliday | binary_sensor / public_holiday_tomorrow |
| publicHolidayName | sensor / public_holiday_name |
| nextPublicHolidayName | sensor / next_public_holiday |
| nextPublicHolidayDate | sensor / next_public_holiday_date |
| isSchoolHolidays | binary_sensor / school_holidays |
| isTomorrowSchoolHolidays | binary_sensor / school_holidays_tomorrow |
| schoolHolidaysName | sensor / school_holiday_name |
| schoolHolidaysEndDate | sensor / school_holidays_end_date |
| nextSchoolHolidaysCountdownInDays | sensor / next_school_holidays_countdown |
| nextSchoolHolidaysCoutdownInDays (ancien alias) | attribut du même capteur, sans doublon |
| nextSchoolHolidaysName | sensor / next_school_holidays |
| nextSchoolHolidaysStartDate | sensor / next_school_holidays_start |
| nextSchoolHolidaysEndDate | sensor / next_school_holidays_end |
| schoolPeriod | sensor / school_period |
| year | sensor / year |
| region | sensor / region (identifiant API, par exemple martinique) |
| academy | sensor / academy |
| zones | sensor / zones |
| version | sensor / version (version Python, pas version Node-RED) |

Les quatre capteurs académie, région, zone et version sont classés diagnostics.
Le compteur existant `days_until_school_holidays` vaut toujours zéro pendant les
vacances. Le nouveau `next_school_holidays_countdown` compte vers la période suivante,
même pendant les vacances en cours. Les deux capteurs week-end et jour ouvré restent
également disponibles, bien que le payload Node-RED actuel ne les expose pas.

### Mise à jour depuis la version publiée 0.1.0

Remplacer le dossier `custom_components/french_holidays` puis redémarrer Home Assistant.
Ne pas supprimer l’entrée de configuration : les identifiants existants seront conservés.
Le cache ancien est rafraîchi pour récupérer la zone. Si le réseau est indisponible,
les anciennes données restent utilisées et la zone est temporairement inconnue.
