import pika 
import time 

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

def callback(ch, method, properties, body):
    print(" [x] Received %r" % body)
    time.sleep(body.count(b'.'))
    print(" [x] Done")
    ch.basic_ack(delivery_tag = method.delivery_tag)

channel.basic_consume(queue='sample_taskQueue',
                      on_message_callback=callback)

print(' [*] Waiting for messages. To exit press CTRL+C')
channel.start_consuming()