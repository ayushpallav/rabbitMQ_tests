import pika
import sys

connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
channel = connection.channel()

channel.exchange_declare(exchange='direct_logs', exchange_type='direct')

# result = channel.queue_declare(queue='', exclusive=True)
# queue_name = result.method.queue

type_of_log = sys.argv[1] if len(sys.argv)>1 else 'info'

message = ''.join(sys.argv[2:]) or 'Default Message'

channel.basic_publish(exchange='direct_logs', routing_key=type_of_log, body=message)
print("[X] Sent %r : %r" %(type_of_log,message))
