#!/usr/bin/env python3

a,b=0,1
n=0
while n<100:
    n=n+1
    print(n,a)
    a,b=b,a+b
print('Finito')

