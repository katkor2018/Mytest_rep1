import requests
from bs4 import BeautifulSoup

def get_keywords(url):
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
    except Exception as e:
        print(f"Ошибка при запросе к сайту: {e}")
        return

    soup = BeautifulSoup(response.text, 'html.parser')
    keywords_tag = soup.find("meta", attrs={"name": "keywords"})
    if keywords_tag and "content" in keywords_tag.attrs:
        keywords = keywords_tag["content"].strip()
        print(f"Ключевые слова сайта {url}:")
        print(keywords)
    else:
        print(f"Ключевые слова на сайте {url} не найдены.")

if __name__ == "__main__":
    url = ("https://www.")  # Укажите здесь нужный сайт
    get_keywords(url)