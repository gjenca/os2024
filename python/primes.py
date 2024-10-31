#!/usr/bin/env python3
import math

def primes(to,from_=2):

    ret=[]
    for n in range(from_,to):
        for d in range(2,int(math.sqrt(to))):
            if n % d == 0:
                break
        else:
            ret.append(n)
    return ret


nohy=4

print('som importovany')

#print(primes(50))
#print(primes(50,10))
