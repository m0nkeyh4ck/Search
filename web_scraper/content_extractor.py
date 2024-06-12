import requests
from bs4 import BeautifulSoup

class ContentExtractor:
    def extract_and_display_content(self, url, num_lines):
        response = requests.get(url)
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')
            title = soup.title.string.strip() if soup.title else "No hay título"
            print("Título:", title)
            paragraphs = soup.find_all("p")
            print(f"\nContenido (mostrando las primeras {num_lines} líneas):")
            for i, paragraph in enumerate(paragraphs):
                if i >= num_lines:
                    break
                print(paragraph.text.strip())
                print()
        else:
            print("No se pudo acceder a la página.")
