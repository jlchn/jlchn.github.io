---
layout: default
title: Python Cheatsheet
description: Python if else else if, Python loop, Python Tuple, Python list, Python Map, Python String
parent: Python
nav_order: 1
has_children: false
---


# basic types, operators, expressions

# control flow

## if, if else, else if

``` python
# if, elif, else, and, or
flag_1 = 'a'
flag_2 = 'd'
if flag_1 == 'a' and flag_2 == 'd':
    print('best')
elif flag_1 == 'a' or flag_2 == 'd':
    print('not so good')
else:
    print('bad')

fruit = ['banana' , 'apple']

# in, not in
if 'apple' in fruit:
    print('yes')
if 'orange' not in fruit:
    print('yes')

# is list empty
empty_list = []

if empty_list:
    print(empty_list)
else:
    print('it is empty')

```
## loops (for, foreach, while, break, continue)

### for



```python
for v in range(0, 3):
    print(v)
[output]
0
1
2

i = 0
while i < 5:
    print(i)
    i += 1

while True:
    message = input("please input")
    if message == 'quit':
        break
    print(message)
```

## switch

 
- no switch-case in python


# object or struct

# pointers

# functions


```python

def create_user(name, age, sex = 'M'): # create a method with default parameter values
    user = {}
    user['name'] = name
    user['age'] = age
    user['sex'] = sex
    print(user)
    return user

create_user('jiangli', 34 )
create_user() # TypeError: create_user() missing 2 required positional arguments: 'name' and 'age'
create_user(age = 34, name = 'my-name' ) # named parameter, parameter sequence can be different from defination
create_user('jiangli', 34, 'F' )

# pass arbitrary items in a tuple
def show_hobby(name, *hobbies):
    print(hobbies)
    for hobby in hobbies:
        print(hobby)
show_hobby('my-name', 'singing', 'dancing')


# pass arbitrary key values
def show_profile(name, **profiles):
    print(profiles)
    for k, v in profiles.items():
        print(k + ": " + v)
show_profile('my-name', addrss='Rd. 5', phone='88888888')
```

### scope and external variables

## pass by value and pass by reference

## dynamic length variable

# array

### array to stream

## array to map

# list 

### initialization


```python
fruit = ['apple', 'banana', 3 , 5 ]
print(fruit) # ['apple', 'banana', 3, 5]
numbers = list(range(0,3))
print(numbers)
[output]
0
1
2
squares = [v**2 for v in range(0,2)]
print(squares)
```
### access via index


```python
fruit = ['apple', 'banana', 3 , 5 ]
print(fruit[0])  # apple
print(fruit[-1]) # 5
```
 tuple
``` python
fruit = ('apple', 'banana', 3 , 5 ) # ('apple', 'banana', 3, 5)
print(fruit[0])  # apple
print(fruit[-1]) # 5

```
### add, upate the list


```python
fruit = ['apple', 'banana', 3 , 5 ]
fruit[0] = 'orange'
fruit.insert(0, 'all fruit: ')
fruit.append('all good')

```
 tuple

python tuple is not allowed to be updated, only assignment allowed
``` python
fruit = ('apple', 'banana', 3 , 5 )
fruit = ('orange')

```
### delete from the list



```python
fruit = ['apple', 'banana', 3 , 5 ]
del(fruit[0])
del(fruit[-1])
print(fruit)          # ['banana', 3]
poped = fruit.pop()   # delete the last one then return it
poped = fruit.pop(1)  # delete the 2rd one then return it
fruit.remove(3)       # delete according to specific value, this will only delete the first occurance value

fruit = ['apple', 'banana', 'banana' ]
while f in fruit:
    fruit.remove(f)

```
 tuple

python tuple is not allowed to be deleted

### traverse the list


```python
fruit = ['apple', 'banana', 3 , 5 ]
for f in fruit:
    print(f)

while fruit:
    poped = fruit.pop()
    print(poped)

```
 tuple

``` python
fruit = ('apple', 'banana', 3 , 5 )
for f in fruit:
    print(f)

```
### slice the list



```python

fruit = ['apple', 'banana', 3 , 5 ]
print(fruit[0:2]) # ['apple', 'banana']
print(fruit[2:]) # [3, 5]
print(fruit[:2]) # ['apple', 'banana']

```
 tuple

``` python
fruit = ('apple', 'banana', 3 , 5 )
print(fruit[0:2]) # ('apple', 'banana')
print(fruit[2:]) # (3, 5)
print(fruit[:2]) # ('apple', 'banana')

```
### sort the list


``` python
fruit = ['apple', 'banana', 3 ]
fruit.sort()           # TypeError: '<' not supported between instances of 'int' and 'str'
fruit = ['apple', 'banana']
fruit.sort(reverse=True) # [ 'banana', 'appale' ]

temp_sort = sorted(fruit) # sort temperarily, will not change fruit
```

 tuple
``` python
fruit = ['apple', 'banana'] 
fruit.sort(reverse=True) # 'tuple' object has no attribute 'sort'
temp_sort = sorted(fruit) # sort temperarily, and return a list instead of a new tuple: ['apple', 'banana']
```

### copy the list

```python
fruit = ['apple', 'banana', 3 , 5 ]
new_fruit = fruit[:]
fruit.pop()
print(fruit)     # ['apple', 'banana', 3]
print(new_fruit) # ['apple', 'banana', 3, 5]


```

 tuple

```python
fruit = ('apple', 'banana', 3 , 5 )
new_fruit = fruit[:]

```

### reverse the list


```python
fruit = ['apple', 'banana', 3 , 5 ]
fruit.reverse()
print(fruit) # [5, 3, 'banana', 'apple']
```
### list to map 

