---
name: hotels
description: Trouve des hôtels ou auberges à proximité d'une position GPS et donne une estimation du prix de la nuitée. Trigger when user asks "dormir", "hôtel près de", "hébergement".
allowed-tools: Bash(python3 *)
---

# Skill `hotels`

Pour chercher un hébergement :

```bash
python3 ${CLAUDE_SKILL_DIR}/hotels.py --lat <LATITUDE> --lon <LONGITUDE> --radius <RAYON_EN_METRES>
```

Renvoie une liste JSON d'hôtels avec leurs coordonnées `lat` / `lon`, leur site web et un prix estimé par nuit (`estimated_price_eur`).
