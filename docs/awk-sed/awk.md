---
layout: default
title: awk
parent: awk & sed
nav_order: 1
has_children: false
---

### working process

- process
    - execute commands in `BEGIN` block;
        - commands in `BEGIN` block will only be executed once;
    - read, execute and repeat;
        - read: read a line from the inputs;
        - execute: most Awk programs will start with a "{" and end with a "}". everything in between there gets run once on each line of input;
        - repeat commands on the next line in the inputs(file etc.) between "{" and "}"
    - execute commands in `END` block;
        - execute commands in `END` block  will only be executed once;
    

### placeholder and delimiter
``` bash
awk '{print $0}'
```
`$0` is the entire line, and awk parses the line in to fields for us automatically, using any whitespace (space, tab) as a delimiter, merging consecutive delimiters. Those fields are available to us as the variables `$1, $2, $3`, etc.

```bash
echo 'this is a test' | awk '{print $3}'  # prints 'a'
echo 'this is a test' | awk '{print $1,$3}'  # prints 'this a'
echo 'this is a test' | awk '{print $1$3}'  # prints 'thisa'
```
The special variable, `NF`, contains the number of fields in the current line. 
```bash
echo 'this is a test' | awk '{print $NF}'  # prints "test"
echo 'this is a test' | awk '{print $1, $(NF-2) }' # prints "this is"
```

Commas between arguments in a print statement put spaces between them, but we can leave out the comma and no spaces are inserted
``` bash
echo 'this is a test' | awk '{print $1,$3}'  # prints 'this a'
echo 'this is a test' | awk '{print $1$3}'  # prints 'thisa'
echo 'this is a test' | awk '{print NR "." $1 "->" $(NF-2)}' # 1.this->is, NR is the current line number
```

how to use them for splitting on a different delimiter

``` bash
echo 'this-is-a test' | awk 'BEGIN{FS="-"}{print $1}' # prints "this"
```

### basic if statement

``` bash
echo 'this is a test' | awk '{if($(NF-2) == "is"){print $1}}'
```

### variables

``` bash
echo 'this is a line \n this is another line' | awk '{lines+=1}END{print "Total:", lines}' #Total: 2
```

