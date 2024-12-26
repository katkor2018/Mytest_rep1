
def collect_user_data():
    print("Заполните анкету:")

    # Сбор данных
    name = input("Введите ваше имя: ")
    age = input("Введите ваш возраст: ")
    residence = input("Введите место жительства: ")
    marital_status = input("Введите семейное положение (неженат/незамужем, женат/замужем, в разводе, вдовец/вдова): ")
    profession = input("Введите вашу профессию: ")


    return {
        "Имя": name,
        "Возраст": age,
        "Место жительства": residence,
        "Семейное положение": marital_status,
        "Профессия": profession
    }

user_data = collect_user_data()

print("\nСпасибо за заполнение анкеты!")
for key, value in user_data.items():
    print(f"{key}: {value}")