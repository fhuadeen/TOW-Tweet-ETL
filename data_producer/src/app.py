from utils.const import (TWITTER_API_KEY, TWITTER_API_SECRET,
                        ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
import sys,os
BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, BASE)
import tweepy
# from time import sleep
# from airflow import DAG
# from airflow.operators.python import PythonOperator
# from datetime import datetime, timedelta

twitter_auth = tweepy.OAuthHandler(TWITTER_API_KEY, TWITTER_API_SECRET)

def get_tweet(t_auth, a_token, a_secret):
    try:
        # authenticate twitter app with user account
        t_auth.set_access_token(a_token, a_secret)
        api = tweepy.API(t_auth) #, wait_on_rate_limit=True
        api.verify_credentials()
        print("Twitter authentication OK")
        #user = api.me()
    
    except:
        print("Error during Twitter authentication")
    finally:
        # Get user's latest from Twitter
        user_tweet = api.user_timeline(count=1)
        return user_tweet

tweet = get_tweet(t_auth=twitter_auth,
                a_token=ACCESS_TOKEN, a_secret=ACCESS_TOKEN_SECRET)

print(tweet)

# with DAG("data_producer", start_date=datetime(2021,1,1),
#     schedule_interval=timedelta(minutes=10), catchup=False) as dag:
#         user_t = PythonOperator(
#             task_id="get_tweet",
#             python_callable=_get_tweet
#             )

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


# topic = 'items' #'user-tweet-topic'

# producer = Producer(bootstrap_servers=KAFKA_SERVER,
#                     value_serializer=lambda x: dumps(x).encode('utf-8'))

# for e in range(1000,2000):
#     data = {'user_id' : e,
#             'name': 'fhuad',
#             'username': 'fhuadeen',
#             'tweet': 'I am happy!'}
#     producer.send(topic, value=data)
#     producer.flush()



