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
