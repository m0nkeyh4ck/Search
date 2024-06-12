from googlesearch import search
from datetime import datetime
import time

# Función para realizar una búsqueda en Google, guardar los resultados en un archivo con la fecha y la hora, y mostrarlos en pantalla de manera bonita
def google_search_and_display(query, num_results=5):
    # Obtener la fecha y hora actual
    now = datetime.now()
    timestamp = now.strftime("%Y-%m-%d_%H-%M-%S")

    # Realizar la búsqueda en Google
    results = search(query, num=num_results, stop=num_results)

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
