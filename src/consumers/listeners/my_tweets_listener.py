# import sys
# sys.path.insert(1, '/tweets-etl/src/consumers')
from tweets_etl.src.consumers.base_consumer import Consumer


topic = "tweet_testing"

my_tweets_consumer = Consumer(topic)

for message in my_tweets_consumer:
    print(message)

# from kafka import KafkaConsumer

# topic = 'items'

# consumer = KafkaConsumer(topic)
# for message in consumer:
#     print(message)