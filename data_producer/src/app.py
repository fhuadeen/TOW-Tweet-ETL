from utils.const import (TWITTER_API_KEY, TWITTER_API_SECRET,
                        ACCESS_TOKEN, ACCESS_TOKEN_SECRET, KAFKA_SERVER)
import sys,os
BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, BASE)
from subscribers.base_producer import Producer
import psycopg2
import tweepy
from json import dumps
from time import sleep

twitter_auth = tweepy.OAuthHandler(TWITTER_API_KEY, TWITTER_API_SECRET)

# try:
#     # authenticate twitter app with user account
#     twitter_auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
#     api = tweepy.API(twitter_auth) #, wait_on_rate_limit=True
#     api.verify_credentials()
#     print("Twitter authentication OK")
#     #user = api.me()
    
# except:
#     print("Error during Twitter authentication")
# finally:
#     # Get user's latest from Twitter
#     user_tweet = api.user_timeline(count=1)


topic = 'items' #'user-tweet-topic'

producer = Producer(bootstrap_servers=KAFKA_SERVER,
                    value_serializer=lambda x: dumps(x).encode('utf-8'))

for e in range(1000):
    data = {'user_id' : e,
            'name': 'fhuad',
            'username': 'fhuadeen',
            'tweet': 'I am happy!'}
    producer.send(topic, value=data)
    producer.flush()
    sleep(5)

# producer.send(topic, b'my Message!!!')
# producer.flush()


