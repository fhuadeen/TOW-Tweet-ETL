import sys,os
BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, BASE)
from base_consumer import Consumer


topic = "item"

user_tweets_consumer = Consumer(topic)

for message in my_tweets_consumer:
    print(message)
