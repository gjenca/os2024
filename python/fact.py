import func

@func.debug_print
def fact(n):

    if n==0:
        return 1
    else:
        return n*fact(n-1)

# fact=func.debug_print(fact)

