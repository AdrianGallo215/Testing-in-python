from data_structures.linked_list import LinkedList
from models.task import Task, TaskList
from services.notifier import Notifier

class User():

    roles = ["user", "admin"]
    userCount = 0

    def __init__(self, name, role="user"):
        User.increaseID()
        self.Id = User.userCount
        self.name = name
        self.role = role if role in User.roles else "user"
        self.taskList = TaskList()
        self.notifier = Notifier()

    @classmethod
    def increaseID(cls):
        cls.userCount += 1

    def assign_task(self, taskList, task_id):
        task = taskList.getTaskById(task_id)
        self.taskList.addTask(task)
        self.notify(f'Se ha asignado la tarea {task.title} a {self.name}', task_id)

    def remove_task(self, task_id):
        if self.role == "admin":
            task = self.taskList.getTaskById(task_id)
            if task:
                self.taskList.removeTask(task_id)
                self.notify(f'Se ha eliminado la tarea {task.title} a {self.name}', task_id)
            else:
                raise ValueError("Tarea no encontrada.")
        else: 
            raise ValueError("No tiene permiso para remover tareas.")

    def change_role(self, newRole):
        if self.role == "admin":
            if newRole in User.roles:
                self.role = newRole
                self.notify(f'Se ha asignado el rol {self.role} al usuario {self.name}')
            else:
                raise ValueError("Error, no existe ese rol de usuario.")
        else:
            raise ValueError("No tiene permiso para asignar roles.")

    def get_tasks(self):
        self.taskList.displayTasks()

    def notify(self, message, taskId = None):
        self.notifier.send_notification(message, taskId)