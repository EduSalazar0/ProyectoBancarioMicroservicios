# producer/notification_producer.py

import pika
import json
import os

def send_deposit_notification(message):
    # Determinar el host (en Docker será 'rabbitmq', en local será 'localhost')
    rabbitmq_host = os.getenv('RABBITMQ_HOST', 'localhost')

    try:
        # Conexión a RabbitMQ
        connection = pika.BlockingConnection(pika.ConnectionParameters(rabbitmq_host))
        channel = connection.channel()

        # Declarar la cola (idempotente: si ya existe no pasa nada)
        channel.queue_declare(queue='deposit_notifications')

        # Enviar el mensaje (como JSON)
        channel.basic_publish(
            exchange='',
            routing_key='deposit_notifications',
            body=json.dumps(message)
        )

        print(f"Notificación enviada: {message}")

    except pika.exceptions.AMQPConnectionError:
        print("Error: No se pudo conectar a RabbitMQ.")

    finally:
        if 'connection' in locals() and connection.is_open:
            connection.close()
