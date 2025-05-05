import json
import os
from models.task import Task

class TaskManager:
    def __init__(self, filepath='data/tasks.json'):
        self.filepath = filepath
        self.tasks = []
        self.load_tasks()

    def add_task(self, title, description=''):
        self.tasks.append(Task(title, description))
        self.save_tasks()

    def delete_task(self, index):
        if 0 <= index < len(self.tasks):
            del self.tasks[index]
            self.save_tasks()

    def complete_task(self, index):
        if 0 <= index < len(self.tasks):
            self.tasks[index].completed = True
            self.save_tasks()

    def load_tasks(self):
        if os.path.exists(self.filepath):
            with open(self.filepath, 'r') as f:
                data = json.load(f)
                self.tasks = [Task.from_dict(d) for d in data]

    def save_tasks(self):
        with open(self.filepath, 'w') as f:
            json.dump([task.to_dict() for task in self.tasks], f, indent=3)

    def get_tasks(self):
        return self.tasks
