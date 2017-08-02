import pika
import boto3
import yaml

with open("config.yml", 'r') as ymlfile:
    cfg = yaml.load(ymlfile)

rabbitmq_host = cfg['rabbitmq']['host']
rabbitmq_queue = cfg['rabbitmq']['queue']
aws_region = cfg['aws']['region']
kinesis_stream = cfg['aws']['stream']
kinesis_partiton_key = cfg['aws']['partition_key']
simulation = cfg['simulation']

connection = pika.BlockingConnection(pika.ConnectionParameters(host=rabbitmq_host))
channel = connection.channel()

if not simulation:
    client = boto3.client('kinesis', region_name=aws_region)

channel.queue_declare(queue=rabbitmq_queue, durable=True)
print('[INFO] Waiting for messages. To exit press CTRL+C')


def callback(ch, method, body):

    print("[INFO] Received %r" % body)
    ch.basic_ack(delivery_tag=method.delivery_tag)

    if not simulation :
        response = client.put_record(
            StreamName=kinesis_stream,
            Data=body,
            PartitionKey=kinesis_partiton_key,
        )

        if response["ResponseMetadata"]["HTTPStatusCode"] == 200:
            print("[OK] Data sent, your request ID is : " + response["ResponseMetadata"]["RequestId"])

        else:
            print("[ERROR] something went wrong")
            exit(1)

channel.basic_qos(prefetch_count=1)

channel.basic_consume(callback,
                      queue=rabbitmq_queue)

channel.start_consuming()