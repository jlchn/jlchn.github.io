BEGIN {
    printf "argument count: %d\n", ARGC

    for ( i = 0; i < ARGC; i++ ){
        printf "ARGV[%d] = %s\n", i, ARGV[i]
    }
}