### numeric list operations


```python
digits = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
min(digits)
max(digits)
sum(digits)
```
# map

### initialization


```python
d = {}
d = { "name": "name", "age" : 1}
print(d['name'])
```

### add, update map


```python
d = { "name": "name", "age" : 1}
d['sex'] = 'M' # add 
d['name'] = 'my_name' # update
print(d)
```

### delete from map


```python
d = { "name": "name", "age" : 1}
d['sex'] = 'M' # add 
del d['sex']
print(d)
```

### traverse the map


```python
d = { "name": "name", "age" : 1}
for k, v in d.items():
    print(k + ": " + str(v))

for k in d.keys():
    print(k)

for v in d.values():
    print(v)
```

# string

### string initialization


``` python
message = " hello, worlD "
message = ' hello, worlD '
print(message)
print(message[0]) # h
```

### length 

```python

message = ' hello, worlD '
len(message)
message.count('l') # 3
```
### to lower case and upper case


``` python
message = " hello, worlD "
print(message.upper())   # to upper case 
print(message.lower())   # to lower case
```
### trim


```python
message = " hello, worlD "
print(message.rstrip())  # remove the specified characters from right hand side of a string (By default, White spaces)
 hello, worlD
print(message.lstrip())  # remove the specified characters from left hand side of a string (By default, White spaces) 
hello, worlD 
print(message.strip())   # remove the specified characters from both left and right hand side of a string (By default, White spaces)
hello, worlD
```
### start with and end with
### contains and index of
### join and split


``` python
 print("hello," + " world") # concat 2 strings
'hello world'.split('o w')  # ['hell', 'orld']
```

### slice the string


```python 

message = 'hello world'
message[2:5] # llo
message[:5]  # hello
message[2:]  # llo world

```
### compare
### title

```python
# python
message = "hello, worlD"
print(message.title())   # convert the first character in each word to uppercase, and all other chracters to lowwercase
Hello, World 
```
# type conversion

python
``` python
age = 3
print("I am " + str(age))
age = '3'
age = int(age)
```
# date and time

# json

```python
import json

json_obj = {}
json_obj['name'] = 'my-name'
json_obj['age'] = 20

with open('1.txt', 'w') as file:
	json.dump(json_obj, file)


with open('1.txt') as file:
	contents= json.load(file)
	print(contents)

```



# module

``` python

# create a module named user
# user.py
create_user(name, age):
    print('user created')
delete_user(name):
    print('user deleted')
# end of user.py

# refer to the user module
# main_1.py
import user
# import user as u
user.create_user('my-name', 20)
user.delete_user('my-name')
# end of main_1.py

# refer to the user module with an alias name
# main_2.py
import user as u
u.create_user('my-name', 20)
u.delete_user('my-name')
# end of main_2.py

# refer to some methods of user module 
# main_3.py
from user import delete_user as d
d.delete_user('my-name')
# end of main_3.py

```

# class

``` python

# car.py
class Car:
	def __init__(self, model, year):
		self.model  = model
		self.year  = year
		self.run_meter = 0 # default value

	def describe(self):
		print(self.model + ": " + str(self.year))
		print("I have been running for "+ str(self.run_meter) + ' meters')
	def add_run_meter(self, meter):
		self.run_meter += meter


class ElectricCar(Car): # inherit from parent class
        def __init__(self, model, year):
                super().__init__(model, year) # init using parent init method
                self.battery_size = 10000
        def describe(self): # override the parent method
                super().describe()
                print("battery size: "+ str(self.battery_size))

# main.py
from car import Car, ElectricCar

car = Car('w', 2019)
car.add_run_meter(100)
car.describe()

electricCar = ElectricCar('telsla', 2019)
electricCar.add_run_meter(200)
electricCar.describe()

```
# errors and exceptions

``` python
first = input("\nFirst number: ") 
second = input("Second number: ")
try:
    answer = int(first) / int(second)
except ZeroDivisionError: 
    print("You can't divide by 0!")
else: 
    print(answer)

```

# file IO

``` python
# write to a file
with open('1.txt', 'w') as file:
	file.write('000\n123\n456\n789\n')

# append to a file
with open('1.txt', 'a') as file:
	file.write('1000\n')


# read all contents at once
with open('1.txt') as file:
	contents = file.read()
	print(contents)

# read line by line
with open('1.txt') as file:
	for line in file:
		print(line.rstrip())

# read to a list
try:
    with open('1.txt') as file:
        contents =  file.readlines()
    for line in contents:
        print(line.rstrip())
except FileNotFoundError:
    print("the file cannot be found")

```
# network IO

# object oriented programming

## object lifecycle

## object initialization

## memory nodel

## reflect 

## garbage collection


# process 

# thread

# format 

``` python
'{0} {1}'.format('good', 'boy') # good boy
'{0:.2f} {1}'.format(12.456, 'GB') # 12.46 GB
'No.{0}'.format(1)
```

# read from stdin



```python

message = input("Please input your message: ")
print(message)
```

# test

``` python
# functions.py
def get_str():
        return 'str'

def get_bool():
        return True

def get_list():
        return ['banana','apple']

# test_functions.py
import unittest
import functions as f

class FunctionsTestCase(unittest.TestCase):
	def test_get_str(self):
		self.assertEqual(f.get_str(), 'str')
		self.assertNotEqual(f.get_str(), 'str2')
	def test_get_bool(self):
		self.assertTrue(f.get_bool())
		self.assertFalse(not f.get_bool())
	def test_get_list(self):
		self.assertIn('apple', f.get_list())
		self.assertNotIn('orange', f.get_list())

unittest.main()
```

# dependency/package management
