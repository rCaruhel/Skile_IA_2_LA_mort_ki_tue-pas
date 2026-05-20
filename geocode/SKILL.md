---
name: geocode
description: Convertit un nom de ville en coordonnées GPS (latitude, longitude). Trigger when user asks "coordonnées de ...", "où se trouve ...", ou a besoin de lat/lon pour une autre commande.
allowed-tools: Bash(python3 *)
---

# Skill `geocode`

Pour obtenir les coordonnées GPS d'une ville :

```bash
python3 ${CLAUDE_SKILL_DIR}/geocode.py --city "$ARGUMENTS"
```

La sortie est en JSON. Extraire `lat` et `lon` pour l'utiliser dans d'autres outils.
