import pika
import sys

connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
channel = connection.channel()

channel.exchange_declare(exchange='direct_logs', exchange_type='direct')

result = channel.queue_declare(queue='', exclusive=True)
queue_name = result.method.queue

log_types = sys.argv[1:]

if not log_types:
    sys.stderr.write("Usage: %s [info] [error] [warning]\n" %sys.argv[0])
    sys.exit(1)

for log_type in log_types:
    channel.queue_bind(exchange='direct_logs', routing_key=log_type, queue=queue_name)

print("[*] Waiting for logs. To exit press Ctrl+C")

def callback(ch, method, properties, body):
    print(" [x] %r:%r" % (method.routing_key, body))


channel.basic_consume(queue=queue_name, on_message_callback=callback, auto_ack=True)

channel.start_consuming()
