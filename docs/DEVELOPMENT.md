# Développement

## Vérifier le code

```bash
python -m unittest discover -s tests -v
python -m compileall -q custom_components
```

Les tests couvrent le moteur de dates, les champs issus de Node-RED, les bornes des
vacances et les données absentes. Ils ne remplacent pas les tests d’intégration
sur Home Assistant : config flow, chargement des plateformes et erreurs réseau.

Les workflows GitHub exécutent les tests, Hassfest et la validation HACS.
Pour la validation HACS complète, il faut également une description et des topics
sur le dépôt, ainsi que des assets de marque acceptés par HACS.

## Architecture

- `config_flow.py` : configuration depuis l’interface.
- `coordinator.py` : téléchargement quotidien, recalcul local et cache persistant.
- `engine.py` : calculs sans dépendance Home Assistant.
- `entity.py`, `sensor.py`, `binary_sensor.py` : entités et identifiants stables.
- `strings.json`, `translations/` : libellés.

Les versions du manifest et de `const.VERSION` doivent rester synchronisées.
Le cache conserve des données JSON ; les objets date sont créés uniquement au calcul des états.

Pas encore d’entités calendrier ni de diagnostics téléchargeables.
La zone des anciens caches est récupérée lors de leur prochain rafraîchissement.
