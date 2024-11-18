#!/usr/bin/env python3

def fibo(upto):

    a,b=0,1
    for n in range(upto):
        yield a        
        a,b=b,a+b

