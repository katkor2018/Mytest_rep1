import requests

# 1. URL для POST-запроса
url = "https://jsonplaceholder.typicode.com/posts"

# 2. Словарь с данными для отправки
data = {
    'title': 'foo',
    'body': 'bar',
    'userId': 1
}

# 3. Отправка POST-запроса с этими данными
response = requests.post(url, json=data)

# 4. Вывод статус-кода и содержимого ответа
print("Status code:", response.status_code)
print("Ответ:", response.json())