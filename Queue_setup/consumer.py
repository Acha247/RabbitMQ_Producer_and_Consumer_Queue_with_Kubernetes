
import pika
connection = pika.BlockingConnection(pika.ConnectionParameters('44.211.169.61', 5672, '/', pika.PlainCredentials("admin", "password")))
channel = connection.channel()

def callback(ch, method, properties, body):
    print(f'{body} is received')

channel.basic_consume(queue="my_app", on_message_callback=callback, auto_ack=True)
channel.start_consuming()
