from confluent_kafka import Producer
import json, time, random, os

# Read environment variables (default fallback if not set)
KAFKA_BROKER = os.environ.get("KAFKA_BROKER", "localhost:9092")
TOPIC = os.environ.get("KAFKA_TOPIC", "events")

# Kafka Producer
p = Producer({'bootstrap.servers': KAFKA_BROKER})

print(f"[Producer] Sending messages to topic '{TOPIC}' on broker {KAFKA_BROKER}")

# Runs forever generating random messages
while True:
    msg = {
        "f1": random.uniform(4, 8),
        "f2": random.uniform(2, 4),
        "f3": random.uniform(1, 6),
        "f4": random.uniform(0, 3),
    }
    # Convert dict -> JSON -> bytes
    p.produce(TOPIC, json.dumps(msg).encode("utf-8"))
    print("Produced:", msg)
    p.flush()   # ensure delivery
    time.sleep(1)