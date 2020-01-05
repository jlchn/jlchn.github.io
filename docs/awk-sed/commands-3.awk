BEGIN {
    print length(ENVIRON) # length of env list
    print ENVIRON["USER"] # user name
    print FILENAME # empty
    print FS
    print NR, NF   # 0 0
}

{
    print ENVIRON["USER"]
    print FILENAME
    print NR, NF
}

