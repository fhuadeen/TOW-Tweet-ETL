import sys,os
BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, BASE)
from utils.const import (DB_PASSWORD, DB_USERNAME,
                        DB_HOST, DB_PORT, DB_DATABASE,
                        TWITTER_API_KEY, TWITTER_API_SECRET,
                        ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

import psycopg2
import tweepy

from consumers.listeners.my_tweets_listener import user_tweets_consumer

# print(user_tweets_consumer)