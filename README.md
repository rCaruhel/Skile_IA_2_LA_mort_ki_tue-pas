# 🧗 Skile IA - Climbing & Trip Assistant (Plugin Claude Code)

Ce projet est un plugin regroupant un ensemble de **skills** conçus pour aider un agent IA (comme Claude Code) à planifier des sessions et voyages d'escalade. 

Basé sur une architecture "Progressive Disclosure" (faible empreinte token), le plugin n'expose que des descriptions courtes à l'agent. Les scripts associés ne sont exécutés qu'à la demande, garantissant une grande réactivité et une économie de contexte.

## 🚀 Comment ça marche ? (Pour l'Agent)

En tant qu'agent, tu dois orchestrer ces différents outils en fonction de la demande de l'utilisateur. Voici le flux logique recommandé :

1. L'utilisateur donne un nom de lieu (ex: "Je veux grimper à Annecy").
2. 📍 **`geocode`** : Utilise ce skill en premier pour convertir le nom de la ville en coordonnées GPS (Latitude/Longitude).
3. 🧗 **`climbing_spots`** : Une fois les coordonnées obtenues, utilise ce skill pour trouver les falaises ou salles d'escalade dans un rayon donné.
4. ⛅ **`climbing_weather`** : Passe les coordonnées exactes du spot trouvé à ce skill pour vérifier si le rocher est sec et à bonne température.
5. 🏨 **`hotels`** (Optionnel) : Si l'utilisateur souhaite rester sur place, utilise ce skill pour trouver des hébergements autour du spot et obtenir un prix estimé.
6. 🗺️ **`climbing_routing`** (Optionnel) : Si l'utilisateur demande un trajet ou fait un road-trip, passe la liste de toutes les coordonnées (départ, hôtel, spots) à ce skill pour générer le temps de trajet global et le lien Google Maps avec étapes.

## 📦 Les 5 Skills inclus

Chaque skill est autonome et possède son propre script CLI Python :

- **`geocode/`** : Traduit un nom de lieu en coordonnées GPS.
- **`climbing_spots/`** : Radar à falaises (Outdoor) et salles d'escalade (Indoor) via Overpass API.
- **`climbing_weather/`** : Analyseur météo (Open-Meteo) pour trouver les meilleures fenêtres de tir (sec, jour, température).
- **`hotels/`** : Chercheur d'auberges et hôtels avec algorithme d'estimation de prix.
- **`climbing_routing/`** : Planificateur de road-trip (OSRM) supportant de multiples étapes.

## 🛠️ Installation & Dépendances

1. Installer les bibliothèques requises :
   ```bash
   pip install -r requirements.txt
   ```
2. (Pour Claude Code) Copier les dossiers des skills dans le répertoire des plugins de Claude :
   ```bash
   cp -r geocode climbing_spots climbing_weather hotels climbing_routing ~/.claude/skills/
   ```
