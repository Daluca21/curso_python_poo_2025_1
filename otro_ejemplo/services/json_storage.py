import json
import os

def guardar_json(ruta, data):
    with open(ruta, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4)

def cargar_json(ruta):
    if not os.path.exists(ruta):
        return None
    with open(ruta, "r", encoding="utf-8") as f:
        return json.load(f)
