#!/usr/bin/env python
import pika

credentials = pika.PlainCredentials('rodrigo', 'rodrigo')
# name is the name of user

parameters = pika.ConnectionParameters('192.168.11.3', 5672, '/rodrigo', credentials)

connection = pika.BlockingConnection(parameters)

channel = connection.channel()

channel.queue_declare(queue='hello')

def callback(ch, method, properties, body):
    print(" [x] Received %r" % body)

channel.basic_consume(callback,
                      queue='hello',
                      no_ack=True)

print(' [*] Waiting for messages. To exit press CTRL+C')
channel.start_consuming()