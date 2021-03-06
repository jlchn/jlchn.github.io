---
layout: default
title: Shell
nav_order: 100
has_children: false
---

### display files 

```bash
ls -d # display directory only
ls -t | head -1 # get last edited file(by last modified time)
ls -rt # order last edited file in reverse order(by last modified time)
ls -R # list in recursive way
ls -1 # display one file name per line
ls -h # display file size with human readable formats
ls -i # display with inode number
ls -n #display with uid and gid
```

### add two integers

``` bash
num=$(($num1 + $num2)) 
num=$(awk "BEGIN {print $num1+$num2; exit}") # for floating point

```

### execution tracing

``` bash
bash -x 1.sh # commandline

set -x # enable execution tracing
set +x # disable execution tracing

```

### variables

``` bash
v1=this_is_a_variable # there shouldn't be spaecs before or after =
v2 = "this is a variable" use "" if there are blanks in the string
echo $v1 # get value of variable
echo "$v1 and $v2"

```

### parameter expansion

`${parameter:-word}`: If parameter is unset or null, the expansion of word is substituted. Otherwise, the value of parameter is substituted.

`${parameter:?word}`: If parameter is null or unset, the expansion of word (or a message to that effect if word is not present) is written to the standard error and the shell, if it is not interactive, exits. Otherwise, the value of parameter is substituted.

let's create a file named `test.sh`:

``` bash
#! /bin/bash
filename=${1:-~/tmp/test.txt}  
echo $filename
filetype=${2:?filetype should be provided!}
```
run `test.sh`

``` bash
bash test.sh file1.sh
file1.sh
filetype should be provided!
```

### printf

printf is more powerful than echo

``` bash
v1=1
printf "$1\n" # printf will not help append \n after the string
printf "hi %s, to be NO.%d" "Jackson" 1

```

### standard inut, standard output, standard error

the standard inut, standard output, standard error are all terminal, we can check by only using `cat` in the terminal and try to type anyting.

``` bash
cat
```

### use > < >> to redirect the standard inut, standard output, standard error

``` bash
cat < 1.sh
cat < 1.sh >> 2.sh 
```


### show ports and process that owns them

``` bash
sudo lsof -i
sudo netstat -lptu
sudo netstat -tulpn
```
### get result of a command
``` bash
result=$(pwd)
result=`pwd`
```

### get exit code of a command
``` bash
grep "^$username" $PASSWD_FILE > /dev/null ; result=$?; echo $result;
```

### add timestamp to filename
``` bash
REMOTE_FILE="/tmp/$(date "+%Y%m%d%H%M%S").sh"
```
kill by port
``` bash
sudo kill -9 $(sudo lsof -t -i:9001)
```

### history
``` bash
history #history list
!998 #repeat n-th command
!ps #repeat the last command that has been executed starting with 'ps'  
```

### grep
``` bash
grep 'warning\|error\|critical' /var/log/messages #find appearances in a file
grep -w 'warning\|error\|critical' /var/log/messages #find words in a file
grep -r '172.26.131.131' . find recursively
grep -rnw '/path/to/somewhere/' -e 'some texts' # find text in folder files 
grep -vE "websocket" # invert match, selected lines are those not matching any of the specified patterns
```
### line count

``` bash
wc -l 
```

find files bigger than 4MB

``` bash
find . -type -f -size +4M
```

### cut: get columns

``` bash 
ls -l | cut -c 1-10 # print first 10 character in each line
ls -l | cut -c 1,10 # print the first and the tenth character in each line
cut -d : -f 1,5 /etc/passwd # print the login name and full name of each user, using : as delimeter

```


### tee
used to store and view(at the same time) the output of any other command

example
``` bash 
ls | tee file1 #write to stdout, as well as a file
ls | tee -a file2 # append to file
ls | tee file1 | sed 's/old/new/' #write to stdout, and also pass to a command
ls | tee file1 file2 file3 #write the output to multiple files 
```

### find the first n lines 

``` bash
$ head -n 5 /etc/passwd # using head
$ head -n 5 /etc/passwd /etc/hosts # check two files at the same time
$ sed -n 1,5p /etc/passwd # using sed
$ awk 'FNR <= 5' /etc/passwd # using awk

```

### sort

``` bash
sort -r -u -t : -k 5,5 /etc/passwd # unique sort in the reverse order using the values in the fifth column, using : as column delimeter
sort -r -u -t : -k 5 -n /etc/passwd # the same with the above, but evaluate as numbers for comparison
sort -t : -k3nr -k1 /etc/passwd # sort using the number values in the third column in reverse order, than sort using the values in the first column.
```

