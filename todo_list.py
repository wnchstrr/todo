from task import Task


class TodoList:
    """Хранит список задач и управляет ими."""

    def __init__(self):
        """Инициализирует пустой список задач"""
        self.tasks = []

    def add_task(self, text):
        """Добавляет новую задачу в список"""
        task = Task(text)
        self.tasks.append(task)

    def delete_task(self, index):
        """Удаляет задачу из списка"""
        self.tasks.pop(index)

    def get_all_tasks(self):
        """Возвращает все задачи"""
        return self.tasks

    def get_filtered_tasks(self, is_done):
        """Фильтрует задачи по статусу выполнения"""
        return [task for task in self.tasks if task.is_done == is_done]
