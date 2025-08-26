from confluent_kafka import Consumer
import json, requests, os

# Environment variables
KAFKA_BROKER = os.environ.get("KAFKA_BROKER", "localhost:9092")
TOPIC = os.environ.get("KAFKA_TOPIC", "events")
INFERENCE_API_URL = os.environ.get("INFERENCE_API_URL", "http://localhost:8000/predict")

# Kafka Consumer
c = Consumer({
    'bootstrap.servers': KAFKA_BROKER,
    'group.id': 'ml_consumer',
    'auto.offset.reset': 'earliest'
})
c.subscribe([TOPIC])

print(f"[Consumer] Listening to topic '{TOPIC}' on broker {KAFKA_BROKER}")
print(f"[Consumer] Forwarding messages to inference API at {INFERENCE_API_URL}")

while True:
    msg = c.poll(1.0)
    if msg is None:
        continue
    if msg.error():
        print("Error:", msg.error())
        continue

    data = json.loads(msg.value().decode("utf-8"))

    try:
        resp = requests.get(INFERENCE_API_URL, params=data)
        print("Consumed:", data, "=> Prediction:", resp.json())
    except Exception as e:
        print("Error calling inference API:", e)