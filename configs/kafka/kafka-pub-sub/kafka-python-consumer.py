from kafka import KafkaConsumer
import json

# Adjust the broker IP according to your environment
KAFKA_BROKER = "172.19.0.2:9092"
TOPIC = "ghibli-movies"

# Create a Kafka consumer instance
consumer = KafkaConsumer(
    TOPIC,
    bootstrap_servers=[KAFKA_BROKER],
    auto_offset_reset="earliest",
    enable_auto_commit=True,
    group_id="ghibli-consumer-group",
    value_deserializer=lambda x: json.loads(x.decode("utf-8")),
)

print(f"Listening to topic '{TOPIC}'...\n")

try:
    for message in consumer:
        print("Received:", message.value)
except KeyboardInterrupt:
    print("\nStopped by user.")
finally:
    consumer.close()
