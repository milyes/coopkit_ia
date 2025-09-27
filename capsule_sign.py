#!/usr/bin/env python3

import hashlib
import shutil
import os
from datetime import datetime

# 📁 Chemins
source_file = os.path.expanduser("~/SYSTEMEOSIA/cockpit/audit_ia22.log")
archive_dir = os.path.expanduser("~/SYSTEMEOSIA/cockpit/archives/")
capsule_path = os.path.expanduser("~/SYSTEMEOSIA/cockpit/capsule_trace_ia22.json")

# 🔐 Génération SHA256
def generate_sha256(file_path):
    with open(file_path, "rb") as f:
        return hashlib.sha256(f.read()).hexdigest()

# 🧬 Capsule JSON
def create_capsule(signature):
    capsule = {
        "capsule": {
            "titre": "Activation IA22 – Trace cockpit certifiée",
            "auteur": "SYSTEMEOSIA / CoopKit IA",
            "date": datetime.now().strftime("%Y-%m-%d"),
            "plateforme": "Android 15.0 + Termux",
            "script": "lancer_ia22.sh",
            "modele": "IA22 local",
            "audit": "symbolique activé",
            "trace": {
                "source": source_file,
                "copie": capsule_path,
                "signature_sha256": signature
            },
            "statut": "Activation réussie, trace archivée",
            "souverainete": "Aucune dépendance externe, aucune fuite",
            "balise": "Trace cryptographiée – activation sans évocation"
        }
    }
    return capsule

# 🗂️ Archivage
def archive_trace():
    os.makedirs(archive_dir, exist_ok=True)
    shutil.copy2(source_file, archive_dir + "audit_ia22_" + datetime.now().strftime("%Y%m%d") + ".log")

# 🧠 Exécution
if os.path.exists(source_file):
    sig = generate_sha256(source_file)
    capsule = create_capsule(sig)

    with open(capsule_path, "w") as f:
        import json
        json.dump(capsule, f, indent=2)

    archive_trace()
    print("✅ Capsule signée et archivée avec succès.")
else:
    print("❌ Fichier source introuvable.")
