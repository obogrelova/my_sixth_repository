from datetime import datetime


class Task:
    def _init_(self, description, deadline):
        self.description = description
        self.deadline = deadline
        self.completed = False

    def mark_as_completed(self):
        self.completed = True

    def _str_(self):
        status = "Выполнено" if self.completed else "Не выполнено"
        return f"Задача: {self.description}, Срок: {self.deadline}, Статус: {status}"



class TaskManager:
    def _init_(self):
        self.tasks = []

    def add_task(self, description, deadline):
        task = Task(description, deadline)
        self.tasks.append(task)

    def mark_task_as_completed(self, task_index):
        if o <= task_index < len(self.tasks):
            self.tasks[task_index].mark_as_completed()

    def get_current_tasks(self):
        return [task for task in self.tasks if not task.completed]

    def show_tasks(self):
        for i, task in enumerate(self.tasks):
            print(f"{i + 1}. {task}")
