# Exemples d’automatisation

Ces exemples se copient individuellement dans l’éditeur YAML d’une nouvelle automatisation : **Paramètres → Automatisations et scènes → Créer une automatisation → Nouvelle automatisation**, puis **⋮ → Modifier en YAML**.

## Choisir les entités de votre installation

Les identifiants ci-dessous sont des **exemples à remplacer**, pas les identifiants garantis de French Holidays. Retrouvez les vôtres dans **Paramètres → Appareils et services → French Holidays → Entités**, ou **Outils de développement → États**.

| Identifiant à remplacer | Entité à sélectionner |
|---|---|
| `binary_sensor.votre_jour_ouvre` | Jour ouvré |
| `binary_sensor.vos_vacances_scolaires` | Vacances scolaires aujourd’hui |
| `climate.votre_chauffage` | Votre thermostat compatible avec `climate.set_temperature` |

Les horaires utilisent le fuseau horaire de Home Assistant. Les températures sont des exemples pour une installation en degrés Celsius ; adaptez-les à votre équipement et à vos habitudes.

## Réveil les jours ouvrés, hors vacances scolaires

À 07:00, une notification apparaît dans Home Assistant si **Jour ouvré = on** et **Vacances scolaires = off**. La notification ne joue pas de son et n’est pas envoyée automatiquement au téléphone : remplacez l’action par votre éclairage, votre enceinte ou votre service de notification mobile pour créer votre réveil.

Retirez la condition sur les vacances si votre rythme de travail ne dépend pas du calendrier scolaire. « Jour ouvré » désigne lundi à vendredi, hors jour férié dans la région configurée ; ce capteur ne connaît pas vos horaires professionnels ou vos congés personnels.

[Télécharger le YAML](../examples/automations/reveil_jours_ouvres.yaml)

```yaml
alias: "French Holidays - Réveil les jours ouvrés"
description: "Notification à 07:00 les jours ouvrés hors vacances scolaires."
triggers:
  - trigger: time
    at: "07:00:00"
conditions:
  - condition: state
    entity_id: binary_sensor.votre_jour_ouvre
    state: "on"
  - condition: state
    entity_id: binary_sensor.vos_vacances_scolaires
    state: "off"
actions:
  - action: persistent_notification.create
    data:
      title: "Bonjour !"
      message: "Aujourd’hui est un jour ouvré hors vacances scolaires."
      notification_id: french_holidays_reveil
mode: single
```

## Chauffage du matin adapté aux vacances scolaires

À 06:30, cet exemple règle une consigne de **20 °C pendant les vacances**, ou **19 °C hors vacances**, pour un logement où les occupants restent davantage à la maison pendant les congés scolaires.

Le choix est volontairement explicite : si le capteur est `unknown` ou `unavailable`, aucune consigne n’est envoyée. Une période de vacances scolaires n’indique pas si votre logement est occupé : ajoutez vos conditions de présence si nécessaire.

Cet exemple change uniquement la température cible, sans forcer un mode chauffage ni définir une programmation pour toute la journée. Votre thermostat doit prendre en charge `climate.set_temperature` avec une consigne unique ; adaptez l’action aux équipements utilisant une plage de températures.

[Télécharger le YAML](../examples/automations/chauffage_vacances.yaml)

```yaml
alias: "French Holidays - Chauffage et vacances scolaires"
description: "Consigne du matin : 20 °C pendant les vacances, 19 °C hors vacances."
triggers:
  - trigger: time
    at: "06:30:00"
conditions: []
actions:
  - choose:
      - conditions:
          - condition: state
            entity_id: binary_sensor.vos_vacances_scolaires
            state: "on"
        sequence:
          - action: climate.set_temperature
            target:
              entity_id: climate.votre_chauffage
            data:
              temperature: 20
      - conditions:
          - condition: state
            entity_id: binary_sensor.vos_vacances_scolaires
            state: "off"
        sequence:
          - action: climate.set_temperature
            target:
              entity_id: climate.votre_chauffage
            data:
              temperature: 19
mode: single
```

## Vérifier vos réglages

Après remplacement des identifiants, enregistrez l’automatisation. Pour le réveil, vérifiez les états des deux capteurs puis choisissez temporairement une heure quelques minutes plus tard : le bouton d’exécution manuelle des actions ne vérifie pas les conditions de l’automatisation.

Pour le chauffage, vérifiez les températures et la cible avant d’exécuter les actions : l’exécution envoie réellement une consigne au thermostat. Consultez ensuite la trace pour vérifier la branche choisie.

Références : [actions d’automatisation](https://www.home-assistant.io/docs/automation/action/), [Climate](https://www.home-assistant.io/integrations/climate/), [notifications persistantes](https://www.home-assistant.io/integrations/persistent_notification/).
