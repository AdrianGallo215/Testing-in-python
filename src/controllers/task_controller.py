from models.task import Task, TaskList
from models.user import User
from services.notifier import Notifier

class TaskController:

    def __init__(self, database = None):
        self.taskList = TaskList(database)
        self.notifier = Notifier()

    def create_task(self, title, description=None, priority = "baja", tag="general"):
        newTask = Task(self.taskList.taskCount()+1, title, description, "pendiente", priority, tag)
        self.taskList.addTask(newTask)
        return newTask
    
    def edit_task(self, task_id, attr, val):
        try:
            self.taskList.editTask(task_id, attr, val)
        except ValueError as e:
            print(f"Error al editar la tarea: {e}")
        
    def assign_task_to_user(self, task_id, user):
        try:
            user.assign_task(self.taskList, task_id)
        except ValueError as e:
            print(f"Error al asignar tarea: {e}")
        
    def list_task_by_tag(self, tag):
        print(f"Tareas con la etiqueta {tag}: ")
        self.taskList.getTasksByTag(tag)
    
    def list_task_by_priority(self, pri):
        print(f"Tareas con prioridad {pri}: ")
        self.taskList.getTasksByPriority(pri)

    def list_task_by_status(self, sts):
        print(f"Tareas con el estado {sts}: ")
        self.taskList.getTasksByStatus(sts)

    def remove_task(self, task_id):
        self.taskList.removeTask(task_id)

    def list_all_task(self):
        print("Todas las tareas: ")
        self.taskList.display()