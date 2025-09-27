#!/bin/bash
# SYSTEMEOSIA – CoopKit IA Launcher Setup
# Auteur : Ilyes Zoubirou

echo "🔧 Initialisation du cockpit CoopKit IA..."

# 1. Création de l’environnement Python
echo "📦 Création de l’environnement virtuel..."
python3 -m venv venv
source venv/bin/activate

# 2. Installation des dépendances
echo "📡 Installation des modules Flask et JSON..."
pip install flask

# 3. Lancement du serveur IA
echo "🚀 Lancement du serveur CoopKit IA..."
nohup python3 coopkit_launcher.py > logs.txt 2>&1 &

# 4. Ouverture du cockpit HTML
echo "🧭 Ouverture du cockpit SYSTEMEOSIA..."
xdg-open index.html

# 5. Confirmation
echo "✅ CoopKit IA opérationnel. Capsule prête à recevoir des signaux."
