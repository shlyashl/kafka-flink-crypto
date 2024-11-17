from kafka import KafkaProducer
import json
from logger import log


class KafkaMessageProducer:
    def __init__(self, bootstrap_servers: str, topic: str):
        self.producer = KafkaProducer(
            bootstrap_servers=bootstrap_servers,
            value_serializer=lambda v: json.dumps(v).encode('utf-8')
        )
        self.topic = topic
        log.info(f"producer initialized for topic '{topic}'.")

    def send_message(self, message: dict):
        try:
            self.producer.send(self.topic, message)
            log.info(f"message sent to Kafka topic '{self.topic}': {message}")
        except Exception as e:
            log.error(f"failed to send message to Kafka: {e}")

    def close(self):
        self.producer.close()
        log.info("producer closed")






from kafka import KafkaProducer, KafkaAdminClient
from kafka.admin import NewTopic
import json
from logger import log

class KafkaMessageProducer:
    def __init__(self, bootstrap_servers: str, topic: str):
        self.bootstrap_servers = bootstrap_servers
        self.topic = topic
        self._create_topic_if_not_exists()

        self.producer = KafkaProducer(
            bootstrap_servers=self.bootstrap_servers,
            value_serializer=lambda v: json.dumps(v).encode('utf-8')
        )
        log.info(f"Kafka producer initialized for topic '{self.topic}'.")

    def _create_topic_if_not_exists(self):
        try:
            admin_client = KafkaAdminClient(bootstrap_servers=self.bootstrap_servers)
            existing_topics = admin_client.list_topics()
            if self.topic not in existing_topics:
                log.info(f"сreating {self.topic=}")
                topic = NewTopic(name=self.topic, num_partitions=1, replication_factor=1)
                admin_client.create_topics(new_topics=[topic], validate_only=False)
                log.info(f"{self.topic=} created successfully")
            else:
                log.info(f"{self.topic=} already exists")
        except Exception as e:
            log.error(f"error while creating '{self.topic=}': {e=}")

    def send_message(self, message: dict):
        try:
            self.producer.send(self.topic, message)
            log.info(f"message sent to Kafka topic '{self.topic}': {message}")
        except Exception as e:
            log.error(f"failed to send message to Kafka: {e}")

    def close(self):
        self.producer.close()
        log.info("producer closed")