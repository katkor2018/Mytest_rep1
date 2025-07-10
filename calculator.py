# Ввод двух чисел пользователем
a = float(input("Введите первое число: "))
b = float(input("Введите второе число: "))

print("Сумма:", a + b)
print("Разность:", a - b)
print("Произведение:", a * b)

if b != 0:
    print("Деление:", a / b)
    print("Целая часть от деления:", a // b)
    print("Остаток от деления:", a % b)
else:
    print("Деление: Нельзя делить на ноль")
    print("Целая часть от деления: Нельзя делить на ноль")
    print("Остаток от деления: Нельзя делить на ноль")

print("Возведение в степень:", a ** b)

while True:
    user_input = input('Введите выражение (например, 2 + 2) или "выход" для завершения: ')
    if user_input.lower() == 'выход':
        print("Программа завершена.")
        break

    parts = user_input.split()
    if len(parts) != 3:
        print("Ошибка: введите выражение в формате 'число операция число'")
        continue

    num1, op, num2 = parts

    try:
        num1 = float(num1)
        num2 = float(num2)
    except ValueError:
        print("Ошибка: введите корректные числа.")
        continue

    if op == '+':
        result = num1 + num2
    elif op == '-':
        result = num1 - num2
    elif op == '*':
        result = num1 * num2
    elif op == '/':
        if num2 == 0:
            print("Ошибка: деление на ноль!")
            continue
        result = num1 / num2
    else:
        print("Ошибка: неизвестная операция.")
        continue

    print("Результат:", result)