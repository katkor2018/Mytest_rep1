import requests
from bs4 import BeautifulSoup
from translate import Translator  # pip install translate

# Функция для получения случайного английского слова и его определения
def get_english_word():
    url = "https://randomword.com/"
    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.content, "html.parser")
        english_word = soup.find("div", id="random_word").text.strip()
        word_definition = soup.find("div", id="random_word_definition").text.strip()

        # Перевод ОПРЕДЕЛЕНИЯ на русский
        try:
            translator = Translator(to_lang="ru", from_lang="en")
            russian_definition = translator.translate(word_definition)
        except Exception as e:
            print("Ошибка перевода определения:", e)
            russian_definition = "Перевод недоступен"

        # Перевод СЛОВА на русский
        try:
            translator_word = Translator(to_lang="ru", from_lang="en")
            russian_word = translator_word.translate(english_word)
        except Exception as e:
            print("Ошибка перевода слова:", e)
            russian_word = None

        return {
            "english_word": english_word,
            "russian_word": russian_word.strip().lower() if russian_word else "",
            "word_definition": word_definition,
            "russian_definition": russian_definition
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

        word = word_dict["english_word"].strip().lower()
        russian_word = word_dict["russian_word"].strip().lower()
        word_definition = word_dict["word_definition"]
        russian_definition = word_dict["russian_definition"]

        print(f"\nЗначение слова (по-английски): {word_definition}")
        print(f"Перевод значения слова на русский: {russian_definition}")

        user = input("Что это за слово? (по-английски или по-русски): ").strip().lower()
        if user == word or user == russian_word:
            print("Все верно!")
        else:
            print(f"Ответ неверный. Было загадано это слово: {word} ({russian_word})")

        play_again = input("Хотите сыграть еще раз? (y/n): ").strip().lower()
        if play_again != "y":
            print("Спасибо за игру!")
            break

word_game()