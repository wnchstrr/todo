import json
from pathlib import Path

from task import Task


class JsonStorage:

    def __init__(self, filename):
        self.filename = Path(filename)

    def save(self, tasks):
        data = [{"text": task.text, "is_done": task.is_done} for task in tasks]
        with open(self.filename, "w") as f:
            json.dump(data, f)

    def load(self):
        if not self.filename.exists():
            return []
        with open(self.filename, "r") as f:
            data = json.load(f)
        return [Task(text=d["text"], is_done=d["is_done"]) for d in data]
