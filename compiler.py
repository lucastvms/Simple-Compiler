import sys

def infixa_posfixa(expressions):
    posfixa = []
    for exp in expressions:
        exp = exp.split(' ')
        if (len(exp) == 4):
            expression = [exp[0], exp[2], exp[1]]
            posfixa.append(expression)

        elif (len(exp) == 6):
            expression = [exp[0], exp[2], exp[4], exp[3], exp[1]]
            posfixa.append(expression)
    return posfixa