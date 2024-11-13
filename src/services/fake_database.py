class FakeDataBase:
    def __init__(self):
         self.data = {}

    def saveTask(self, task):
         self.data[task.id] = task
         return True
    
    def getTask(self, task_id):
         return self.data.get(task_id, None)