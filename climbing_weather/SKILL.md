---
name: climbing_weather
description: Analyse la météo pour un spot et trouve le meilleur créneau pour grimper (sec, bonne température). Trigger when user asks "quand aller grimper", "météo falaise", "est-ce que le rocher est sec".
allowed-tools: Bash(python3 *)
---

# Skill `climbing_weather`

Pour obtenir les meilleurs créneaux météo pour grimper :

```bash
python3 ${CLAUDE_SKILL_DIR}/weather.py --lat <LATITUDE> --lon <LONGITUDE> [--indoor]
```

Renvoie du JSON avec une liste des meilleurs créneaux horaires (sans pluie, de jour, température agréable). Utiliser `--indoor` si c'est une salle.
