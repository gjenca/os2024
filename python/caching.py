
def cache_f(f):

    remember={}

    def ret_f(x):

        if x in remember:
            return remember[x]
        else:
            remember[x]=f(x)
            return remember[x]
    return ret_f

