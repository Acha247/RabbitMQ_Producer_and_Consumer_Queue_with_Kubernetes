import pika

connection = pika.BlockingConnection(pika.ConnectionParameters('44.211.169.61', 5672, '/', pika.PlainCredentials('admin', 'password')))
channel = connection.channel()

channel.basic_publish(exchange='my_exchange', routing_key='test', body='Test!')

connection.close()

