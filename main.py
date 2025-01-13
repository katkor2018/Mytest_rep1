
class Store:
    def __init__(self, name, address):
        self.name = name  # Название магазина
        self.address = address  # Адрес магазина
        self.items = {}  # Словарь для хранения товаров и их цен

    def add_item(self, item_name, price):

        self.items[item_name] = price
        print(f"Товар '{item_name}' добавлен с ценой {price}.")

    def remove_item(self, item_name):

        if item_name in self.items:
            del self.items[item_name]
            print(f"Товар '{item_name}' удален.")
        else:
            print(f"Товар '{item_name}' не найден.")

    def get_price(self, item_name):

        return self.items.get(item_name, None)

    def update_price(self, item_name, new_price):

        if item_name in self.items:
            self.items[item_name] = new_price
            print(f"Цена товара '{item_name}' обновлена на {new_price}.")
        else:
            print(f"Товар '{item_name}' не найден, обновление цены невозможно.")



store1 = Store("Магазин 1", "Улица 1, дом 1")
store1.add_item("яблоки", 0.5)
store1.add_item("бананы", 0.75)

store2 = Store("Магазин 2", "Улица 2, дом 2")
store2.add_item("хлеб", 1.0)
store2.add_item("молоко", 0.85)

store3 = Store("Магазин 3", "Улица 3, дом 3")
store3.add_item("сыр", 2.5)
store3.add_item("колбаса", 3.0)


print("\nТестирование методов для магазина:", store1.name)
item_name = "яблоки"
price = store1.get_price(item_name)
print(f"Цена товара '{item_name}': {price}")
store1.update_price("яблоки", 0.6)
price = store1.get_price("яблоки")
print(f"Обновленная цена товара 'яблоки': {price}")
store1.remove_item("бананы")
price = store1.get_price("бананы")
print(f"Цена удаленного товара 'бананы': {price}")

print("\nТестирование методов для магазина:", store2.name)
item_name = "молоко"
price = store2.get_price(item_name)
print(f"Цена товара '{item_name}': {price}")
store2.update_price("молоко", 0.9)
price = store2.get_price("молоко")
print(f"Обновленная цена товара 'молоко': {price}")
store2.remove_item("хлеб")
price = store2.get_price("хлеб")
print(f"Цена удаленного товара 'хлеб': {price}")


print("\nТестирование методов для магазина:", store3.name)
item_name = "сыр"
price = store3.get_price(item_name)
print(f"Цена товара '{item_name}': {price}")
store3.update_price("сыр", 3.0)
price = store3.get_price("сыр")
print(f"Обновленная цена товара 'сыр': {price}")
store3.remove_item("колбаса")
price = store3.get_price("колбаса")
print(f"Цена удаленного товара 'колбаса': {price}")