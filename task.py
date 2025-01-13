class Task:
    def __init__(self, description, due_date):
        self.description = description
        self.due_date = due_date
        self.completed = False

    def mark_as_completed(self):
        self.completed = True

    def __str__(self):
        status = "Выполнено" if self.completed else "Не выполнено"
        return f"Задача: {self.description}, Срок: {self.due_date}, Статус: {status}"


class TaskManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, description, due_date):
        new_task = Task(description, due_date)
        self.tasks.append(new_task)

    def mark_task_as_completed(self, task_index):
        if 0 <= task_index < len(self.tasks):
            self.tasks[task_index].mark_as_completed()
        else:
            print("Ошибка: Индекс задачи вне диапазона.")

    def get_current_tasks(self):
        return [task for task in self.tasks if not task.completed]

    def show_tasks(self):
        for index, task in enumerate(self.tasks):
            print(f"{index}. {task}")


# Пример использования
if __name__ == "__main__":
    manager = TaskManager()

    manager.add_task("Написать отчет", "2023-10-01")
    manager.add_task("Подготовить презентацию", "2023-10-05")
    manager.add_task("Провести встречу", "2023-10-10")

    print("Список всех задач:")
    manager.show_tasks()

    print("\nОтмечаем первую задачу как выполненную...")
    manager.mark_task_as_completed(0)

    print("\nСписок всех задач после обновления:")
    manager.show_tasks()

    print("\nТекущие (не выполненные) задачи:")
    current_tasks = manager.get_current_tasks()
    for task in current_tasks:
        print(task)