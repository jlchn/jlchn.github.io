---
layout: default
title: Git Cheatsheet
parent: Git
nav_order: 1
has_children: false
---


### git branch

``` bash
# rename local branch
git branch -m oldname newname
# rename current branch
git branch -m newname

```

### git commit 

``` bash
# update commit message
git commit --amend -m 'second'
```

### git reset(undo)

``` bash
# reset a file from staging to untracked
git reset a.file
# reset all files from staging to untracked
git reset

# reset `git commit`(reset to staging state of a commit)
git reset --soft HEAD~1
# reset `git commit` and `git add`(reset to untracked state of a commit)
git reset HEAD~1
# reset `git commit`, `git add` and `all changes will lost`
git reset --hard  HEAD~1
```
### git clean

``` bash
# clean untracked files
git clean
# this will delete files and folders
git clean -fd
```

### git merge

``` bash
git checkout develop
git checkout -b ticket-xxx-squash
git merge --squash ticket-xxx
git commit -m "My feature complete"
git push origin ticket-xxx-squash:ticket-xxx

# merge the last 3 commits
git reset --soft HEAD~3
git commit --amend


```

### rebase and stash
when run with `git pull --rebase`, sometimes we may get following error:
>Cannot pull with rebase: You have unstaged changes.

If we don't want to keep the changes we can do `git checkout -- <file name>` or `git reset --hard` to get rid of the changes.

If we want to keep the changes, we can run `git stash`, it stores the differences away from everything else, returning our working directory to the last commit. Once we have done our rebase, run `git stash pop`. This will return those files to the working directory and allow us to work as before.

``` bash
git stash list
git stash apply stash@{n}
```

### git ignore

``` bash
# stop tracking and ignore changes to a file
git rm -r --cached 
git add .
git commit -m 'fixing .gitignore'
```