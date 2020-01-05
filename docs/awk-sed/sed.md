---
layout: default
title: awk
parent: awk & sed
nav_order: 2
has_children: false
---

```bash

date "+%Y%m%d.1730"


#!/bin/bash

echo $1;

echo $2;

name1=docker.1

name2=docker.2

tag=$1

sed -i '.bak' "s/$name1=\".*\"/$name1=\"$tag\"/" test.txt

sed -i '.bak' "s/$name2=\".*\"/$name2=\"$tag\"/" test.txt
```