def show_menu():
    """Показывает меню"""
    print("0. Выход")
    print("1. Добавить задачу")
    print("2. Удалить задачу")
    print("3. Отметить задачу выполненной")
    print("4. Показать список задач")
    print("5. Отфильтровать по статусу")


def get_choice():
    """Принимает выбор пользователя"""
    return input("Выбери пункт из меню: ")


def show_tasks(tasks):
    """Выводит список задач"""
    if not tasks:
        print("Задач нет :(")
        return
    for index, task in enumerate(tasks, start=1):
        status = "✓" if task.is_done else "✗"
        print(f"{index}. [{status}] {task.text}")
