import sys,os
BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, BASE)
from base_producer import Producer
from utils.const import KAFKA_SERVER


topic = 'item'

producer = Producer(bootstrap_servers=KAFKA_SERVER)

producer.send(topic, b'One message!')
producer.flush()