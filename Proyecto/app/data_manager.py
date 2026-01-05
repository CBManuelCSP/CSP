import json
from pathlib import Path

ARCHIVO_DATOS = Path("plantilla.json")

def cargar_datos() -> list:
    """
    Carga la plantilla desde su archivo JSON. 
    Devuelve una lista vacía si no existe o el archivo está corrupto.
    """
    # Comprobamos si el archivo existe
    if not ARCHIVO_DATOS.exists():
        return []
    
    try:
        with ARCHIVO_DATOS.open("r", encoding="utf-8") as f:
            return json.load(f)
        
    except (json.JSONDecodeError, IOError):
        return []

def guardar_datos(datos: list):
    """Función para guardar al nuevo jugador en el archivo JSON."""
    try:
        with ARCHIVO_DATOS.open("w", encoding="utf-8") as f:
            json.dump(datos, f, indent=4)

        print("Jugador guardado correctamente.")
    except IOError:
        print("Error al guardar al jugador.")