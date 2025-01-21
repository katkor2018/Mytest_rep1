# Задание: Применение Принципа Открытости/Закрытости (Open/Closed Principle) в Разработке Простой Игры
#
# Цель: Цель этого домашнего задание - закрепить понимание и навыки применения принципа открытости/закрытости (Open/Closed Principle), одного из пяти SOLID принципов объектно-ориентированного программирования. Принцип гласит, что программные сущности (классы, модули, функции и т.д.) должны быть открыты для расширения, но закрыты для модификации.
#
# Задача: Разработать простую игру, где игрок может использовать различные типы оружия для борьбы с монстрами. Программа должна быть спроектирована таким образом, чтобы легко можно было добавлять новые типы оружия, не изменяя существующий код бойцов или механизм боя.
#
# Исходные данные:
#
# - Есть класс `Fighter`, представляющий бойца.
#
# - Есть класс `Monster`, представляющий монстра.
#
# - Игрок управляет бойцом и может выбирать для него одно из вооружений для боя.
#
# Шаг 1:Создайте абстрактный класс для оружия
#
# - Создайте абстрактный класс `Weapon`, который будет содержать абстрактный метод `attack()`.
#
# Шаг 2: Реализуйте конкретные типы оружия
#
# - Создайте несколько классов, унаследованных от `Weapon`, например, `Sword` и `Bow`. Каждый из этих классов реализует метод `attack()` своим уникальным способом.
#
# Шаг 3: Модифицируйте класс `Fighter`
#
# - Добавьте в класс `Fighter` поле, которое будет хранить объект класса `Weapon`.
#
# - Добавьте метод `change_weapon()`, который позволяет изменить оружие бойца.
#
# Шаг 4: Реализация боя
#
# - Реализуйте простой механизм для демонстрации боя между бойцом и монстром, исходя из выбранного оружия.
#
# Требования к заданию:
#
# - Код должен быть написан на Python.
#
# - Программа должна демонстрировать применение принципа открытости/закрытости: новые типы оружия можно легко добавлять, не изменяя существующие классы бойцов и механизм боя.
#
# - Программа должна выводить результат боя в консоль.
#
# Пример результата:
#
# Боец выбирает меч.
#
# Боец наносит удар мечом.
#
# Монстр побежден!
#
# Боец выбирает лук.
#
# Боец наносит удар из лука.
#
# Монстр побежден!



#Простой вариант

from abc import ABC, abstractmethod

class Weapon(ABC):

    @abstractmethod
    def attack(self):
        pass


class Sword(Weapon):

    def attack(self):
        return "Боец наносит удар мечом"

class Bow(Weapon):

    def attack(self):
        return "Боец делает выстрел из лука"


class Fighter:

    def __init__(self, weapon: Weapon):
        self.weapon = weapon

    def changeWeapon(self, weapon: Weapon):
        self.weapon = weapon

    def fight(self):
        print(self.weapon.attack())
        print("Монстр побежден!")

class Monster:

    pass

sword1 = Sword()

bow1 = Bow()

fighter = Fighter(sword1)
print("Боец выбирает меч.")
fighter.fight()

fighter.changeWeapon(bow1)
print("Боец выбирает лук.")
fighter.fight()





# с помощью нейросети

from abc import ABC, abstractmethod

# Шаг 1: Абстрактный класс для оружия
class Weapon(ABC):
    @abstractmethod
    def attack(self):
        pass

# Шаг 2: Конкретные типы оружия
class Sword(Weapon):
    def attack(self):
        return "Боец наносит удар мечом."

class Bow(Weapon):
    def attack(self):
        return "Боец наносит удар из лука."

# Класс Monster
class Monster:
    def __init__(self, name):
        self.name = name
        self.health = 100

    def take_damage(self, damage):
        self.health -= damage
        if self.health <= 0:
            return True
        return False

# Класс Fighter
class Fighter:
    def __init__(self, name):
        self.name = name
        self.weapon = None

    def change_weapon(self, weapon: Weapon):
        self.weapon = weapon

    def attack_monster(self, monster: Monster):
        if self.weapon is not None:
            print(self.weapon.attack())
            if monster.take_damage(100):  # Урон фиксированный для примера
                print(f"{monster.name} побежден!")
            else:
                print(f"{monster.name} еще жив!")
        else:
            print("У бойца нет оружия!")

# Основная программа
def main():
    # Создаем бойца и монстра
    fighter = Fighter("Воин")
    monster = Monster("Зомби")

    # Боец выбирает меч
    fighter.change_weapon(Sword())
    print(f"{fighter.name} выбирает меч.")
    fighter.attack_monster(monster)

    # Проверка состояния монстра
    print()

    # Боец выбирает лук
    fighter.change_weapon(Bow())
    print(f"{fighter.name} выбирает лук.")
    fighter.attack_monster(monster)

if __name__ == "__main__":
    main()