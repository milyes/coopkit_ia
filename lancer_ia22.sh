#!/bin/bash

# 🧠 IA22 – Activation locale du modèle souverain
# Ce script initialise, vérifie, et trace le modèle IA22 dans l’écosystème SYSTEMEOSIA

echo "🔁 Initialisation du modèle IA22..."

# 1. Activation de l’environnement virtuel
source ~/ia22_env/bin/activate

# 2. Lancement du modèle IA local
python3 ~/ia22_model/main.py --mode=local --audit=symbolic --trace=on

# 3. Vérification de l’intégrité
if [ $? -eq 0 ]; then
    echo "✅ Modèle IA22 lancé avec succès."
    echo "🧬 Audit symbolique activé."
else
    echo "❌ Échec du lancement IA22. Vérifier les logs."
    exit 1
fi

# 4. Enregistrement de la trace
echo "$(date) - IA22 activé localement avec audit symbolique" >> ~/ia22_logs/trace.log

# 5. Option de diffusion cockpit
read -p "Souhaitez-vous diffuser cette activation dans le cockpit SYSTEMEOSIA ? (y/n): " choix
if [ "$choix" == "y" ]; then
    cp ~/ia22_logs/trace.log ~/SYSTEMEOSIA/cockpit/audit_ia22.log
    echo "📡 Trace IA22 diffusée dans le cockpit."
else
    echo "🛑 Diffusion cockpit désactivée."
fi

