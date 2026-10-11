# Demande d’ajout au catalogue HACS

Version publiée : [v0.1.2](https://github.com/tataille/homeassistant-french-holidays/releases/tag/v0.1.2).

Validation du code inclus dans cette release : [tests, HACS et Hassfest](https://github.com/tataille/homeassistant-french-holidays/actions/runs/38170844625), tous réussis sans désactivation de contrôle. Le tag pointe sur le commit de publication ; les fichiers de l’intégration sont identiques au commit validé `1a7de6c3a6a7a6181befb0b085fea57ed282fd97`.

## Étape restante

Créer un fork personnel de [hacs/default](https://github.com/hacs/default/fork) sous le compte `tataille`. Créer une branche `add-french-holidays` à partir de `master`. Dans le fichier JSON `integration`, ajouter `"tataille/homeassistant-french-holidays"` entre `"tarikbc/ha-ppa-contatto"` et `"tbclark3/ha-xweatherly"`, en conservant les virgules et l’ordre alphabétique.

Ouvrir une PR vers `hacs/default:master`, avec l’option autorisant les mainteneurs à modifier la branche. Ne pas demander de reviewers. Titre : `Add French Holidays integration`.

La connexion GitHub utilisée pour préparer ce projet ne propose pas de création de fork. Aucun ajout au catalogue n’a encore été soumis.

## Corps de la PR

Copier le texte ci-dessous dans la description de la PR :

## Checklist

- [x] I've read the [publishing documentation](https://hacs.xyz/docs/publish/start).
- [x] I've added the [HACS action](https://hacs.xyz/docs/publish/action) to my repository.
- [x] (For integrations only) I've added the [hassfest action](https://developers.home-assistant.io/blog/2020/04/16/hassfest/) to my repository.
- [x] The actions are passing without any disabled checks in my repository.
- [x] I've added a link to the action run on my repository below in the links section.
- [x] I've created a new release of the repository after the validation actions were run successfully.

## Links

Link to current release: https://github.com/tataille/homeassistant-french-holidays/releases/tag/v0.1.2
Link to successful HACS action (without the `ignore` key): https://github.com/tataille/homeassistant-french-holidays/actions/runs/38170844625/job/114562941463
Link to successful hassfest action (if integration): https://github.com/tataille/homeassistant-french-holidays/actions/runs/38170844625/job/114562941464

## Integration

I am the owner and maintainer of this repository. French Holidays provides French public holidays and school holidays for Home Assistant, with academy and public holiday region selection, 23 entities, French and English translations, and persistent calendar caching. It is a native Python port of my Node-RED module and requires neither Node-RED nor MQTT.

The released `hacs.json` declares `country: FR`. Local branding is provided in `custom_components/french_holidays/brand/`.

<!-- tid:73253df5-5376-4e68-8c16-b234da6a2de3 -->
