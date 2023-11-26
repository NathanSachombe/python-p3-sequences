#!/usr/bin/env python3

def print_fibonacci(length):
    a = 0
    b = 1
    for i in range(0,length):
        print(a,end = " ")
        c=a+b
        a=b
        b=c

print_fibonacci(0)
print_fibonacci(1)
print_fibonacci(2)
print_fibonacci(10)


