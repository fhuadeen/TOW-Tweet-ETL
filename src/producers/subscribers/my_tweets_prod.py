from producers.base_producer import Producer

topic = "tweet_testing"

data = "How are you?"

my_tweets_producer = Producer(bootstrap_servers=KAFKA_SERVER)

my_tweets_producer.send(topic, data)
my_tweets_producer.flush()