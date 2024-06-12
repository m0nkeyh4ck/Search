from google_search import GoogleSearch
from content_extractor import ContentExtractor
import time

def main():
    google_search = GoogleSearch()
    content_extractor = ContentExtractor()

    while True:
        query = input("¿Qué quieres buscar? (Escribe 'salir' para terminar): ")

        if query.lower() == "salir":
            print("¡Hasta luego!")
            break

        results = google_search.search(query)
        valid_urls = google_search.filter_valid_urls(results)

        google_search.save_results(query, valid_urls)
        google_search.display_results(valid_urls)

        while True:
            choice = input("¿A cuál de los resultados deseas acceder? (Escribe el número correspondiente o 'salir' para terminar): ")
            if choice.lower() == "salir":
                print("¡Hasta luego!")
                return
            try:
                choice_index = int(choice) - 1
                if 0 <= choice_index < len(valid_urls):
                    break
                else:
                    print("¡Elige un número válido!")
            except ValueError:
                print("¡Elige un número válido!")

        while True:
            num_lines = input("¿Cuántas líneas deseas mostrar? (Escribe un número o 'salir' para terminar): ")
            if num_lines.lower() == "salir":
                print("¡Hasta luego!")
                return
            try:
                num_lines = int(num_lines)
                if num_lines > 0:
                    break
                else:
                    print("¡Elige un número válido!")
            except ValueError:
                print("¡Elige un número válido!")

        page_url = valid_urls[choice_index]
        print(f"Accediendo al resultado {choice} ({page_url})...")
        content_extractor.extract_and_display_content(page_url, num_lines)

if __name__ == "__main__":
    main()
