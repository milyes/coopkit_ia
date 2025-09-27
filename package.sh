#!/bin/bash

# Nom du fichier à sceller
FILE="capsules/capsule_health.json"

# Vérification d'existence
if [ ! -f "$FILE" ]; then
  echo "❌ Capsule introuvable : $FILE"
  exit 1
fi

# Génération du hash SHA256
HASH=$(sha256sum "$FILE" | awk '{print $1}')
DATE=$(date +"%Y-%m-%d %H:%M:%S")

# Création du manifeste
echo "{
  \"capsule\": \"$FILE\",
  \"sha256\": \"$HASH\",
  \"scellé_le\": \"$DATE\",
  \"signature\": \"GEMINI CORE 2.6 PRO\",
  \"architecte\": \"Zoubirou Mohammed Ilyes\"
}" > capsule_manifest.json

echo "✅ Capsule scellée avec succès."
echo "📦 SHA256 : $HASH"
echo "📝 Manifeste : capsule_manifest.json"

