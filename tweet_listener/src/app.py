import sys,os
BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, BASE)
from utils.const import (DB_PASSWORD, DB_USERNAME,
                        DB_HOST, DB_PORT, DB_DATABASE)
import psycopg2
import tweepy
from listeners.base_consumer import Consumer

# from consumers.listeners.my_tweets_listener import user_tweets_consumer

# print(user_tweets_consumer)


topic = "item"

user_tweets_consumer = Consumer(topic)

for message in user_tweets_consumer:
    print(message)