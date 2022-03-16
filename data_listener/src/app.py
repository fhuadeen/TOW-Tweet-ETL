import sys,os
BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, BASE)
from utils.const import (DB_PASSWORD, DB_USERNAME,
                        DB_HOST, DB_PORT, DB_DATABASE, KAFKA_SERVER)
import psycopg2
import tweepy
from listeners.base_consumer import Consumer
from kafka import KafkaConsumer, BrokerConnection
from json import loads

# conn = psycopg2.connect(host=DB_HOST,
#                         port=DB_PORT,
#                         user=DB_USERNAME,
#                         password=DB_PASSWORD,
#                         database=DB_DATABASE)

# cursor = conn.cursor()


topic = "items"

consumer = Consumer(topic, bootstrap_servers=KAFKA_SERVER,
                                value_deserializer=lambda x: loads(x.decode('utf-8')),
                                auto_offset_reset='earliest',
                                enable_auto_commit=True,
                                group_id='items-grp',
                                )

for message in consumer:
    message = message.value
    # user_id = message[0]
    # name = message[1]
    # user = message[2]
    # tweet = message[3]
    # cursor.execute("INSERT INTO tweets (user_id, name, username, tweet) VALUES(%s, %s, %s, %s)",
    #                 (message['user_id'], message['name'], message['username'], message['tweet']))
    # conn.commit()
    print(message)