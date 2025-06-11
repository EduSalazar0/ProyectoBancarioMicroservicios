import pika
import json
import os
import logging
import time

# Configurar logging
logging.basicConfig(
    filename='consumer.log',
    level=logging.INFO,
    format='%(asctime)s %(levelname)s:%(message)s'
)

# Obtener host de RabbitMQ
rabbitmq_host = os.getenv('RABBITMQ_HOST', 'localhost')

def callback(ch, method, properties, body):
    message = json.loads(body)
    
    # Mostrar notificación en consola
    print(" Notificación recibida:")
    print(f"  Cliente ID: {message['client_id']}")
    print(f"  Monto depositado: ${message['amount']:.2f}")
    print(f"  Evento: {message['event']}")
    print("-" * 50)

    # Guardar notificación en log
    logging.info(f"Deposit notification: {message}")

def main():
    while True:
        try:
            # Conectar a RabbitMQ
            connection = pika.BlockingConnection(pika.ConnectionParameters(rabbitmq_host))
            channel = connection.channel()

            # Declarar la cola (debe coincidir con el producer)
            channel.queue_declare(queue='deposit_notifications')

            # Prefetch para control de flujo
            channel.basic_qos(prefetch_count=1)

            print(f" Conectado a RabbitMQ en '{rabbitmq_host}'.")
            print(" Esperando notificaciones de depósito... (Ctrl+C para salir)\n")

            # Consumir mensajes
            channel.basic_consume(
                queue='deposit_notifications',
                on_message_callback=callback,
                auto_ack=True
            )

            channel.start_consuming()

        except pika.exceptions.AMQPConnectionError:
            print(f" No se pudo conectar a RabbitMQ en '{rabbitmq_host}'. Reintentando en 5 segundos...")
            time.sleep(5)
        except KeyboardInterrupt:
            print(" Consumer detenido manualmente.")
            break
        except Exception as e:
            print(f" Error inesperado: {str(e)}. Reintentando en 5 segundos...")
            time.sleep(5)

if __name__ == '__main__':
    main()
