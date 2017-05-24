#!/usr/bin/env python
import pika

credentials = pika.PlainCredentials('rodrigo', 'rodrigo')

parameters = pika.ConnectionParameters('192.168.11.3', 5672, '/rodrigo', credentials)

connection = pika.BlockingConnection(parameters)

channel = connection.channel()

channel.queue_declare(queue='hello')

published = channel.basic_publish(exchange='',
                      routing_key='hello',
                      body='Hello World!')

print(" [x] Sent 'Hello World!'")

connection.close()
