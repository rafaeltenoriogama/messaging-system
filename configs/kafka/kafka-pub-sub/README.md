# Kafka Examples

This directory contains basic examples of how to interact with Apache Kafka using **Python**.  
Kafka can be integrated with a wide variety of tools and frameworks such as:

- Apache Spark
- Spring Boot
- Python (confluent-kafka, kafka-python, etc.)

Although only Python examples are included here, the Kafka setup is compatible with any producer/consumer implementation.

---

## How to Visualize Topics and Messages

To inspect Kafka topics, messages, and broker metadata:

👉 **Use the Redpanda Kafka UI** container available in the Docker Compose stack.

Open your browser and go to:

[RedPanda Kafka UI (after you already has your docker running)](http://localhost:8082)

> Redpanda Console provides an intuitive web interface for interacting with your Kafka cluster.

---

## Python Examples

Inside this directory, you'll find Python scripts that demonstrate:

- Producing messages to a topic
- Consuming messages from a topic
- Using basic serialization

All examples assume Kafka is running and accessible at `kafka:9092` within the Docker network.

---

## Notes

- Make sure all required Python dependencies are installed (see each script for instructions).
- The Kafka container is configured using Bitnami's Kafka image.
- Topics can be created automatically or via the Redpanda Console.

Feel free to expand this directory with examples in other languages or integrations.
