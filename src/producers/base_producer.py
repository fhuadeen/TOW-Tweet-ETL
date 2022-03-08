from kafka import KafkaProducer
from utils.const import KAFKA_SERVER

# producer = KafkaProducer(bootstrap_servers=KAFKA_SERVER)

class Producer(KafkaProducer):
    pass

# producer.send(topic, data)
# producer.flush()