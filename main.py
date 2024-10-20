from datetime import datetime


class Task:
    def __init__(self, description, deadline):
        self.description = description
        self.deadline = deadline
        self.completed = False

    def mark_as_completed(self):
        self.completed = True

    def __str__(self):
        status = "Выполнено" if self.completed else "Не выполнено"
        return f"Задача: {self.description}, Срок: {self.deadline}, Статус: {status}"



class TaskManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, description, deadline):
        task = Task(description, deadline)
        self.tasks.append(task)

    def mark_task_as_completed(self, task_index):
        if 0 <= task_index < len(self.tasks):
            self.tasks[task_index].mark_as_completed()

    def get_current_tasks(self):
        return [task for task in self.tasks if not task.completed]

    def show_tasks(self):
        for i, task in enumerate(self.tasks):
            print(f"{i + 1}. {task}")



task_manager = TaskManager()

task_manager.add_task("Купить продукты", datetime(2024, 10, 19))
task_manager.add_task("Написать отчет", datetime(2024, 10, 22))

task_manager.mark_task_as_completed(0)

print("Все задачи:")
task_manager.show_tasks()

print("\nТекущие задачи:")
for task in task_manager.get_current_tasks():
    print(task)