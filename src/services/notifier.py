

class Notifier:
    def __init__(self):
        self.url = "https://api.sendgrid.com/v3/mail/send"

    def send_notification(self, message, task_id=None ):

        if(task_id):
            print(f"\nEnviando notificación para la tarea {task_id}: {message}")
        else:
            print(message)

