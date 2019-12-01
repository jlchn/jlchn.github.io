
import os, sys, re

regex = r"---(.*)---"
root = './docs/';
class Dir(object):
 
     def __init__(self, path, title, order):
         self.path = path
         self.title = title
         self.order = int(order)
         self.children = []
 
     def __lt__(self, other):
         return self.order < other.order

def match_block(content):
    matches = re.search(regex, content, re.MULTILINE | re.DOTALL)
    if not matches:
        print('no description block found in ' + sub_root_file)
        exit(1)
    return matches.group(1).strip().split('\n')

def find_property(file, lines, name):
    for line in lines:
        if line.startswith(name):
            return line.split(':')[1].strip();
    print('{0} is not found in {1} ', name, sub_root_file)
    exit(1)

dirs = []
for dir in os.listdir(root):
    if os.path.isdir(root + dir):
        sub_root_file = root + dir + '/' + dir + '.md'
        if not os.path.exists(sub_root_file):
            print(sub_root_file + " doesn't exist!")
            exit(1)
        with open(sub_root_file) as file:
            lines = match_block(file.read())
            dirs.append(Dir(sub_root_file, find_property(sub_root_file, lines, 'title'), find_property(sub_root_file, lines, 'nav_order')))

dirs.sort()
for dir in dirs:         
    print(dir.title + ' ' + str(dir.order))
                

