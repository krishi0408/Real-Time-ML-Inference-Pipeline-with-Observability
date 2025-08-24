# This script is a Kafka producer that continuously generates and sends random data (simulating Iris flower features) to a Kafka topic.
# Import Kafka producer
from confluent_kafka import Producer
import json, time, random

# Connects to kafka broker running at loacalhost 9092
p = Producer({'bootstrap.servers': 'localhost:9092'})
topic = "events"

# Runs forever in loop generating random message with four floating point numbers
while True:
    msg = {"f1": random.uniform(4,8), "f2": random.uniform(2,4),
           "f3": random.uniform(1,6), "f4": random.uniform(0,3)}
# Converts python dict to JSON and encodes it to bytes
# Send messages to the event kafka topic
    p.produce(topic, json.dumps(msg).encode("utf-8"))
    print("Produced:", msg)
# Ensures message is actually sent before continuing
    p.flush()
# Makes it produce one message per second
    time.sleep(1)