from utils.const import (DB_PASSWORD, DB_USERNAME,
                        DB_HOST, DB_PORT, DB_DATABASE,
                        TWITTER_API_KEY, TWITTER_API_SECRET,
                        ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

import psycopg2
import tweepy

try:
    # create connection to the database server
    db_conn = psycopg2.connect(user=DB_USERNAME,
                        password=DB_PASSWORD,
                        host=DB_HOST,
                        port=DB_PORT,
                        database=DB_DATABASE)
    db_conn.autocommit = True
    print("DB connected")
except ConnectionError:
    print(ConnectionError)

# connect to twitter auth
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
    # Get user's details from Twitter
    # user_details = api.me()
    print(api.me())