import os
import numpy as np
import matplotlib.pyplot as plt
import csv
import requests

# Definir rutas organizadas
BASE_DIR = "static"
TXT_DIR = os.path.join(BASE_DIR, "txt")
CSV_DIR = os.path.join(BASE_DIR, "csv")
IMG_DIR = os.path.join(BASE_DIR, "img")

# Crear directorios si no existen
for directory in [TXT_DIR, CSV_DIR, IMG_DIR]:
    os.makedirs(directory, exist_ok=True)


#  1️ FUNCION PARA GRAFICAR POLINOMIOS Y GUARDAR IMAGEN
def graficar_polinomios(*polinomios):
    x = np.linspace(-10, 10, 400)

    plt.figure(figsize=(8, 6))

    for a, n in polinomios:
        y = a * x**n
        plt.plot(x, y, label=f'{a}x^{n}')

    plt.axhline(0, color='black', linewidth=0.8)
    plt.axvline(0, color='black', linewidth=0.8)
    plt.grid(True, linestyle='--', alpha=0.6)
    plt.legend()
    plt.title("Gráfica de Polinomios")
    plt.xlabel("Eje X")
    plt.ylabel("Eje Y")

    ruta_imagen = os.path.join(IMG_DIR, "grafica.png")
    plt.savefig(ruta_imagen)  # Guarda la imagen en la carpeta img
    plt.show(block=True)

    print(f" Gráfica guardada en: {ruta_imagen}")


#  2️ CLASE PARA LEER ARCHIVO TXT DE INSTRUCCIÓN 1
class LectorTXT:
    def __init__(self):
        self.ruta_txt = os.path.join(TXT_DIR, "instruccion_1.txt")

    def leer_txt(self):
        if not os.path.exists(self.ruta_txt):
            print(f" ERROR: El archivo '{self.ruta_txt}' no existe.")
            return None

        with open(self.ruta_txt, "r", encoding="utf-8") as f:
            return f.read()


#  3️ FUNCION PARA ESCRIBIR ARCHIVO CSV CON FRUTAS
def escribir_csv():
    frutas = [
        ["Manzana", "Roja", "Dulce"],
        ["Plátano", "Amarillo", "Dulce"],
        ["Lima", "Verde", "Ácida"]
    ]
    
    ruta_csv = os.path.join(CSV_DIR, "frutas.csv")

    with open(ruta_csv, mode="w", newline="", encoding="utf-8") as archivo:
        escritor_csv = csv.writer(archivo)
        escritor_csv.writerows(frutas)

    print(f" Archivo '{ruta_csv}' guardado exitosamente.")


#  4️ FUNCION PARA LEER ARCHIVO CSV DE FRUTAS
def leer_csv():
    ruta_csv = os.path.join(CSV_DIR, "frutas.csv")

    if not os.path.exists(ruta_csv):
        print(f" ERROR: El archivo '{ruta_csv}' no existe.")
        return None

    with open(ruta_csv, "r", encoding="utf-8") as f:
        reader = csv.reader(f)
        datos_frutas = [fila for fila in reader]
    
    return datos_frutas


#  5️ FUNCION PARA EXTRAER DATOS DE UNA API Y GUARDAR EN CSV
def extraer_api():
    url_usuarios = "https://jsonplaceholder.typicode.com/users"
    url_tareas = "https://jsonplaceholder.typicode.com/todos"

    usuarios = requests.get(url_usuarios).json()
    tareas = requests.get(url_tareas).json()

    tareas_completadas = [t for t in tareas if t["completed"]]

    usuarios_dict = {u["id"]: u["name"] for u in usuarios}

    ruta_csv = os.path.join(CSV_DIR, "tareas_completadas.csv")
    
    with open(ruta_csv, "w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(["ID Usuario", "Nombre", "ID Tarea", "Título"])  

        for tarea in tareas_completadas:
            writer.writerow([tarea["userId"], usuarios_dict[tarea["userId"]], tarea["id"], tarea["title"]])

    print(f" Pipeline completada. Archivo generado en: {ruta_csv}")


#  PRUEBAS
if __name__ == "__main__":
    graficar_polinomios((1, 2), (-0.5, 3), (2, 1))

    lector = LectorTXT()
    contenido = lector.leer_txt()
    if contenido:
        print("\n Contenido del archivo TXT:")
        print(contenido)

    escribir_csv()
    print("\n Datos del CSV de frutas:")
    print(leer_csv())

    extraer_api()
