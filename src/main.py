from controllers.task_controller import TaskController
from controllers.user_controller import UserController
from utils.file_manager import FileManager

def mostrar_menu_principal():
    print("\n=====================")
    print("   MENÚ PRINCIPAL")
    print("=====================")
    print("1. Gestión de Tareas")
    print("2. Gestión de Usuarios")
    print("3. Exportar Datos")
    print("0. Salir")
    return input("Selecciona una opción: ")

def mostrar_menu_tareas():
    print("\n--- Gestión de Tareas ---")
    print("1. Crear Tarea")
    print("2. Listar Tareas")
    print("3. Editar Tarea")
    print("4. Eliminar Tarea")
    print("5. Filtrar Tareas por Etiqueta")
    print("6. Filtrar Tareas por Prioridad")
    print("7. Filtrar Tareas por Estado")
    print("0. Volver al Menú Principal")
    return input("Selecciona una opción: ")

def mostrar_menu_usuarios():
    print("\n--- Gestión de Usuarios ---")
    print("1. Crear Usuario")
    print("2. Listar Usuarios")
    print("3. Asignar Tarea a Usuario")
    print("4. Eliminar Usuario")
    print("5. Cambiar Rol de Usuario")
    print("6. Mostrar Tareas de un Usuario")
    print("0. Volver al Menú Principal")
    return input("Selecciona una opción: ")

def mostrar_menu_exportar():
    print("\n--- Exportar Datos ---")
    print("1. Exportar Tareas a CSV")
    print("2. Exportar Usuarios a JSON")
    print("0. Volver al Menú Principal")
    return input("Selecciona una opción: ")

def menu_gestion_tareas(task_controller):
    while True:
        opcion = mostrar_menu_tareas()
        if opcion == "1":
            titulo = input("Título de la tarea: ")
            descripcion = input("Descripción: ")
            prioridad = input("Prioridad (baja, media, alta, urgente, atrasada): ")
            tag = input("Etiqueta: ")
            task_controller.create_task(titulo, descripcion, prioridad, tag)
        elif opcion == "2":
            task_controller.list_all_task()
        elif opcion == "3":
            task_id = int(input("ID de la tarea a editar: "))
            attr = input("Atributo (status, priority, tag): ")
            value = input(f"Nuevo valor para {attr}: ")
            task_controller.edit_task(task_id, attr, value)
        elif opcion == "4":
            task_id = int(input("ID de la tarea a eliminar: "))
            task_controller.remove_task(task_id)
        elif opcion == "5":
            tag = input("Etiqueta: ")
            task_controller.list_task_by_tag(tag)
        elif opcion == "6":
            priority = input("Prioridad: ")
            task_controller.list_task_by_priority(priority)
        elif opcion == "7":
            status = input("Estado: ")
            task_controller.list_task_by_status(status)
        elif opcion == "0":
            break
        else:
            print("Opción no válida.")

def menu_gestion_usuarios(user_controller, task_controller):
    while True:
        opcion = mostrar_menu_usuarios()
        if opcion == "1":
            nombre = input("Nombre del usuario: ")
            role = input("Rol (user/admin): ")
            user_controller.create_user(nombre, role)
        elif opcion == "2":
            user_controller.display(user_controller.userList)
        elif opcion == "3":
            user_id = int(input("ID del usuario: "))
            task_id = int(input("ID de la tarea: "))
            user = user_controller.get_user_by_id(user_id)
            if user:
                task_controller.assign_task_to_user(task_id, user)
        elif opcion == "4":
            user_id = int(input("ID del usuario a eliminar: "))
            user_controller.remove_user_by_id(user_id)
        elif opcion == "5":
            user_id = int(input("ID del usuario: "))
            new_role = input("Nuevo rol (user/admin): ")
            user_controller.change_user_role(user_id, new_role)
        elif opcion == "6":
            user_id = int(input("ID del usuario: "))
            user_controller.list_user_tasks(user_id)
        elif opcion == "0":
            break
        else:
            print("Opción no válida.")

def menu_exportar(task_controller, user_controller):
    while True:
        opcion = mostrar_menu_exportar()
        if opcion == "1":
            tasks = task_controller.taskList.get_all_tasks()
            FileManager.export_csv(tasks, "tareas.csv")
            print("Tareas exportadas a tareas.csv")
        elif opcion == "2":
            users = user_controller.userList
            FileManager.export_json(users, "usuarios.json")
            print("Usuarios exportados a usuarios.json")
        elif opcion == "0":
            break
        else:
            print("Opción no válida.")

def main():
    task_controller = TaskController()
    user_controller = UserController()

    while True:
        opcion = mostrar_menu_principal()
        if opcion == "1":
            menu_gestion_tareas(task_controller)
        elif opcion == "2":
            menu_gestion_usuarios(user_controller, task_controller)
        elif opcion == "3":
            menu_exportar(task_controller, user_controller)
        elif opcion == "0":
            print("¡Gracias por usar la aplicación! Hasta luego.")
            break
        else:
            print("Opción no válida.")

if __name__ == "__main__":
    main()