### tar
``` bash
tar -cvf backup.tar /home/jenkins #create a tar
tar -xvf backup.tar #extract a tar
tar -tvf backup.tar #view tar contains
```
### compare two folders
``` bash
diff -arq folder1 folder2
git diff --no-index dir1/ dir2/
```

### translate characters (tr)

``` bash
# translate some character to the upper case
echo "welcome to shanghai" | tr "az" "AZ" # welcome to shAnghAi
echo "welcome to shanghai" | tr "a-z" "A-Z" # WELCOME TO SHANGHAI
echo "welcome to shanghai" | tr "we" "aa" # aalcoma to shanghai
echo "welcome to {shanghai}" | tr "{}" "()" # welcome to (shanghai)

# squeeze repetition of characters using -s
echo "welcome   to    {shanghai}" | tr -s " " "S" # welcomeStoS{shanghai}
# delete specified characters using -d option
echo "welcome   to    {shanghai}" | tr -d " " # welcometo{shanghai}
# remove all the digits from the string
echo "welcome  2  {shanghai}" | tr -d "[0-9]"
echo "welcome  2  {shanghai}" | tr -d "[:digit:]" 

# opposite meaning of set1
echo "The number is 12" | tr -cd [:digit:] # 12
echo "aaabbb" | tr -c "a" "c" # aaaccc


```

### rsync
#### pull
``` bash
rsync -rave "ssh -i ${WORK_TERMINAL_PEM}" ubuntu@${WORK_TERMINAL_IP}:"${BASE_DIR}/${REMOTE_PATH}" ${LOCAL_PATH}rsync -rave "ssh -i ${WORK_TERMINAL_PEM}" ubuntu@${WORK_TERMINAL_IP}:"${BASE_DIR}/${REMOTE_PATH}" ${LOCAL_PATH}
```

#### push
``` bash 
rsync -rave  "ssh -i /home/jiangli/Documents/AWS/pem/hue-operation-tool-work-terminal.pem" di.py ubuntu@13.112.122.215:"/tmp/abc.test"
```
#### delete mode
--delete

### zip with password
``` bash
zip --password (password) file.zip files
```
### if else
``` bash
if [ "$PASSWORD" == "$VALID_PASSWORD" ]; then
echo "You have access!"
else
echo "ACCESS DENIED!"
fi
```

### case

``` bash 
case "${REMOTE_FILE_TYPE}" in

   "py") ssh -i ${WORK_TERMINAL_PEM}  ubuntu@${WORK_TERMINAL_IP} "py ${REMOTE_FILE} ${REMOTE_FILE_PARAMETERS}"
   ;;

   "yml" | "yaml") ssh -i ${WORK_TERMINAL_PEM}  ubuntu@${WORK_TERMINAL_IP} "ansible-playbook ${SCRIPT_ROOT_DIR}/${REMOTE_FILE} -i ${SCRIPT_ROOT_DIR}/inventory ${REMOTE_FILE_PARAMETERS}"
   ;;

   *) ssh -i ${WORK_TERMINAL_PEM}  ubuntu@${WORK_TERMINAL_IP} "bash ${REMOTE_FILE} ${REMOTE_FILE_PARAMETERS}"
   ;;

esac
```


### command options and interactive mode
``` bash
#! /bin/bash
set -e

function usage()
{
echo "-v -f -h";
}
interactive=
filename=~/system_page.html

while [ "$1" != "" ]; do
    case $1 in
        -f | --file )           shift
                                filename=$1
                                ;;
        -v)                     set -x
                                ;;
        -h | --help )           usage
                                exit
                                ;;
        -i )                    interactive=1
                                ;;
    esac
    shift
done


if [ "$interactive" = "1" ]; then

    response=

    echo -n "Enter name of output file [$filename] > "
    read response
    if [ -n "$response" ]; then
        filename=$response
    fi

    if [ -f $filename ]; then
        echo -n "Output file exists. Overwrite? (y/n) > "
        read response
        if [ "$response" != "y" ]; then
            echo "Exiting program."
            exit 1
        fi
    fi
fi


echo $filename

```
### /dev/null

a special file that data redirected to this file will be dropped by the os.

it would be very useful if we only want the exit code of a program instead of the output.

``` bash 
if grep "test" 2.sh > /etc/null
then
        echo "1"
else
        echo "2"
fi

```

### check if it is hard disk or SSD
0 is SSD and i is the hard disk.

``` bash
lsblk -d -o name,rota
NAME ROTA
xvda    0
xvdf    0

```

