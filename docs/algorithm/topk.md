---
layout: default
title: top k
parent: Algorithm and Data Structure
nav_order: 101
has_children: false
---

find the top k largest value in an array

### solution 1: using java PriorityQueue
``` java
    private static List<Integer> topKLargest(int[] array, int k){

        List<Integer> list = new ArrayList<>();
        if (k > array.length || k == 0) {
            return list;
        }

        PriorityQueue<Integer> queue = new PriorityQueue<>();

        for (int i : array){
            if (queue.size()<k){
                queue.add(i);
            } else if (queue.peek() < i) {
                queue.poll();
                queue.add(i);
            }
        }

        while (k-- > 0) {
            list.add(queue.poll());
        }

        return list;
    }
```

### solution 2: quick sort

todo