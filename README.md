# Rabbitmq 2 Kinesis

## Presentation

This software connects to a RabbitMQ queue and allows you to send the data received from the queue to a Kinesis Stream on AWS.

## Prerequisites

Install the required Python packages:

```bash
pip install -r requirements.txt
```

To be able to use it you also have configure your `~/.aws/credentials`
file according to the [boto3 documentation](http://boto3.readthedocs.io/en/latest/guide/quickstart.html#configuration).

## How to use it

Edit the `config.yml` file in the same folder as the python script.
This configuration file contains data about your RabbitMQ queue and your Kinesis stream.
The configuration file must look like that :

```yaml
simulation: False     #Simulation mode (if True, only shows RabbitMQ messages on the terminal and does not send it to AWS

rabbitmq:
  host: localhost     #hostname or ip of the Rabbitmq server
  queue: queue        #name of the queue

aws:
  region: eu-west-1   #region of your Kinesis stream
  stream: TBD         #name of your Kinesis stream
  partition_key: TBD  #partition key of your Kinesis stream
```
If you want to test your setup before sending data to AWS, just use `simulation: True` in the config file.
With `simulation: True` the software will only log date received from RabbitMQ in the console and will not send
the data to AWS.

### Manual usage

Then just start the software

```
python rabbitmq2kinesis.py
```

### Development environment

Environment installation (for CentOs 7)

* Run the `install.sh` script.
* Run `docker-compose up` 
* You have now a rabbitmq server listening on port 5672 of your machine

TODO: move the rabbitmq2kinesis in a docker container in the docker-compose file
