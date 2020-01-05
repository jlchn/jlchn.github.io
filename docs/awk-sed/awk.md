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
### read inputs from a file

create a file named `score-test.txt`

```
1 Dell Math 97
2 Dell English 99
3 Jackson Math 78
4 Jackson English 66
```
read lines in `score-test.txt`
``` bash
awk '{print $0}' score-test.txt
```

### execute commands in a file

create a file named `commands-1.awk`
``` bash
{print $0}
```
execute:

``` bash
awk -f commands-1.awk score-test.txt 
```
### set variable in the command line

``` bash
awk -v name=Jack '{printf "Name: %s\n", name }' score-test.txt
Name: Jack
Name: Jack
Name: Jack
Name: Jack
```

### print the third and fourth columns in the file

``` bash
awk '{print $3,$4 }' score-test.txt
Math 97
English 99
Math 78
English 66

awk '{print $3 "\t"  $4 }' score-test.txt
Math    97
English 99
Math    78
English 66

```

### print scores of Math

``` bash
awk '/Math/ {print $3,$4 }' score-test.txt # lines containing Math
Math 97
Math 78
```

### print line count containing Math

``` bash
awk '/Math/{++count} END {print "Count = ", count}' score-test.txt
Count =  2
```

### build-in variables

#### ARGV and ARGC

commandline parameter count and values

create a file named `commands-2.awk` with below commands

``` bash
BEGIN {
    printf "argument count: %d\n", ARGC

    for ( i = 0; i < ARGC; i++ ){
        printf "ARGV[%d] = %s\n", i, ARGV[i]
    }
}
```

``` bash 
awk -f commands-2.awk score-test.txt a b c d
argument count: 6
ARGV[0] = awk
ARGV[1] = score-test.txt
ARGV[2] = a
ARGV[3] = b
ARGV[4] = c
ARGV[5] = d

```

#### ENVIRON, FILENAME, FS, NR and NF
- ENVIRON: environment variable array
- FILENAME: name of inputs file(score-test.txt)
- FS: field seperator, blank as default
- NR: Line number of record(how many lines in a file)
- NF: column number of of a line(how many columns in a line)

create a file named `commands-3.awk` with below commands

``` bash
BEGIN {
    print length(ENVIRON) # length of env list
    print ENVIRON["USER"] # user name
    print FS
    print FILENAME # empty
    print NR, NF   # 0 0
}

{
    print ENVIRON["USER"]
    print FILENAME
    print NR, NF
}
```

### assigment, if, if else

``` bash
BEGIN {
    a = 50
    b = 20
    printf "a + b = %d\n", a + b
    printf "a - b = %d\n", a - b
    printf "a * b = %d\n", a * b
    printf "a / b = %f\n", a / b
    printf "a++ = %d\n",  a++
    printf "++a = %d\n",  ++a

    if ( a != b ){
        print "a != b\n"
    }
    if ( a <= b ){
        print "a <= b\n"
    } else {
        printf "a > b\n"
    }
    
    a > b ? max = a : max = b;
    printf "max= %d\n", max

    str1 = "str1"
    str2 = "str2"
    str3 = str1 str2 # string concat
    print str3,"\n"
}

```

### two dimension array

```
1 2 3
4 5 6
7 8 9
```



### regex

```
 awk '/Ma.h/ {print $0}' score-test.txt  
1 Dell Math 97
3 Jackson Math 78
awk '/M.*/ {print $0}' score-test.txt 
1 Dell Math 97
3 Jackson Math 78

```
