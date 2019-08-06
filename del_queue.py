import pika
import sys

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

name = ' '.join(sys.argv[1:]) or ''
if name != '':
    channel.queue_delete(queue=name)
    print(" \n %r deleted" % name)
else:
    print("\n Enter the name of file as command line argument")
connection.close()