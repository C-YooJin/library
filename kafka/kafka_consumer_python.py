from kafka import KafkaConsumer
from json import loads

consumer = KafkaConsumer('topic-name',
                         bootstrap_server=['localhost:9092'],
                         auto_offset_reset = 'earliest',
                         enable_auto_commit = True)

for message in consumer:
    print(" ")
    print("%s:%d:%d: key=%s value=%s" % (message.topic, message.partition,
                                         message.offset, message.key,
                                         message.value))
    print(" ")
    print("%s" % (message.value))


"""
KafkaConsumer(value_deserializer=msgpack.unpackb)
KafkaConsumer(value_deserializer=lambda m: json.loads(m.decode('ascii'))
"""