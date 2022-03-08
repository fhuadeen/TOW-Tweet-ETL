import sys
sys.path.insert(1, '/twitter/src/consumers')
# from twitter.src.consumers.base_consumer 
import base_consumer


topic = "tweet_testing"

my_tweets_consumer = Consumer(topic)

for message in my_tweets_consumer:
    print(message)
