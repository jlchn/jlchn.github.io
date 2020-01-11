---
layout: default
title: quick sort
parent: Algorithm and Data Structure
nav_order: 998
has_children: false
---

- we choose a value in the array as the partition value:
    - when moving left pointer of x, the values in the right part of x must be all greater/smaller than x;
    - when moving right pointer of x, the values in the left part of x must be all smaller/greater or equal than x;
- in the initialization, we set value of array[0] as x, which means the values on left of value x are all greater/smalller than x, even though there is no value on the left of x.

``` java
private static void quickSort(int [] array, int start, int end){

        if (start >= end){
            return;
        }

        int i = start, j = end, x = array[i];

        while (i < j){
            while (i < j && array[j] >=x ){
                j--;
            }
            if (i < j){
                array[i] = array[j];
                i++;
            }
            while (i < j && array[i] < x ){
                i++;
            }
            if (i < j){
                array[j] = array[i];
                j--;
            }
        }

        array[i] = x;
        quickSort(array, start, i-1);
        quickSort(array, i+1, end);
    }
```