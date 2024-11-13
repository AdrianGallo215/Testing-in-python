from behave import given, when, then
from src.models.task import Task, TaskList

@given("Una lista de tareas vacía")
def step_given_empty_task_list(context):
    context.task_list = TaskList()

@when('Añado una nueva tarea con id {id:d}, título "{title}" y estado "{status}"')
def step_when_add_new_task(context, id, title, status):
    task = Task(id, title, status=status)
    context.task_list.addTask(task)

@then("La lista debe tener {count:d} tarea")
def step_then_check_task_count(context, count):
    print(context.task_list.taskCount())
    print(count)
    assert context.task_list.taskCount() == count

@then('la tarea debe tener el título "{title}" y estado "{status}"')
def step_then_check_task_details(context, title, status):
    task = context.task_list.getTaskById(4)
    assert task.title == title
    assert task.status == status