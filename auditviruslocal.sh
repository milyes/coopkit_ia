#!/data/data/com.termux/files/usr/bin/bash

echo "🔍 Audit local en cours..."

# 1. Scan des processus suspects
ps aux | grep -vE 'termux|bash|python' > ~/coopkit/logs.txt

# 2. Vérification des fichiers exécutables inconnus
find ~/ -type f -executable > ~/coopkit/suspects_exec.txt

# 3. Analyse des connexions réseau
netstat -tulnp > ~/coopkit/netstat_trace.txt

# 4. Résumé
echo "✅ Audit terminé. Traces enregistrées dans ~/coopkit/"

