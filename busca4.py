from googlesearch import search
from bs4 import BeautifulSoup
import requests
import time

# Función para extraer un número específico de líneas del contenido de una página web y mostrarlas en la terminal
def extract_and_display_content(url, num_lines):
    # Realizar solicitud HTTP para obtener el contenido de la página
    response = requests.get(url)
    if response.status_code == 200:
        # Parsear el contenido HTML utilizando BeautifulSoup
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Extraer el título de la página
        title = soup.title.string.strip() if soup.title else "No hay título"
        print("Título:", title)
        
        # Extraer los párrafos de la página y mostrar el número especificado de líneas
        paragraphs = soup.find_all("p")
        print("\nContenido (mostrando las primeras {} líneas):".format(num_lines))
        for i, paragraph in enumerate(paragraphs):
            if i >= num_lines:
                break
            print(paragraph.text.strip())
            print()
    else:
        print("No se pudo acceder a la página.")

# Función para realizar una búsqueda en Google y mostrar el resultado más relevante
def google_search_and_display(query):
    try:
        # Realizar la búsqueda en Google y obtener solo el primer resultado
        search_results = search(query, num_results=1, stop=1)

        # Obtener el primer resultado de la lista
        page_url = next(search_results, None)

        if page_url:
            print(f"Accediendo al resultado de Google: {page_url}\n")
            # Extraer y mostrar el contenido de la página
            extract_and_display_content(page_url, num_lines=10)
        else:
            print("No se encontraron resultados para la búsqueda.")
    except Exception as e:
        print(f"Error al realizar la búsqueda: {e}")

# Bucle interactivo
def main():
    while True:
        query = input("¿Qué quieres buscar en Google? (Escribe 'salir' para terminar): ")
        if query.lower() == "salir":
            print("¡Hasta luego!")
            break

        google_search_and_display(query)
        print("---")

        time.sleep(2)  # Esperar un poco antes de la próxima búsqueda

if __name__ == "__main__":
    main()

