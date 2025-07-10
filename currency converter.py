# Ввод курса доллара к рублю
rate = float(input("Введите курс 1 USD в RUB: "))

# Выбор направления конвертации
direction = input("Выберите направление конвертации (1 - USD в RUB, 2 - RUB в USD): ")

if direction == '1':
    usd = float(input("Введите сумму в USD: "))
    rub = usd * rate
    print(f"{usd} USD = {rub} RUB")
elif direction == '2':
    rub = float(input("Введите сумму в RUB: "))
    usd = rub / rate
    print(f"{rub} RUB = {usd} USD")
else:
    print("Ошибка: выбрано неверное направление конвертации.")