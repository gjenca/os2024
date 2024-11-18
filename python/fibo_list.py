#!/usr/bin/env python3

def fibo(upto):

    a,b=0,1
    ret=[]
    for n in range(upto):
        ret.append(a)
        a,b=b,a+b
    return ret
