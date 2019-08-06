import pika
import sys
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

message = ' '.join(sys.argv[1:]) or "Hello World!"

channel.queue_declare(queue='sample_taskQueue', durable)
channel.basic_publish(exchange='',
                      routing_key='sample_taskQueue',
                      body=message)
print(" [x] Sent %r" % message)