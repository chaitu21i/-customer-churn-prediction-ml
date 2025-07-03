from pyflink.datastream import StreamExecutionEnvironment
from pyflink.datastream.connectors import FlinkKafkaConsumer
from pyflink.common.serialization import SimpleStringSchema

env = StreamExecutionEnvironment.get_execution_environment()

properties = {
    'bootstrap.servers': 'localhost:9092',
    'group.id': 'clickstream-group'
}

kafka_source = FlinkKafkaConsumer(
    topics='clickstream',
    deserialization_schema=SimpleStringSchema(),
    properties=properties
)

stream = env.add_source(kafka_source)
stream.print()

env.execute("Flink Clickstream Job")
