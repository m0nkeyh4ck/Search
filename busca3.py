from googlesearch import search
from bs4 import BeautifulSoup
import requests
from datetime import datetime
import time

# Función para extraer un resumen del contenido de una página web y mostrarlo de manera bonita en la terminal
def extract_and_display_content(url):
    # Realizar solicitud HTTP para obtener el contenido de la página
    response = requests.get(url)
    if response.status_code == 200:
        # Parsear el contenido HTML utilizando BeautifulSoup
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Extraer el título de la página
        title = soup.title.string.strip() if soup.title else "No hay título"
        print("Título:", title)
        
        # Extraer los párrafos de la página y mostrar un resumen de cada uno
        paragraphs = soup.find_all("p")
        print("\nResumen del contenido:")
        for paragraph in paragraphs:
            words = paragraph.text.strip().split()
            summary = ' '.join(words[:30]) + ('...' if len(words) > 30 else '')
            print(summary)
            print()
    else:
        print("No se pudo acceder a la página.")

# Función para realizar una búsqueda en Google, guardar los resultados en un archivo con la fecha y la hora, y mostrarlos en pantalla de manera bonita
def google_search_and_display(query, num_results=5):
    # Obtener la fecha y hora actual
    now = datetime.now()
    timestamp = now.strftime("%Y-%m-%d_%H-%M-%S")

    # Realizar la búsqueda en Google
    results = list(search(query, num=num_results, stop=num_results))

    # Guardar los resultados en un archivo con la fecha y la hora
    file_name = f"resultados_{timestamp}.txt"
    with open(file_name, "w", encoding="utf-8") as file:
        file.write(f"Búsqueda: {query}\n")
        file.write(f"Fecha y hora: {now}\n\n")
        for i, result in enumerate(results, start=1):
            file.write(f"Resultado {i}:\n")
            file.write(result + "\n\n")
    print(f"Búsqueda completada. Resultados guardados en '{file_name}'.\n")

    # Leer el archivo de resultados y mostrarlos en pantalla de manera bonita
    with open(file_name, "r", encoding="utf-8") as file:
        results_text = file.read()
    print("Resultados de la búsqueda:")
    print(results_text)

    # Pedir al usuario que elija a cuál de los resultados acceder
    while True:
        choice = input("¿A cuál de los resultados deseas acceder? (Escribe el número correspondiente o 'salir' para terminar): ")
        if choice.lower() == "salir":
            print("¡Hasta luego!")
            return
        try:
            choice_index = int(choice) - 1
            if 0 <= choice_index < len(results):
                break
            else:
                print("¡Elige un número válido!")
        except ValueError:
            print("¡Elige un número válido!")

    # Extraer información de la página elegida y mostrarla en la terminal
    page_url = results[choice_index]
    print(f"Accediendo al resultado {choice} ({page_url})...")
    extract_and_display_content(page_url)

# Bucle interactivo
while True:
    # Pedir al usuario que introduzca la consulta de búsqueda
    query = input("¿Qué quieres buscar? (Escribe 'salir' para terminar): ")

    # Salir del bucle si el usuario escribe "salir"
    if query.lower() == "salir":
        print("¡Hasta luego!")
        break

    # Realizar la búsqueda en Google y mostrar los resultados
    google_search_and_display(query)

    # Esperar un rato antes de la próxima búsqueda
    time.sleep(2)  # Puedes ajustar el tiempo de espera según tus preferencias
