import json, sys, os
def generate_json():
    data = {
        "module": "health_tracking",
        "status": "active",
        "fields": {
            "patient_id": "string",
            "symptoms": ["tremor", "rigidity", "bradykinesia"],
            "timestamp": "ISO8601"
        },
        "validated_by": "SYSTEMEOSIA"
    }
    os.makedirs("capsules", exist_ok=True)
    with open("capsules/capsule_health.json", "w") as f:
        json.dump(data, f, indent=4)
    print("✔ Format JSON généré : capsule_health.json")

def generate_html():
    html = "<html><head><title>Capsule Santé</title></head><body><h1>Module: Health Tracking</h1><p>Status: Active</p><p>Validated by SYSTEMEOSIA</p></body></html>"
    os.makedirs("capsules", exist_ok=True)
    with open("capsules/capsule_health.html", "w") as f:
        f.write(html)
    print("✔ Format HTML généré : capsule_health.html")

def main():
    if len(sys.argv) < 2 or not sys.argv[1].strip():
        print("✘ Format manquant. Utilise : json, html")
        return
    fmt = sys.argv[1].lower()
    if fmt == "json": generate_json()
    elif fmt == "html": generate_html()
    else: print(f"✘ Format inconnu : {fmt}")

if __name__ == "__main__":
    main()
