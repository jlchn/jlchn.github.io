---
layout: default
title: [File System] inode
parent: Operating System
nav_order: 15
has_children: false
---

An inode is a data structure on a filesystem on Linux that stores all the information about a file except its name and its actual data.

When a file is created, it is assigned both a name and an inode number, which is an integer that is unique within the filesystem. 

Both the file names and their corresponding inode numbers are stored as entries in the directory that appears to the user to contain the files. That is, the directory associates file names with inodes.

Whenever a user or a program refers to a file by name, the operating system uses that name to look up the corresponding inode, which then enables the system to obtain the information it needs about the file to perform further operations. 

When a new hard link to a file is created, both links share the same inode number because the link is only a pointer, not a copy of the file.

There are two ways in which a filesystem can run out of space: it can consume all the space for adding new data (i.e., to existing files or to new files), or it can use up all the inodes

It is particularly easy to run out of inodes if a filesystem contains a very large number of very small files. 

To see how many free inodes available , use `df -hi` to check `ifree` column

``` bash
df -ih

Filesystem      Size   Used  Avail Capacity iused      ifree %iused  Mounted on
/dev/disk1     112Gi  104Gi  7.5Gi    94% 1669596 4293297683    0%   /
devfs          195Ki  195Ki    0Bi   100%     676          0  100%   /dev
```

To check the inode of a specific file, use `ls -i file-name`

```bash
ls -i workspace

12252448
```

To check which process is occupying `pi` file, use `lsof` with `grep`

``` bash
lsof | grep 12252448

zsh        2585 jiangli  cwd       DIR                1,4        170 12252448 workspace
```


