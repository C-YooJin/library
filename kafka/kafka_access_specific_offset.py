from kafka import KafkaConsumer, TopicPartition

consumer = KafkaConsumer()

# TopicPartition('Your Topic Name', partition num)
partiton = TopicPartition('Your-Topic-Name', 0)

# fill offset num that you want to access
start = 1000
end = 2000

consumer.assign([partition])
consumer.seek(partition, start)

for msg in consumer:
    if msg.offset > end:
        break
    else:
        print(" ")
        print(msg)