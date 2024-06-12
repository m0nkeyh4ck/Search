from googlesearch import search
import re

class GoogleSearch:
    def search(self, query, num_results=5):
        results = list(search(query, num_results))
        return results

    def save_results(self, query, results):
        from datetime import datetime
        now = datetime.now()
        timestamp = now.strftime("%Y-%m-%d_%H-%M-%S")
        file_name = f"resultados_{timestamp}.txt"
        with open(file_name, "w", encoding="utf-8") as file:
            file.write(f"Búsqueda: {query}\n")
            file.write(f"Fecha y hora: {now}\n\n")
            for i, result in enumerate(results, start=1):
                file.write(f"Resultado {i}:\n")
                file.write(result + "\n\n")
        print(f"Búsqueda completada. Resultados guardados en '{file_name}'.")

    def display_results(self, results):
        print("Resultados de la búsqueda:")
        for i, result in enumerate(results, start=1):
            print(f"Resultado {i}:\n{result}\n")

    def filter_valid_urls(self, results):
        valid_urls = []
        for result in results:
            # Verificar si el resultado es una URL válida
            if re.match(r'https?://(?:[-\w.]|(?:%[\da-fA-F]{2}))+', result):
                valid_urls.append(result)
        return valid_urls
