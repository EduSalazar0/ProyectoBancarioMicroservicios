import sys
import os

# Añadir el path raíz → para acceder a producer/
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

from producer.notification_producer import send_deposit_notification

class NotificationsService:
    @staticmethod
    def send_deposit_notification(message):
        send_deposit_notification(message)
