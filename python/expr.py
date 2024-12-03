

import operator

oper_d={
        '+':operator.add,
        '-':operator.sub,
        '*':operator.mul,
        '/':operator.floordiv,
        }


def eval_expr(s,**var_d):

    stack=[]
    for word in s.split():
        if word in oper_d:
            a=stack.pop()
            b=stack.pop()
            stack.append(oper_d[word](a,b))
        elif word in var_d:
            stack.append(int(var_d[word]))
        else:
            stack.append(int(word))
    return stack.pop()


def eval_expr_f(s):

    stack=[]
    for word in s.split():
        if word in oper_d:
            a_f=stack.pop()
            b_f=stack.pop()
            def fun(**var_d):
                return oper_d[word](a_f(**var_d),b_f(**var_d))
            stack.append(fun)
        elif word.isdigit(): 
            value=int(word)
            def fun(**var_d):
                return value
            stack.append(fun)
        else:
            def fun(**var_d):
                nonlocal word
                value=var_d[word]
            stack.append(fun)
    return stack.pop()



