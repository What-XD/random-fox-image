import requests

API_URL = "https://randomfox.ca/floof/"

def get_random_fox_url() -> str:
    """Возвращает URL случайной картинки лисы."""
    response = requests.get(API_URL, timeout=5)
    response.raise_for_status()
    return response.json()["image"]

def download_random_fox(path: str = "fox.jpg") -> str:
    """Скачивает случайное изображение лисы в файл."""
    url = get_random_fox_url()
    img = requests.get(url, timeout=5)
    img.raise_for_status()
    with open(path, "wb") as f:
        f.write(img.content)
    return path
