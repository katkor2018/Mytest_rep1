# Запрашиваем у пользователя длину и ширину прямоугольника
length_input = input("Введите длину прямоугольника: ")
width_input = input("Введите ширину прямоугольника: ")

# Преобразуем введённые значения в числа с плавающей точкой
try:
    length = float(length_input)
    width = float(width_input)
    area = length * width
    print("Площадь прямоугольника:", area)
except ValueError:
    print("Ошибка: введите числовые значения для длины и ширины.")