---
layout: default
title: Git Cheatsheet
parent: Git
nav_order: 1
has_children: false
---

### 1.Undo a commit

- git reset --soft: reset `git commit`
- git reset: reset `git commit` and `git add`
- git reset --hard: reset `git commit`, `git add` and `all changes on the file`


### 2.rebase and stash
when run with `git pull --rebase`, sometimes we may get following error:
>Cannot pull with rebase: You have unstaged changes.

If we don't want to keep the changes we can do `git checkout -- <file name>` or `git reset --hard` to get rid of the changes.

If we want to keep the changes, we can run `git stash`, it stores the differences away from everything else, returning our working directory to the last commit. Once we have done our rebase, run `git stash pop`. This will return those files to the working directory and allow us to work as before.

