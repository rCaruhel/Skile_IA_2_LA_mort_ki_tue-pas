---
name: climbing_routing
description: Calcule la distance, le temps de trajet en voiture et renvoie un lien GPS. Trigger when user asks "comment y aller", "trajet pour", "distance jusqu'à".
allowed-tools: Bash(python3 *)
---

# Skill `climbing_routing`

Pour calculer l'itinéraire entre plusieurs étapes (road-trip) :

```bash
python3 ${CLAUDE_SKILL_DIR}/routing.py --coords "lat1,lon1 lat2,lon2 lat3,lon3"
```

Renvoie du JSON contenant la distance, le temps de trajet et un lien Google Maps.
