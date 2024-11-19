
def apply_f(f,x):

    return f(x)

def compose(f,g):

    def ret_fun(x):

        return f(g(x))

    return ret_fun

def add_n(n):

    def ret_fun(k):
        return k+n

    return ret_fun

def debug_print(f):

    def ret_fun(x):

        print(f'Called {f.__name__}({x})')
        return f(x)

    return ret_fun
