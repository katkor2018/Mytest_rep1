from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

def main():
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    driver = webdriver.Chrome(options=options)
    driver.implicitly_wait(3)
    try:
        driver.get('https://ru.wikipedia.org')
        driver.find_element(By.NAME, 'search').send_keys(input('Запрос: ') + Keys.RETURN)
        while True:
            print("\n1. Параграфы\n2. Связанные страницы\n3. Выход")
            choice = input("Ваш выбор: ")
            if choice == '1':
                paragraphs = [p.text for p in driver.find_elements(By.CSS_SELECTOR, '#mw-content-text p') if p.text.strip()]
                for i, p in enumerate(paragraphs, 1):
                    print(f"\nПараграф {i}:\n{p}")
                    if i != len(paragraphs):
                        if input("Enter - далее, q - выход: ").lower() == 'q': break
            elif choice == '2':
                links = [(a.text, a.get_attribute('href')) for a in driver.find_elements(By.CSS_SELECTOR, '#mw-content-text a')
                         if a.get_attribute('href') and '/wiki/' in a.get_attribute('href') and ':' not in a.get_attribute('href').split('/wiki/')[1] and a.text]
                shown = []
                for text, href in links:
                    if href not in shown:
                        print(f"{len(shown)+1}. {text}")
                        shown.append(href)
                    if len(shown) == 10: break
                sel = input("Номер для перехода или Enter для отмены: ")
                if sel.isdigit() and 1 <= int(sel) <= len(shown):
                    driver.get(shown[int(sel)-1])
            elif choice == '3':
                break
            else:
                print("Некорректный выбор.")
    except Exception as e:
        print(f"Произошла ошибка: {e}")
    finally:
        driver.quit()

if __name__ == '__main__':
    main()