import sys,os
BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, BASE)
from kafka import KafkaProducer
from utils.const import KAFKA_SERVER


class Producer(KafkaProducer):
    pass
