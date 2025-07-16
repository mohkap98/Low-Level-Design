from abc import ABC, abstractmethod

# Abstract base class for notifications
class NotificationService(ABC):
    def __init__(self, type) -> None:
        self.type = type.lower()
    
    def get_type(self):
        return self.type
    
    @abstractmethod
    def send(self):
        pass

# Concrete notification types
class EmailNotification(NotificationService):
    def send(self):
        print(f"Sending notification via {self.type}")

class SMSNotification(NotificationService):
    def send(self):
        print(f"Sending notification via {self.type}")

class PushNotification(NotificationService):
    def send(self):
        print(f"Sending notification via {self.type}")

# Factory to create and send notifications
class NotificationFactory:
    @staticmethod
    def createNotificationService(type: str):
        type = type.lower()
        if type == "email":
            return EmailNotification(type)
        elif type == "sms":
            return SMSNotification(type)
        elif type == "push":
            return PushNotification(type)
        else:
            raise ValueError("Invalid notification type")
    
    @staticmethod
    def sendNotification(type: str):
        notifier = NotificationFactory.createNotificationService(type)
        notifier.send()

# ✅ Client code
NotificationFactory.sendNotification("push")
