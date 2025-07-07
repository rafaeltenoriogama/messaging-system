from kafka import KafkaProducer
import json
import time

producer = KafkaProducer(
    # Check the correct IP Address on container kakfa
    bootstrap_servers="172.19.0.2:9092",
    value_serializer=lambda v: json.dumps(v).encode("utf-8"),
)

topic = "ghibli-movies"

messages = [
    {"titulo": "Spirited Away", "director": "Hayao Miyazaki"},
    {"titulo": "My Neighbour Totoro", "director": "Hayao Miyazaki"},
    {"titulo": "Howls Moving Castle", "diretor": "Hayao Miyazaki"},
]

for msg in messages:
    producer.send(topic, msg)
    print(f"Sended: {msg}")
    time.sleep(1)

producer.flush()
