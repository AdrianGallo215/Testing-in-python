from data_structures.node import Node
from data_structures.linked_list import LinkedList
from services.notifier import Notifier
from services.fake_database import FakeDataBase 
from services.tag_manager import load_tags, add_tag

class Task:

    tags = load_tags()
    priorityList = ["baja", "media", "alta", "urgente", "atrasada"]
    statusList = ["pendiente", "en curso", "completada", "postpuesta", "cancelada"]

    def __init__(self, id, title, description=None, status="pendiente", priority = "baja", tag="general"):
        self.id = id
        self.title = title
        self.description = description
        self.status = status if status in Task.statusList else "pendiente"
        self.priority = priority if priority in Task.priorityList else "baja"
        self.tag = tag if tag in Task.tags else "general"

    def changeStatus(self, notifier, newStatus):

        if newStatus in self.statusList:
            notifier.send_notification(f'La tarea "{self.title}" cambió de estado "{self.status}" a "{newStatus}".')
            self.status = newStatus
        else:
            raise ValueError("Error, el estado ingresado no existe")

    def changePriority(self, newPriority, notifier):

        if newPriority in self.priorityList:
            notifier.send_notification(f'La tarea "{self.title}" cambió de prioridad "{self.priority}" a "{newPriority}".')
            self.priority = newPriority
        else:
            raise ValueError("Error, la prioridad ingresada no existe")

    def changeTag(self, newTag, notifier):
        if newTag in Task.tags:
            notifier.send_notification(f'La tarea "{self.title}" cambió de etiqueta "{self.priority}" a "{newTag}".')
            self.tag = newTag
        else:
            raise ValueError(f'Error, la etiqueta ingresada no existe.')


    @classmethod
    def createTag(cls, newTag):
        if newTag not in cls.tags:
            add_tag(newTag)

    def __str__(self):
        return (f"{'-'*15}\n"
                f"Tarea {self.id}\n"
                f"{self.title}\n"
                f"Desc: "
                f"{self.description}\n"
                f"Estado: "
                f"{self.status}\n"
                f"{'-'*15}")
    
class TaskList(LinkedList):


    def __init__(self, database = None):
        super().__init__()
        self.database = database if database else FakeDataBase()

    def addTask(self, task):
        node = Node(task)
        super().add(node)
        return self.database.saveTask(task)


    def removeTask(self, task_id):
        prev = None
        current = self.head

        while current:
            if current.data.id == task_id:
                if prev:
                    prev.next = current.next                   
                else:
                    self.head = current.next
                return print(f"Tarea {current.data.title} eliminada con éxito.")
            
            prev = current
            current = current.next
        return print(f"No se ha encontrado la tarea {task_id}.")

    def getTaskById(self, task_id):
        current = self.head

        while current:
            if current.data.id == task_id:
                return current.data
            current = current.next
            
        return None
    
    def getTaskInDB(self, task_id):
        return self.database.getTask(task_id)

    def editTask(self, task_id, attr, value):
        task = self.getTaskById(task_id)
        notifier = Notifier()

        actions = {"status" : task.changeStatus, "priority": task.changePriority, "tag":task.changeTag}

        if(attr in actions):
            actions[attr](value, notifier)
        else:
            raise ValueError("Error, solo puede modificar el estado, prioridad y etiqueta de la tareas.")
        
    def getTasksByTag(self, tag):
        current = self.head
        tagLinkedList = LinkedList()

        while current:
            if(current.data.tag == tag):
                tagLinkedList.add(current)
            current = current.next
        
        print(f"Mostrando {tagLinkedList.len()} tareas")
        tagLinkedList.display()

    def getTasksByPriority(self, priority):
        current = self.head
        priorityLinkedList = LinkedList()

        while current:
            if(current.data.priority == priority):
                priorityLinkedList.add(current)
            current = current.next
        
        print(f"Mostrando {priorityLinkedList.len()} tareas")
        priorityLinkedList.display()

    def getTasksByStatus(self, status):
        current = self.head
        statusLinkedList = LinkedList()

        while current:
            if(current.data.status == status):
                statusLinkedList.add(current)
            current = current.next
        
        print(f"Mostrando {statusLinkedList.len()} tareas")
        statusLinkedList.display()


    def displayTasks(self):
        if self.head:
            super().display()
        else:
            print("No existen tareas para esta lista")

    def taskCount(self):
        return super().len()

    
        