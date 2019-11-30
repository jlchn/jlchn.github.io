---
layout: default
title: Partition Management
parent: Kafka
nav_order: 2
has_children: false
---

in Kafka, only leader replica serves read and write requests from client, the other replica only sync from the leader replica, they are not exposed to clients.

in order to balance the requests evenly to all broker, Kafka will try its best to seperate the leaders to all brokers. 

however, when some broker down, in order to continue serve for clients, Kafka will elect one replica(on another replica) as leader. 


``` bash
# when there are 3 broker
kafka-topics --zookeeper zookeeper-2:22181 --describe --topic first-topic
Topic:first-topic	PartitionCount:5	ReplicationFactor:2	Configs:
	Topic: first-topic	Partition: 0	Leader: 2	Replicas: 2,1	Isr: 2,1
	Topic: first-topic	Partition: 1	Leader: 3	Replicas: 3,2	Isr: 2,3
	Topic: first-topic	Partition: 2	Leader: 1	Replicas: 1,3	Isr: 1,3
	Topic: first-topic	Partition: 3	Leader: 2	Replicas: 2,3	Isr: 2,3
	Topic: first-topic	Partition: 4	Leader: 3	Replicas: 3,2	Isr: 3,2

# when broker 1 is stopped
kafka-topics --zookeeper zookeeper-2:22181 --describe --topic first-topic
Topic:first-topic	PartitionCount:5	ReplicationFactor:2	Configs:
	Topic: first-topic	Partition: 0	Leader: 2	Replicas: 2,1	Isr: 2
	Topic: first-topic	Partition: 1	Leader: 3	Replicas: 3,2	Isr: 2,3
	Topic: first-topic	Partition: 2	Leader: 3	Replicas: 1,3	Isr: 3
	Topic: first-topic	Partition: 3	Leader: 2	Replicas: 2,3	Isr: 2,3
	Topic: first-topic	Partition: 4	Leader: 3	Replicas: 3,2	Isr: 3,2

```

in this case, the broker which holds new leader will suffer more loads. Kafka avoids such case by rebalance the leaders every 5 minutes.

``` bash
# broker 1 is up again and after 5 mibutes
kafka-topics --zookeeper zookeeper-2:22181 --describe --topic first-topic
Topic:first-topic	PartitionCount:5	ReplicationFactor:2	Configs:
	Topic: first-topic	Partition: 0	Leader: 2	Replicas: 2,1	Isr: 2
	Topic: first-topic	Partition: 1	Leader: 3	Replicas: 3,2	Isr: 2,3
	Topic: first-topic	Partition: 2	Leader: 3	Replicas: 1,3	Isr: 3
	Topic: first-topic	Partition: 3	Leader: 2	Replicas: 2,3	Isr: 2,3
	Topic: first-topic	Partition: 4	Leader: 3	Replicas: 3,2	Isr: 3,2
```

rebalancing the leaders will stop serving to clients, it will cause slow responses to clients when Kafka is under high loads.

we should avoid such situation and ask Kafka do partition rebalance while Kafka in low loads. to achieve this, we can set `auto.leader.rebalance.enble=false` and use `kafka-preferred-replica-election.sh` to do it manually.

``` bash
# rebalance all topic and partitions
kafka-preferred-replica-election --zookeeper zookeeper-2:22181

Created preferred replica election path with first-topic-2,second-topic-2,first-topic-4,first-topic-3,another-topic-0,second-topic-3,1-topic-0,second-topic-0,__confluent.support.metrics-0,first-topic-1,1-topic-2,another-topic-1,1-topic-1,first-topic-0,another-topic-3,another-topic-2,second-topic-1
Successfully started preferred replica election for partitions Set(first-topic-2, second-topic-2, first-topic-4, first-topic-3, another-topic-0, second-topic-3, 1-topic-0, second-topic-0, __confluent.support.metrics-0, first-topic-1, 1-topic-2, another-topic-1, 1-topic-1, first-topic-0, another-topic-3, another-topic-2, second-topic-1)

```
rebalance all topics and partitions will cost lots of time, we usually rebalance per pertations.

we can do this by providing a file named `election.json` and pass `--path-to-json-file election.json` to `kafka-preferred-replica-election`

``` json
{
    "partitions": [
        {
            "topic": "first-topic",
            "partition": 0
        },
        {
            "topic": "first-topic",
            "partition": 1
        }
    ]
}
```

```
kafka-preferred-replica-election --zookeeper zookeeper-2:22181 --path-to-json-file election.json

Created preferred replica election path with first-topic-0,first-topic-1
Successfully started preferred replica election for partitions Set(first-topic-0, first-topic-1)
```

# partition re-assignment

why do we need partition re-assignment manually?

- when a broker is lost, or when we want to bring some broker down regularlly, if there were leader replicas there, Kafka will find another replica in ISR and mark it as leader, but Kafka won't help us re-assign the missing replica to the living brokers.
- when adding new brokers in the cluster, Kafka won't help us re-assign replicas to this new broker, only new topic's partitions have the chance to be assigned there.

now considering we want to stop broker 2 and upgrade the host to support higher loads. we need to assign all the replicas to other brokers.

first, we need to prepare a file to tell Kafka which topics do we want to re-assign, this requires us check which topics are on broker 2. 

create a file named `re-assign.json`, the file content is like this:

```
{
    "topics": [
        {
            "topic": "first-topic"
        }
    ],
    "version": 1
}
```

then, let Kafka help propose a reassignment configuration. 

