# Real-Time Streaming Data Pipeline using Kafka and Flink

This project simulates a streaming system to analyze user clickstream data in real time.

## Components
- Apache Kafka: Stream ingestion
- Apache Flink: Stream processing
- MinIO: Object storage
- Avro: Serialization
- Python: Producer simulation

## How to Run
1. Start Kafka + Zookeeper with Docker Compose
2. Run `producer.py` to simulate events
3. Run `flink_job.py` to consume and process the stream
