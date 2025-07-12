import csv
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
url = "https://tomsk.hh.ru/vacancies/programmist"
driver.get(url)
time.sleep(3)

# Пример корректного поиска карточек вакансий с помощью CSS-селектора:
vacancies = driver.find_elements(By.CSS_SELECTOR, 'div.serp-item')  # Обычно на hh.ru у карточки класс serp-item

print(vacancies)
parsed_data = []

for vacancy in vacancies:
    try:
        # Название вакансии
        title = vacancy.find_element(By.CSS_SELECTOR, 'a.serp-item__title').text
        # Компания
        company = vacancy.find_element(By.CSS_SELECTOR, 'a[rel="nofollow"]').text
        # Зарплата (может отсутствовать!)
        try:
            salary = vacancy.find_element(By.CSS_SELECTOR, 'span.bloko-header-section-2').text
        except:
            salary = 'Не указано'
        # Ссылка
        link = vacancy.find_element(By.CSS_SELECTOR, 'a.serp-item__title').get_attribute('href')
        # Добавляем только если не возникло ошибок выше
        parsed_data.append([title, company, salary, link])
    except Exception as e:
        print("произошла ошибка при парсинге", e)
        continue

driver.quit()

with open("hh.csv", 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['Название вакансии', 'Название компании', 'Зарплата', 'Ссылка на вакансию'])
    writer.writerows(parsed_data)