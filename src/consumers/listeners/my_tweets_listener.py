# import sys
# sys.path.insert(1, '/home/fhuad/Documents/py/data_engineering/tweets_etl/src/consumers')
# import Consumer
# from tweets_etl.src.consumers.base_consumer import Consumer
import sys,os
BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, BASE)

from base_consumer import Consumer


topic = "tweet_testing"

my_tweets_consumer = Consumer(topic)

for message in my_tweets_consumer:
    print(message)

# from kafka import KafkaConsumer

# topic = 'items'

# consumer = KafkaConsumer(topic)
# for message in consumer:
#     print(message)