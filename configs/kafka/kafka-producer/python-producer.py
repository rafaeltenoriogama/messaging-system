from kafka import KafkaProducer
import json
import time

producer = KafkaProducer(
    bootstrap_servers="172.19.0.2:9092",  # IP interno do container Kafka
    value_serializer=lambda v: json.dumps(v).encode("utf-8"),
)

topic = "ghibli-filmes"

mensagens = [
    {"titulo": "A Viagem de Chihiro", "diretor": "Hayao Miyazaki"},
    {"titulo": "Meu Amigo Totoro", "diretor": "Hayao Miyazaki"},
    {"titulo": "O Castelo Animado", "diretor": "Hayao Miyazaki"},
]

for msg in mensagens:
    producer.send(topic, msg)
    print(f"Enviado: {msg}")
    time.sleep(1)

producer.flush()

