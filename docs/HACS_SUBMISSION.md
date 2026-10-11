# Demande d’ajout au catalogue HACS

Version publiée : [v0.1.2](https://github.com/tataille/homeassistant-french-holidays/releases/tag/v0.1.2).

Validation du code inclus dans cette release : [tests, HACS et Hassfest](https://github.com/tataille/homeassistant-french-holidays/actions/runs/38170844625), tous réussis sans désactivation de contrôle. Le tag pointe sur le commit de publication ; les fichiers de l’intégration sont identiques au commit validé `1a7de6c3a6a7a6181befb0b085fea57ed282fd97`.

## Soumettre la PR

Le fork `tataille/default` et la branche `add-french-holidays` sont prêts. Le commit `28ce03a3507722b0da96d5d78ee33d532bb18f99` ajoute uniquement une ligne au fichier `integration`, dans l’ordre alphabétique.

[Ouvrir la PR avec le titre et la description préremplis](https://github.com/hacs/default/compare/master...tataille:default:add-french-holidays?expand=1&title=Add%20French%20Holidays%20integration&body=%23%23%20Checklist%0A%0A-%20%5B%20%5D%20I've%20read%20the%20%5Bpublishing%20documentation%5D(https%3A%2F%2Fhacs.xyz%2Fdocs%2Fpublish%2Fstart).%0A-%20%5Bx%5D%20I've%20added%20the%20%5BHACS%20action%5D(https%3A%2F%2Fhacs.xyz%2Fdocs%2Fpublish%2Faction)%20to%20my%20repository.%0A-%20%5Bx%5D%20(For%20integrations%20only)%20I've%20added%20the%20%5Bhassfest%20action%5D(https%3A%2F%2Fdevelopers.home-assistant.io%2Fblog%2F2020%2F04%2F16%2Fhassfest%2F)%20to%20my%20repository.%0A-%20%5Bx%5D%20The%20actions%20are%20passing%20without%20any%20disabled%20checks%20in%20my%20repository.%0A-%20%5Bx%5D%20I've%20added%20a%20link%20to%20the%20action%20run%20on%20my%20repository%20below%20in%20the%20links%20section.%0A-%20%5Bx%5D%20I've%20created%20a%20new%20release%20of%20the%20repository%20after%20the%20validation%20actions%20were%20run%20successfully.%0A%0A%23%23%20Links%0A%0ALink%20to%20current%20release%3A%20https%3A%2F%2Fgithub.com%2Ftataille%2Fhomeassistant-french-holidays%2Freleases%2Ftag%2Fv0.1.2%0ALink%20to%20successful%20HACS%20action%20(without%20the%20%60ignore%60%20key)%3A%20https%3A%2F%2Fgithub.com%2Ftataille%2Fhomeassistant-french-holidays%2Factions%2Fruns%2F38170844625%2Fjob%2F114562941463%0ALink%20to%20successful%20hassfest%20action%20(if%20integration)%3A%20https%3A%2F%2Fgithub.com%2Ftataille%2Fhomeassistant-french-holidays%2Factions%2Fruns%2F38170844625%2Fjob%2F114562941464%0A%0A%23%23%20Integration%0A%0AI%20am%20the%20owner%20and%20maintainer%20of%20this%20repository.%20French%20Holidays%20provides%20French%20public%20holidays%20and%20school%20holidays%20for%20Home%20Assistant%2C%20with%20academy%20and%20public%20holiday%20region%20selection%2C%2023%20entities%2C%20French%20and%20English%20translations%2C%20and%20persistent%20calendar%20caching.%20It%20is%20a%20native%20Python%20port%20of%20my%20Node-RED%20module%20and%20requires%20neither%20Node-RED%20nor%20MQTT.%0A%0AThe%20released%20%60hacs.json%60%20declares%20%60country%3A%20FR%60.%20Local%20branding%20is%20provided%20in%20%60custom_components%2Ffrench_holidays%2Fbrand%2F%60.%0A%0A%3C!--%20tid%3A73253df5-5376-4e68-8c16-b234da6a2de3%20--%3E%0A). Vérifier que « Allow edits by maintainers » est coché, puis cliquer sur « Create pull request ». Ne pas demander de reviewers.

GitHub a refusé la création automatique de la PR vers `hacs/default` avec l’erreur 403 « Resource not accessible by integration ». La PR n’a donc pas encore été soumise.

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
