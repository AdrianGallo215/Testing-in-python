Feature: Gestion de tareas
    Scenario: Añadir una nueva tarea
        Given Una lista de tareas vacía
        When Añado una nueva tarea con id 4, título "Estudiar Python" y estado "Completado"
        Then La lista debe tener 1 tarea
        And La tarea debe tener el título "Estudiar Python" y estado "Completado"