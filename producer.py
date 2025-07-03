from kafka import KafkaProducer
import json
import time
import random

producer = KafkaProducer(
    bootstrap_servers='localhost:9092',
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

user_ids = [101, 102, 103, 104]
actions = ['click', 'scroll', 'purchase']

while True:
    event = {
        'user_id': random.choice(user_ids),
        'action': random.choice(actions),
        'timestamp': int(time.time())
    }
    producer.send('clickstream', value=event)
    print(f"Sent: {event}")
    time.sleep(1)
