---
layout: default
title: Overview
parent: Distributed System
nav_order: 1
has_children: false
---

# Overview

A Bloom filter is a data structure that is used to test whether a collection containing a specific element.

Bloom filter returns either an element is `100% not in the collection` or `possibly in the collection`.

A bloom filter consists of `m` hash functions and a bit array of `n` bits.

```
                    +------------------------+
                    |                        |
         +----------+       a string         +---------+
         |          |                        |         |
         |          +-----------+------------+         |
         |                      |                      |
         |                      |                      |
+--------v--------+    +--------v--------+    +--------v--------+
|                 |    |                 |    |                 |
|   hash_func_1   |    |   hash_func_2   |    |   hash_func_3   |
|                 |    |                 |    |                 |
+------+----------+    +---------+-------+    +----------+------+
       |                         |                       |
       |                         |                       |
       |                         |                       |
+------v-----+------------+------v-----+------------+----v------+
|            |            |            |            |           |
|     1      |      0     |     1      |     0      |     1     |
|            |            |            |            |           |
+------------+------------+------------+------------+-----------+

```

# Add elements to bloom filter

suppose we have 3 hash functions and a bit array of 5 bits.

for the input `good`, we use the 3 hash functions to get the results, the results indicate the positions(indices) of the bit array.

```
hash_func_1('good') % 5 = 1
hash_func_2('good') % 5 = 3
hash_func_3('good') % 5 = 5
```
after adding the frist word, the bit array is changed like the following.

| 1   | 2       | 3     | 4    | 5     |
| ---:| -------:| -----:|-----:| -----:|
| 1   |0        | 1     | 0    | 1     |


for the second input `bad`,  we use the 3 hash functions and get the below results


```
hash_func_1('bad') % 5 = 1
hash_func_2('bad') % 5 = 2
hash_func_3('bad') % 5 = 3
```

after adding the second word, the bit array is changed like the following.

| 1   | 2       | 3     | 4    | 5     |
| ---:| -------:| -----:|-----:| -----:|
| 1   |1        | 1     | 0    | 1     |

as you can see, both `good` and `bad` are hashed into the same position `1` and `2`.

# find element in bloom filter

find element in bloom filter requires the input string being hashed by 3 hash functions as well.

consider the input string is `how` and we got below results

```
hash_func_1('how') % 5 = 1
hash_func_2('how') % 5 = 2
hash_func_3('how') % 5 = 3
```

all the values of position 1,2 and 3 are 1, however, we know the `1` in these positions are set while adding `good` and `bad`.

this is why we say bloom filer can not guarantee the input is `100% in the collection`.

next, let's consider the input string is `why` and we got below results

```
hash_func_1('how') % 5 = 2
hash_func_2('how') % 5 = 3
hash_func_3('how') % 5 = 4
```

even though the values of position 2 and 3 is 1,  the value of position 4 is `0`, which means not all result values are 1, we say `why is 100% not in the collection` 

we call the `possibly in the collection` as `false positive`, we can decrease the `false positive` by using a more number of hash functions and adding more spaces to the bit array of Bloom filter. 

# further reading

- Guava bloom filter
- Redis bloom filter