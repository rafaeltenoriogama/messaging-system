# Kafka Producer using Python

from confluent_kafka import Producer

conf = {"bootstrap.servers": "localhost:9092"}

producer = Producer(conf)


def delivery_report(err, msg):
    if err is not None:
        print(f"Error sending messages: {err}")
    else:
        print(f"Delivered at {msg.topic()} [{msg.partition()}]")


for i in range(10):
    data = f"message {i}"
    producer.produce("my-topic", value=data.encode("utf-8"),
                     callback=delivery_report)
    producer.poll(0)

producer.flush()
