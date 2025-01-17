import json


class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def make_sound(self):
        raise NotImplementedError("Subclasses should implement this method")

    def eat(self):
        return f"{self.name} is eating."


class Bird(Animal):
    def make_sound(self):
        return f"{self.name} says chirp!"


class Mammal(Animal):
    def make_sound(self):
        return f"{self.name} says roar!"


class Reptile(Animal):
    def make_sound(self):
        return f"{self.name} says hiss!"


def animal_sound(animals):
    for animal in animals:
        print(animal.make_sound())


class Employee:
    def __init__(self, name):  # Исправлено init на __init__
        self.name = name


class ZooKeeper(Employee):
    def feed_animal(self, animal):
        return f"{self.name} is feeding {animal.name}."


class Veterinarian(Employee):
    def heal_animal(self, animal):
        return f"{self.name} is healing {animal.name}."


class Zoo:
    def __init__(self):  
        self.animals = []
        self.employees = []

    def add_animal(self, animal):
        self.animals.append(animal)

    def add_employee(self, employee):
        self.employees.append(employee)

    def save_to_file(self, filename):
        data = {
            'animals': [{'name': animal.name, 'age': animal.age, 'type': type(animal).__name__} for animal in self.animals],
            'employees': [{'name': employee.name, 'type': type(employee).__name__} for employee in self.employees]
        }
        with open(filename, 'w') as f:
            json.dump(data, f)

    def load_from_file(self, filename):
        with open(filename, 'r') as f:
            data = json.load(f)
            for animal_data in data['animals']:
                if animal_data['type'] == 'Bird':
                    animal = Bird(animal_data['name'], animal_data['age'])
                elif animal_data['type'] == 'Mammal':
                    animal = Mammal(animal_data['name'], animal_data['age'])
                elif animal_data['type'] == 'Reptile':
                    animal = Reptile(animal_data['name'], animal_data['age'])
                self.add_animal(animal)

            for employee_data in data['employees']:
                if employee_data['type'] == 'ZooKeeper':
                    employee = ZooKeeper(employee_data['name'])
                elif employee_data['type'] == 'Veterinarian':
                    employee = Veterinarian(employee_data['name'])
                self.add_employee(employee)


# Пример использования
if __name__ == '__main__':  # Исправлено name на __name
    zoo = Zoo()

    # Создаем животных
    parrot = Bird("Polly", 2)
    lion = Mammal("Leo", 5)
    snake = Reptile("Slithery", 3)

    # Добавляем животных в зоопарк
    zoo.add_animal(parrot)
    zoo.add_animal(lion)
    zoo.add_animal(snake)

    # Создаем сотрудников
    zookeeper = ZooKeeper("John")
    veterinarian = Veterinarian("Dr. Smith")

    # Добавляем сотрудников в зоопарк
    zoo.add_employee(zookeeper)
    zoo.add_employee(veterinarian)

    # Вызываем звуки животных
    animal_sound(zoo.animals)

    # Пример кормления и лечения животных
    print(zookeeper.feed_animal(parrot))
    print(veterinarian.heal_animal(lion))

    # Сохраняем состояние зоопарка в файл
    zoo.save_to_file('zoo_data.json')

    # Загружаем состояние зоопарка из файла
    new_zoo = Zoo()
    new_zoo.load_from_file('zoo_data.json')
    animal_sound(new_zoo.animals)