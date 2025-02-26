import requests
import json
import os

# Definir la URL de la API
URL = "https://restcountries.com/v3.1/all"

# Directorio donde guardaremos el JSON
OUTPUT_DIR = "src/pad_2025/static/json"
OUTPUT_FILE = os.path.join(OUTPUT_DIR, "paises.json")

def obtener_datos_paises():
    """Obtiene datos de la API REST Countries y los guarda en un archivo JSON."""
    try:
        response = requests.get(URL)
        response.raise_for_status()  # Lanza un error si la solicitud falla
        datos = response.json()
        
        # Extraer solo la información relevante
        paises_info = [
            {
                "nombre": pais.get("name", {}).get("common", "Desconocido"),
                "capital": pais.get("capital", ["Desconocida"])[0],
                "poblacion": pais.get("population", 0),
                "idiomas": list(pais.get("languages", {}).values()),
                "bandera": pais.get("flags", {}).get("png", "Sin bandera")
            }
            for pais in datos
        ]

        # Crear la carpeta si no existe
        os.makedirs(OUTPUT_DIR, exist_ok=True)

        # Guardar en un archivo JSON
        with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
            json.dump(paises_info, f, indent=4, ensure_ascii=False)

        print(f"✅ Datos guardados en {OUTPUT_FILE}")

    except requests.exceptions.RequestException as e:
        print(f"⚠️ Error al obtener los datos: {e}")

# Ejecutar el script
if __name__ == "__main__":
    obtener_datos_paises()
