---
layout: default
title: Kafka Topic Management
parent: Kafka
nav_order: 1
has_children: false
---

# create a topic

## assign the replicas dynamically

let's create a topic `first-topic` with 4 partitions and 2 replicas. 

``` bash
kafka-topics --zookeeper zookeeper-1:12181 --create --topic first-topic --partitions 4 --replication-factor 2
```

after creating, there would be directories of the new topic in Kafka data directory.

let's login to 3 Kafka nodes and run below command:

``` bash

root@kafka-1: ls /var/lib/kafka/data | grep first-topic
first-topic-0
first-topic-2

root@kafka-2: ls /var/lib/kafka/data | grep first-topic
first-topic-0
first-topic-1
first-topic-3


root@kafka-3: ls /var/lib/kafka/data | grep first-topic
first-topic-1
first-topic-2
first-topic-3
```
as you can see, 8(=2 * 4) directories of the `first-topic` has been created on 3 nodes. we can also verify this by using below command

``` bash
kafka-topics --zookeeper zookeeper-2:22181 --describe --topic first-topic

Topic:first-topic	PartitionCount:4	ReplicationFactor:2	Configs:
	Topic: first-topic	Partition: 0	Leader: 2	Replicas: 2,1	Isr: 2,1
	Topic: first-topic	Partition: 1	Leader: 3	Replicas: 3,2	Isr: 3,2
	Topic: first-topic	Partition: 2	Leader: 1	Replicas: 1,3	Isr: 1,3
	Topic: first-topic	Partition: 3	Leader: 2	Replicas: 2,3	Isr: 2,3

```

`Topic: first-topic	Partition: 0	Leader: 2	Replicas: 2,1	Isr: 2,1` means:
- the leader of partition `0` locates on the broker `2`, `2` is the broker Id
- another replica of partition `0` locates on the broker `1`.
- the isr of partition `0` is broker `1` and broker `2`

## one broker can only hold one replica for each partition

notice we have 3 nodes in the cluster, so we can have at most 3 replicas for each partition. 

if we create 4 replica for a partition, Kafka will stop us from doing this by throwing an error.

``` 

kafka-topics --zookeeper zookeeper-1:12181 --create --topic second-topic --partitions 4 --replication-factor 4

Error while executing topic command : Replication factor: 4 larger than available brokers: 3.
[2019-11-30 07:07:02,569] ERROR org.apache.kafka.common.errors.InvalidReplicationFactorException: Replication factor: 4 larger than available brokers: 3.
```

## assign replica manually

by default, Kafka will help us decide the where to assign each replica. however, if you want to decide yourself, you can use below command

```
kafka-topics --zookeeper zookeeper-1:12181 --create --topic another-topic --replica-assignment 0:1,1:2,0:2,1:2

kafka-topics --zookeeper zookeeper-2:22181 --describe --topic another-topic
Topic:another-topic	PartitionCount:4	ReplicationFactor:2	Configs:
	Topic: another-topic	Partition: 0	Leader: 1	Replicas: 0,1	Isr: 1
	Topic: another-topic	Partition: 1	Leader: 1	Replicas: 1,2	Isr: 1,2
	Topic: another-topic	Partition: 2	Leader: 2	Replicas: 0,2	Isr: 2
	Topic: another-topic	Partition: 3	Leader: 1	Replicas: 1,2	Isr: 1,2
```

we created topic with 4 partitions and 2 relicas, the first partion locates on broker 0 and broker 1, the second partition locates on broker 1 and broker 2, the third broker locates on broker 0 and broker 2 and the fourth partion locates on broker 1 and broker 2


# list all kafka topics

```
kafka-topics --zookeeper zookeeper-2:22181 --list

__confluent.support.metrics
```

# describe topics

```
kafka-topics --zookeeper zookeeper-2:22181 --describe --topic __confluent.support.metrics
Topic:__confluent.support.metrics	PartitionCount:1	ReplicationFactor:3	Configs:retention.ms=31536000000
	Topic: __confluent.support.metrics	Partition: 0	Leader: 2	Replicas: 2,1,3	Isr: 2,1,3
```

## describe under replicated partitions

when a replica is lost or has problems which sync from the leader replica, it would be remove from the ISR collection.

