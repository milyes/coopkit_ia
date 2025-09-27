#!/usr/bin/env python3

import os
import sys

def neutralise(path):
    if os.path.exists(path):
        try:
            os.remove(path)
            print(f"✅ Fichier neutralisé : {path}")
        except Exception as e:
            print(f"❌ Échec de suppression : {e}")
    else:
        print("⚠️ Fichier introuvable.")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage : python3 neutralise.py <chemin_du_fichier>")
        sys.exit(1)
    neutralise(sys.argv[1])

