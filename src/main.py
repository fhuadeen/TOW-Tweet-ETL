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
    print(api.user_timeline(count=1))

# TODO: 1. Connect app to Kafka
# TODO: 2. Dockerise app
# TODO: 3. Refactor code (add test, modularise)
# TODO: 4. Add app to kubernetes (pod, svc, skaffold)
# TODO: 5. Transform the user_timeline data
# TODO: 6. Connect Kafka to Pyspark streaming
# TODO: 7. Connect Pyspark streaming to postgresql