```
kafka-reassign-partitions --zookeeper zookeeper-2:22181 --generate --topics-to-move-json-file re-assign.json --broker-list 1,3
Current partition replica assignment
{"version":1,"partitions":[{"topic":"first-topic","partition":2,"replicas":[1,3],"log_dirs":["any","any"]},{"topic":"first-topic","partition":4,"replicas":[3,2],"log_dirs":["any","any"]},{"topic":"first-topic","partition":3,"replicas":[2,3],"log_dirs":["any","any"]},{"topic":"first-topic","partition":1,"replicas":[3,2],"log_dirs":["any","any"]},{"topic":"first-topic","partition":0,"replicas":[2,1],"log_dirs":["any","any"]}]}

Proposed partition reassignment configuration
{"version":1,"partitions":[{"topic":"first-topic","partition":2,"replicas":[3,1],"log_dirs":["any","any"]},{"topic":"first-topic","partition":4,"replicas":[3,1],"log_dirs":["any","any"]},{"topic":"first-topic","partition":1,"replicas":[1,3],"log_dirs":["any","any"]},{"topic":"first-topic","partition":3,"replicas":[1,3],"log_dirs":["any","any"]},{"topic":"first-topic","partition":0,"replicas":[3,1],"log_dirs":["any","any"]}]}
```
it tells us the `Current partition replica assignment`, we'd better keep it in a safe place in case we want to rollback the configuration.

save the `Proposed partition reassignment configuration`(json format) into a file named `solution.json`

and run below command

```
 kafka-reassign-partitions --zookeeper zookeeper-2:22181 --execute --reassignment-json-file solution.json
```
you should see there is no partitions on broker 2, now it is safe for us to bring broker 2 down.
```
kafka-topics --zookeeper zookeeper-2:22181 --describe --topic first-topic
Topic:first-topic	PartitionCount:5	ReplicationFactor:2	Configs:
	Topic: first-topic	Partition: 0	Leader: 3	Replicas: 3,1	Isr: 1,3
	Topic: first-topic	Partition: 1	Leader: 3	Replicas: 1,3	Isr: 3,1
	Topic: first-topic	Partition: 2	Leader: 1	Replicas: 3,1	Isr: 3,1
	Topic: first-topic	Partition: 3	Leader: 1	Replicas: 1,3	Isr: 3,1
	Topic: first-topic	Partition: 4	Leader: 3	Replicas: 3,1	Isr: 3,1
```

when broker 2 is back, or when you add new brokers to the cluster, you can update the re-assign.json(change the version) file and run `kafka-reassign-partitions` to put partitions on new brokers. 

# replica reassignment

when we execute `kafka-reassign-partition`, we see partition configuration like this:
``` json
{
    "version": 1,
    "partitions": [
        {
            "topic": "first-topic",
            "partition": 2,
            "replicas": [
                1,
                2
            ],
            "log_dirs": [
                "any",
                "any"
            ]
        },
        {
            "topic": "first-topic",
            "partition": 4,
            "replicas": [
                3,
                2
            ],
            "log_dirs": [
                "any",
                "any"
            ]
        },
        {
            "topic": "first-topic",
            "partition": 3,
            "replicas": [
                2,
                1
            ],
            "log_dirs": [
                "any",
                "any"
            ]
        },
        {
            "topic": "first-topic",
            "partition": 1,
            "replicas": [
                3,
                1
            ],
            "log_dirs": [
                "any",
                "any"
            ]
        },
        {
            "topic": "first-topic",
            "partition": 0,
            "replicas": [
                2,
                3
            ],
            "log_dirs": [
                "any",
                "any"
            ]
        }
    ]
}
```

we can update the `replicas` section and `log_dirs` section, if we want to add a replica, we can update it as follows:

``` json
{
    "version": 1,
    "partitions": [
        {
            "topic": "first-topic",
            "partition": 2,
            "replicas": [
                1,
                2,
                3
            ],
            "log_dirs": [
                "any",
                "any",
                "any"
            ]
        },
        {
            "topic": "first-topic",
            "partition": 4,
            "replicas": [
                3,
                2,
                1
            ],
            "log_dirs": [
                "any",
                "any",
                "any"
            ]
        },
        {
            "topic": "first-topic",
            "partition": 3,
            "replicas": [
                2,
                1,
                3
            ],
            "log_dirs": [
                "any",
                "any",
                "any"
            ]
        },
        {
            "topic": "first-topic",
            "partition": 1,
            "replicas": [
                3,
                1,
                2
            ],
            "log_dirs": [
                "any",
                "any",
                "any"
            ]
        },
        {
            "topic": "first-topic",
            "partition": 0,
            "replicas": [
                2,
                3,
                1
            ],
            "log_dirs": [
                "any",
                "any",
                "any"
            ]
        }
    ]
}
```
after executing `kafka-reassign-partition`, you will see new replicas are assigned to each partition.
```

kafka-topics --zookeeper zookeeper-2:22181 --describe --topic first-topic             Topic:first-topic	PartitionCount:5	ReplicationFactor:3	Configs:
	Topic: first-topic	Partition: 0	Leader: 2	Replicas: 2,3,1	Isr: 2,1,3
	Topic: first-topic	Partition: 1	Leader: 3	Replicas: 3,1,2	Isr: 3,2,1
	Topic: first-topic	Partition: 2	Leader: 1	Replicas: 1,2,3	Isr: 1,3,2
	Topic: first-topic	Partition: 3	Leader: 2	Replicas: 2,1,3	Isr: 2,3,1
	Topic: first-topic	Partition: 4	Leader: 3	Replicas: 3,2,1	Isr: 3,1,2

```