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

        # Guardar en un archivo tipo .JSON
        with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
            json.dump(paises_info, f, indent=4, ensure_ascii=False)

        print(f" Datos guardados en {OUTPUT_FILE}")

    except requests.exceptions.RequestException as e:
        print(f" Error al obtener los datos: {e}")

def mostrar_ejemplo_datos():
    """Lee el archivo JSON y muestra un ejemplo de datos."""
    ruta_json = OUTPUT_FILE  # Usar la ruta definida globalmente
    try:
        with open(ruta_json, "r", encoding="utf-8") as file:
            data = json.load(file)

        print("\n Ejemplo de datos extraídos:")
        for i, pais in enumerate(data[:5]):
            print(f"{i+1}. {pais}")
    except FileNotFoundError:
        print(f"Error: El archivo {ruta_json} no existe.")

def leer_datos_paises():
    """Lee el archivo JSON de países y muestra un resumen."""
    try:
        with open(OUTPUT_FILE, "r", encoding="utf-8") as file:
            data = json.load(file)

        print("\n Datos cargados correctamente. Ejemplo de 5 países:\n")
        
        # Mostrar información de los primeros 5 países
        for i, pais in enumerate(data[:5]):
            nombre = pais.get("nombre", "Desconocido")
            capital = pais.get("capital", "Desconocida")
            poblacion = pais.get("poblacion", 0)
            idiomas = ", ".join(pais.get("idiomas", ["No disponible"]))
            bandera = pais.get("bandera", "No disponible")

            print(f"{i+1}. 🇦🇺 {nombre}")
            print(f" Capital: {capital}")
            print(f" Población: {poblacion:,}")
            print(f" Idiomas: {idiomas}")
            print(f" Bandera: {bandera}\n")
    except FileNotFoundError:
        print(f"Error: El archivo {OUTPUT_FILE} no existe.")

# Ejecutar el script
if __name__ == "__main__":
    obtener_datos_paises()
    mostrar_ejemplo_datos()
    leer_datos_paises()