we can find `partitions` under such condition by providing `--under-replicated-partitions` on describe command. 

let's stop one broker and see what's happening

```
kafka-topics --zookeeper zookeeper-2:22181 --describe --topic first-topic
Topic:first-topic	PartitionCount:4	ReplicationFactor:2	Configs:
	Topic: first-topic	Partition: 0	Leader: 2	Replicas: 2,1	Isr: 2,1
	Topic: first-topic	Partition: 1	Leader: 2	Replicas: 3,2	Isr: 2
	Topic: first-topic	Partition: 2	Leader: 1	Replicas: 1,3	Isr: 1
	Topic: first-topic	Partition: 3	Leader: 2	Replicas: 2,3	Isr: 2

kafka-topics --zookeeper zookeeper-2:22181 --describe --topic first-topic --under-replicated-partitions
	Topic: first-topic	Partition: 1	Leader: 2	Replicas: 3,2	Isr: 2
	Topic: first-topic	Partition: 2	Leader: 1	Replicas: 1,3	Isr: 1
	Topic: first-topic	Partition: 3	Leader: 2	Replicas: 2,3	Isr: 2

```

after stopping one broker, we see the `ISR` has less broker Ids than `Replicas`. 

Kafka doesn't help us re-arrange the lost replica to other brokers even though there are enough spaces, why? #todo

## describe unavailable partitions

when leader partition left the cluster, this partition cannot be used by producer or consumer any more, we can find such partitions by using `--unavailable-partions` in describe command.

we can stop 2 broker thus only 1 broker left running, and check which partition we lost

```
kafka-topics --zookeeper zookeeper-2:22181 --describe --topic first-topic --unavailable-partitions
	Topic: first-topic	Partition: 2	Leader: -1	Replicas: 1,3	Isr: 1
```
as you can see, partition 2 is lost thus cannot provide service to producers or consumers.

# alter a topic

## alter topic partition number

```
kafka-topics --zookeeper zookeeper-2:22181 --alter --topic first-topic --partitions 5

kafka-topics --zookeeper zookeeper-2:22181 --describe --topic first-topic
Topic:first-topic	PartitionCount:5	ReplicationFactor:2	Configs:
	Topic: first-topic	Partition: 0	Leader: 2	Replicas: 2,1	Isr: 2,1
	Topic: first-topic	Partition: 1	Leader: 3	Replicas: 3,2	Isr: 2,3
	Topic: first-topic	Partition: 2	Leader: 1	Replicas: 1,3	Isr: 1,3
	Topic: first-topic	Partition: 3	Leader: 2	Replicas: 2,3	Isr: 2,3
	Topic: first-topic	Partition: 4	Leader: 3	Replicas: 3,2	Isr: 3,2
```
attention
- after changing the partition number, the messages in one partition will be arranged to other partitions, which means if you depends on key to distribute messages to different partitions, you will see unexpected behavior.
- decreasing the partition number is not supported right now, we decreasing the number, Kafka has to care about how to deal with messages on the partitions beling deleted: Kafka has to copy these messages to other partitions, and merge the messages to the existing log files, it is a huge work.

# manage topic configs

Kafka provides a seperate command to help us update topic configurations like `max.message.bytes` or `retention.ms`

``` bash
# add 
kafka-configs --zookeeper zookeeper-2:22181 --alter --entity-type topics --entity-name first-topic --add-config max.message.bytes=10000
Completed Updating config for entity: topic 'first-topic'.
# add
kafka-configs --zookeeper zookeeper-2:22181 --alter --entity-type topics --entity-name first-topic --add-config retention.ms=60000000
Completed Updating config for entity: topic 'first-topic'.
# describe
kafka-configs --zookeeper zookeeper-2:22181 --describe --entity-type topics --entity-name first-topic
Configs for topic 'first-topic' are retention.ms=60000000,max.message.bytes=10000
# delete
kafka-configs --zookeeper zookeeper-2:22181 --alter --entity-type topics --entity-name first-topic --delete-config max.message.bytes,retention.ms
```

# delete a topic

```
kafka-topics --zookeeper zookeeper-2:22181 --delete --topic another-topic
```