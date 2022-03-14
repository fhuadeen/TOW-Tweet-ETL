from utils.const import (TWITTER_API_KEY, TWITTER_API_SECRET,
                        ACCESS_TOKEN, ACCESS_TOKEN_SECRET, KAFKA_SERVER)
import sys,os
BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, BASE)
from subscribers.base_producer import Producer
import psycopg2
import tweepy

twitter_auth = tweepy.OAuthHandler(TWITTER_API_KEY, TWITTER_API_SECRET)

try:
    # authenticate twitter app with user account
    twitter_auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
    api = tweepy.API(twitter_auth) #, wait_on_rate_limit=True
    api.verify_credentials()
    print("Twitter authentication OK")
    #user = api.me()
    
except:
    print("Error during Twitter authentication")
finally:
    # Get user's latest from Twitter
    user_tweet = api.user_timeline(count=1)


topic = 'item' #'user-tweet-topic'

producer = Producer(bootstrap_servers=KAFKA_SERVER)

producer.send(topic, b'my Message!!!')
producer.flush()


