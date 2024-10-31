#!/usr/bin/env python3


def f(a,b,c='bum',d='bac'):

    print(a,b,c,d)

f(1,2)
f(1,2,'BUM')
f(1,2,d='BAC')

def g(*argl,**argd):

    print(argl,argd)

g(1,2,3,slon=4,pstros=2)

y=2

def h(x):

    global y

    print(x,y)
    y=5

h(1)
print('y=',y)

