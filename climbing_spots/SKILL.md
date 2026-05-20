---
name: climbing_spots
description: Cherche les sites et salles d'escalade autour d'une position GPS. Trigger when user asks "trouver spot", "salle escalade près de", "où grimper à".
allowed-tools: Bash(python3 *)
---

# Skill `climbing_spots`

Pour chercher les spots d'escalade :

```bash
python3 ${CLAUDE_SKILL_DIR}/spots.py --lat <LATITUDE> --lon <LONGITUDE> --radius <RAYON_EN_METRES>
```

Renvoie une liste JSON de spots avec leurs coordonnées `lat` / `lon` et s'ils sont en intérieur (`is_indoor`).
