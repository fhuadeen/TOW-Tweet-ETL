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

conn = psycopg2.connect(host=DB_HOST,
                        port=DB_PORT,
                        user=DB_USERNAME,
                        password=DB_PASSWORD,
                        database=DB_DATABASE)

cursor = conn.cursor()


topic = "items"

consumer = Consumer(topic, bootstrap_servers=KAFKA_SERVER,
                                value_deserializer=lambda x: loads(x.decode('utf-8')),
                                auto_offset_reset='earliest',
                                enable_auto_commit=True,
                                group_id='items-grp',
                                )

for message in consumer:
    user_id = message['user_id']
    name = message['name']
    user = message['username']
    tweet = message['tweet']
    cursor.execute("INSERT INTO tweets (user_id, name, username, tweet) VALUES(%s, %s, %s, %s)",
                    (user_id, name, username, tweet))
    cursor.close()
    print(msg)