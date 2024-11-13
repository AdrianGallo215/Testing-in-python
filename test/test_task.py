import unittest
from unittest.mock import MagicMock, Mock
from src.models.task import Task, TaskList
from services.fake_database import FakeDataBase
from test.stubs import StatusStub
from services.notifier import Notifier

class TestTask(unittest.TestCase):

    def setUp(self):
        """Configura el entorno para cada prueba"""
        self.fake_db = FakeDataBase()
        self.task_list = TaskList(self.fake_db)
        self.task1 = Task(1, "Estudiar fixtures")
        self.task2 = Task(2, "Practicar fixtures")
        self.task_list.addTask(self.task1)
        self.task_list.addTask(self.task2)
        self.notifier = Notifier()
    
    def tearDown(self):
        self.task_list = None
        self.fake_db.data.clear()

    def test_mark_task_completed(self):
        # task_list = TaskList()
        # task = Task(1, "Estudiat RGR")
        # task_list.addTask(task)

        updatedTask = self.task_list.getTaskById(1)

        updatedTask.changeStatus(self.notifier, 'completada')

        self.assertEqual(updatedTask.status, "completada")

    def test_fakes_database(self):  
        # fakeDB = FakeDataBase()
        # task_list = TaskList(fakeDB)
        task3 = Task(3, "Practicar con fakes")
        

        bool = self.task_list.addTask(task3)
        result = self.task_list.getTaskInDB(3)

        self.assertEqual(bool, True)
        self.assertIsNotNone(result)
        self.assertEqual(result.title, "Practicar con fakes")

    def test_stub_status(self):
        # task = Task(1, "Entender stubs")
        # task_list = TaskList()
        # task_list.addTask(task)
        stub = StatusStub()

        updatedTask= self.task_list.getTaskById(1)

        updatedTask.changeStatus(self.notifier, "completada")

        self.assertEqual(stub.getStatus(1), self.task1.status)



if __name__ == "__main__":
    unittest.main()

