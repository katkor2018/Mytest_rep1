class User:
    def __init__(self, user_id, name):
        self.__user_id = user_id
        self.__name = name
        self.__access_level = "пользователь"

    def get_user_id(self):
        return self.__user_id

    def get_name(self):
        return self.__name

    def get_access_level(self):
        return self.__access_level

    def set_name(self, name):
        self.__name = name


class Admin(User):
    def __init__(self, user_id, name):
        super().__init__(user_id, name)
        self.__access_level = "администратор"  # уровень доступа для администраторов
        self.__users = []  # список пользователей

    def add_user(self, user):
        if isinstance(user, User):
            self.__users.append(user)
            print(f"Пользователь {user.get_name()} добавлен.")
        else:
            print("Только пользователи могут быть добавлены.")

    def remove_user(self, user_id):
        for user in self.__users:
            if user.get_user_id() == user_id:
                self.__users.remove(user)
                print(f"Пользователь {user.get_name()} удален.")
                return
        print("Пользователь не найден.")

    def list_users(self):
        if not self.__users:
            print("Пользователи не найдены.")
            return
        print("Список пользователей:")
        for user in self.__users:
            print(f"ID: {user.get_user_id()}, Name: {user.get_name()}, Access Level: {user.get_access_level()}")


# Пример использования
if __name__ == "__main__":
    admin = Admin(1, "Aдминистратор")

    user1 = User(2,"Мария" )
    user2 = User(3, "Сергей")

    admin.add_user(user1)
    admin.add_user(user2)

    admin.list_users()

    admin.remove_user(2)
    admin.list_users()