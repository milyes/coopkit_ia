#!/usr/bin/env python3

import sys

def generate(args):
    print("✅ Capsule miroir générée avec slogan :", args)

def audit(args):
    print("✅ Audit symbolique activé avec source :", args)

def diffuse(args):
    print("✅ Capsule diffusée sur :", args)

def trace(args):
    print("✅ Trace cognitive enregistrée :", args)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("✘ Commande manquante")
        sys.exit(1)

    command = sys.argv[1]
    args = sys.argv[2:]

    if command == "generate":
        generate(args)
    elif command == "audit":
        audit(args)
    elif command == "diffuse":
        diffuse(args)
    elif command == "trace":
        trace(args)
    else:
        print(f"✘ Format inconnu : {command}")
