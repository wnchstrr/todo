from todo_list import TodoList
from ui import show_menu, get_choice, show_tasks


def main():
    todo_list = TodoList()
    while True:
        print()
        show_menu()
        answer = get_choice()
        if answer == '0':
            print("До свиданья.")
            break
        elif answer == '1':
            text = input("Введите задачу: ")
            todo_list.add_task(text)
            print("\nЗадача успешно добавлена:")
            show_tasks(todo_list.get_all_tasks())
        elif answer == '2':
            show_tasks(todo_list.get_all_tasks())
            index = int(input("Введите номер задачи: ")) - 1
            todo_list.delete_task(index)
            print("\nЗадача успешно удалена ✓")
        elif answer == '3':
            show_tasks(todo_list.get_all_tasks())
            index = int(input("Введите номер задачи: ")) - 1
            task = todo_list.tasks[index]
            task.mark_done()
            print(f"«{task.text}» ✓\nЗадача выполнена")
        elif answer == '4':
            show_tasks(todo_list.tasks)
        elif answer == '5':
            status = input("Показать выполненные? y/n: ")
            is_done = status == 'y'
            show_tasks(todo_list.get_filtered_tasks(is_done))


if __name__ == '__main__':
    main()
