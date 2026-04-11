class Task:
    """Представляет задачу с текстом и статусом выполнения"""

    def __init__(self, text, is_done=False):
        """Инициализирует атрибуты текста и выполнения задачи"""
        self.text = text
        self.is_done = is_done

    def mark_done(self):
        """Отмечает задачу выполненной"""
        self.is_done = True

    def __repr__(self):
        return f"Task(text={self.text!r}, is_done={self.is_done})"
