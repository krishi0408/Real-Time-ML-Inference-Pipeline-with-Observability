from confluent_kafka import Consumer
import json, requests

c = Consumer({
    'bootstrap.servers': 'localhost:9092',
    'group.id': 'ml_consumer',
    'auto.offset.reset': 'earliest'
})
c.subscribe(['events'])
while True:
    msg = c.poll(1.0)
    if msg is None: continue
    if msg.error(): print ("Error:", msg.error()); continue
    data = json.loads(msg.value().decode("utf-8"))
    try:
        resp = requests.get("http://localhost:8000/predict", params=data)
        print("Consumed:" , data, "=> Prediction:" , resp.json())
    except Exception as e:
        print("Error calling inference API", e)