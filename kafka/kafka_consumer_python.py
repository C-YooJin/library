from kafka import KafkaConsumer
from json import loads

consumer = KafkaConsumer('topic-name',
                         bootstrap_server=['localhost:9092'],
                         auto_offset_reset = 'earliest',
                         enable_auto_commit = True)

def is_json(input):
    try:
        result_json = json.loads(input)
    except ValueError as e:
        return False
    return result_json

for message in consumer:
    # message value and key are raw bytes -- decode if necessary!
    # e.g., for unicode: 'message.value.decode('utf-8')'
    print(" ")
    input = message.value.decode("utf-8")
    result = is_json(input)

    if result["BasicLog"]["PCID"] == "blahblah":
        print("Topic: %s" % message.topic)
        print("Partition: %d" % message.partition)
        print("Offset: %d" % message.offset)
        print("Key: %s" % message.key)
        print(result)

"""
KafkaConsumer(value_deserializer=msgpack.unpackb)
KafkaConsumer(value_deserializer=lambda m: json.loads(m.decode('ascii'))
"""