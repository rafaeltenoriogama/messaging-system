![Display Screen Page](./resources/screen_page.png)

# Kafka Monitoring and Messaging System

This project sets up a simple Apache Kafka messaging environment using Docker environment, with monitoring tools and a web interface for topic inspection.

## Features

- **Apache Kafka** (Bitnami image) – for producing and consuming messages
- **Redpanda Console** – modern Kafka UI for topic inspection
- **AKHQ** – alternative Kafka UI
- **Zabbix** – for infrastructure and Kafka monitoring
- **Grafana** – for dashboard visualization
- **Python examples** – basic Kafka producer and consumer scripts
- **Custom Web Page** – served via Nginx

## Usage

1. Clone the repository:

    ```bash
    git clone https://github.com/your-username/your-repo-name.git
    cd your-repo-name
    ```

2. Running the docker

    ```bash
    docker-compose up -d
    ```

    Access interfaces:

         Redpanda Console: http://localhost:8082

         AKHQ: http://localhost:8083

         Zabbix: http://localhost:8080

        Grafana: http://localhost:3000

         Static Web (Nginx): http://localhost:8081

    Python scripts:

         Located in the kafka/ folder.

         Run them using Python 3 with the kafka-python library installed.

**Notes**:

There are many ways to interact with Kafka: using Python, Spark, Spring Boot, etc.
This repository only provides Python examples for simplicity.
