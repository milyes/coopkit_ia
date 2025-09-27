#!/bin/bash

# Capsule cible
FILE="capsules/capsule_health.json"

# Vérification
if [ ! -f "$FILE" ]; then
  echo "❌ Capsule introuvable : $FILE"
  exit 1
fi

# Génération du hash SHA256
HASH=$(sha256sum "$FILE" | awk '{print $1}')
DATE=$(date +"%Y-%m-%d %H:%M:%S")

# Création du manifeste JSON
cat <<EOF > capsule_manifest.json
{
  "capsule_id": "coopkit_capsule_health_IA22",
  "architect": "Zoubirou Mohammed Ilyes",
  "activation_date": "$DATE",
  "module": "IA22_LOGIC_LAUNCHER",
  "sha256_hash": "$HASH",
  "status": "Scellé",
  "signature": "GEMINI CORE 2.6 PRO",
  "traceboard_link": "https://milyes.github.io/TRACEBOARD.html",
  "github_repo": "https://github.com/milyes/coopkit"
}
EOF

echo "✅ Capsule scellée avec succès."
echo "📦 SHA256 : $HASH"
echo "📝 Manifeste généré : capsule_manifest.json"
