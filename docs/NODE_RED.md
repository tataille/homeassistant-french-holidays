# Correspondance avec Node-RED


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
