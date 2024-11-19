import caching
import functools

def comb(n,k):

    if n==k:
        return 1
    elif k==0:
        return 1
    else:
        return comb(n-1,k)+comb(n-1,k-1)

#@caching.cache_f
@functools.cachecomb_pair
def comb_pair(pair):

    n,k=pair
    if n==k:
        return 1
    elif k==0:
        return 1
    else:
        return comb_pair((n-1,k))+comb_pair((n-1,k-1))

remember={}

def comb_fast(n,k):

    if (n,k) in remember:
        return remember[(n,k)]
    if n==k:
        return 1
    elif k==0:
        return 1
    else:
        remember[(n,k)]=comb_fast(n-1,k)+comb_fast(n-1,k-1)
        return remember[(n,k)]

