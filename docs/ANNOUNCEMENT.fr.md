# French Holidays : jours fériés et vacances scolaires dans Home Assistant

J’ai porté mon module Node-RED French Holidays vers une intégration native Home Assistant.

Choisissez votre académie et votre région pour retrouver les jours fériés, les vacances scolaires en cours, les prochaines dates et les comptes à rebours. Les 23 entités se configurent depuis l’interface, sans Node-RED ni MQTT. Un cache persistant permet de réutiliser les calendriers déjà téléchargés en cas de coupure réseau.

Quelques usages : conditionner le réveil aux jours ouvrés, adapter les horaires de chauffage pendant les vacances ou afficher les prochaines vacances sur le tableau de bord.

Les jours fériés incluent les régions d’outre-mer proposées. Les dates scolaires sont actuellement interprétées en Europe/Paris ; Nantes est la configuration testée et les académies ultramarines restent à vérifier.

Installation : HACS → Dépôts personnalisés → `https://github.com/tataille/homeassistant-french-holidays` → Intégration, puis téléchargement et redémarrage de Home Assistant.

- Projet et documentation : https://github.com/tataille/homeassistant-french-holidays
- Ouvrir dans HACS : https://my.home-assistant.io/redirect/hacs_repository/?owner=tataille&repository=homeassistant-french-holidays&category=integration
- Versions : https://github.com/tataille/homeassistant-french-holidays/releases
- Retours et bugs : https://github.com/tataille/homeassistant-french-holidays/issues

L’ajout au catalogue HACS n’est pas encore acquis. Vos retours sur les calendriers et les automatisations sont les bienvenus !

Visuel illustratif : https://raw.githubusercontent.com/tataille/homeassistant-french-holidays/main/docs/images/entities-overview.svg

Pour accompagner l’annonce, utilisez une capture réelle de votre tableau de bord ; le visuel du dépôt est une illustration.
