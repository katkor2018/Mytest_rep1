import requests
from bs4 import BeautifulSoup
from googletrans import Translator

# Функция для получения случайного английского слова и его определения
def get_english_word():
    url = "https://randomword.com/"
    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.content, "html.parser")
        english_word = soup.find("div", id="random_word").text.strip()
        word_definition = soup.find("div", id="random_word_definition").text.strip()

        # Перевод слова на русский с помощью googletrans
        try:
            translator = Translator()
            translation = translator.translate(english_word, dest="ru")
            russian_word = translation.text
        except Exception as e:
            print("Ошибка перевода:", e)
            russian_word = "Перевод недоступен"

        return {
            "english_word": english_word,
            "word_definition": word_definition,
            "russian_word": russian_word
        }
    except Exception as e:
        print("Произошла ошибка при получении слова:", e)
        return None

# Функция игры
def word_game():
    print("Добро пожаловать в игру")
    while True:
        word_dict = get_english_word()
        if not word_dict:
            print("Не удалось получить слово. Повторяем попытку...")
            continue

        word = word_dict["english_word"]
        word_definition = word_dict["word_definition"]
        russian_word = word_dict["russian_word"]

        print(f"\nЗначение слова (по-английски): {word_definition}")
        print(f"Перевод слова на русский: {russian_word}")

        user = input("Что это за слово? (по-английски): ").strip()
        if user.lower() == word.lower():
            print("Все верно!")
        else:
            print(f"Ответ неверный, было загадано это слово: {word}")

        play_again = input("Хотите сыграть еще раз? (y/n): ").strip().lower()
        if play_again != "y":
            print("Спасибо за игру!")
            break

word_game()