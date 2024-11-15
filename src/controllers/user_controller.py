from models.user import User
from services.notifier import Notifier

class UserController:

    def __init__(self):
        self.userList = {}
        self.notifier = Notifier()
    
    def create_user(self, name, role = "user"):
        user = User(name, role)
        self.userList[user.Id] = user

    def remove_user_by_id(self, user_id):
        removed_user = self.userList.pop(user_id, None)
        if removed_user:
            print(f"Se removió al usuario {removed_user.name} con id {removed_user.Id}")
        else:
            print(f"No se encontró al usuario con id {user_id}")
        
    def get_user_by_id(self, user_id):
        return self.userList.get(user_id, None)
    
    def get_users_by_name(self, user_name):
        users = [user for user in self.userList.values() if user.name.lower() == user_name.lower()]
        if users:
            print(f'usuarios con el nombre "{user_name}": \n')
            self.display(users)
            return users
        else:
            print(f'No se han encontrado usuarios con el nombre "{user_name}".')
            return None

    def display(self, userlist):
        if isinstance(userlist, dict):
            userlist = userlist.values()
        for user in userlist:
            print(f"Id: {user.Id}\nName: {user.name}\nRole: {user.role}\n")

    def change_user_role(self, user_id, new_role):
        user = self.get_user_by_id(user_id)
        if user:
            if new_role in User.roles:
                user.role = new_role
                self.notifier.send_notification(f'Se ha asignado el rol {new_role} al usuario {user.name}')
            else:
                print("No existe el rol ingresado")
        else:
            print(f"No existe el usuario con el id {user_id}")
    
    def list_user_tasks(self, user_id):
        user = self.get_user_by_id(user_id)
        if user:
            user.get_tasks()

    def notify_user(self, user_id, msg):
        user = self.get_user_by_id(user_id)
        if user:
            user.notify(msg)
        else:
            print(f"No se encontró al usuario con id {user_id}")

    
        
            