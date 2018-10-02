import sys
import operator

from syntactic import analise_sintatica
from lexer import analise_lexica, tokens_da_linguagem
from compiler import infixa_posfixa



def calcula(posfixa):
    cont = 1
    dicio = {'A': None, 'B': None, 'C': None}
    ops = { "+": operator.add, "-": operator.sub, "*": operator.mul, "/": operator.truediv}
    resultado = []

    for exp in posfixa:

        # expressões simples
        if (len(exp) == 3):
            # caso A = 1
            if(exp[1] not in ('A', 'B', 'C')):
                dicio[exp[0]] = int(exp[1])
            #caso A = B
            else:
                if(dicio[exp[1]] != None):
                    dicio[exp[0]] = dicio[exp[1]]
                else:
                    sys.stderr.write('Problema no programa: %s\n' % exp)
                    sys.exit(2)

        # expressões compostas
        if (len(exp) == 5):
            # ERRO: A = None + 1
            if(exp[1] in ('A', 'B', 'C') and dicio[exp[1]] == None):
                sys.stderr.write('Problema no programa: %s\n' % exp)
                sys.exit(2)

            # ERRO: A = 1 + None
            if (exp[2] in ('A', 'B', 'C') and dicio[exp[2]] == None):
                sys.stderr.write('Problema no programa: %s\n' % exp)
                sys.exit(3)

            #SOMAS
            # A = 1 + valor
            if (exp[1] not in ('A', 'B', 'C')):
                # A = 1 + 1
                if (exp[2] not in ('A', 'B', 'C')):
                    dicio[exp[0]] = ops[exp[3]](int(exp[1]), int(exp[2]))
                # A = 1 + B
                else:
                    dicio[exp[0]] = ops[exp[3]](int(exp[1]), dicio[exp[2]])

            # A = B + valor
            else:
                # A = B + 1
                if (exp[2] not in ('A', 'B', 'C')):
                    dicio[exp[0]] = ops[exp[3]](dicio[exp[1]], int(exp[2]))
                # A = B + C
                else:
                    dicio[exp[0]] = ops[exp[3]](dicio[exp[1]], dicio[exp[2]])

        print()
        print("==DICIONÁRIO: " + str(cont) + " ==")
        print(dicio)

        cont += 1

    return resultado


code = 'B = 1; B = B; A = 2 + 2; A = B - B; A = 100; A = B + 1000; A = B / 2; C = A;'

# LÉXICO
print()
print("==LÉXICA: ==")
tokens = analise_lexica(code, tokens_da_linguagem)
print(tokens)

# SINTÁTICO
print()
print("==SINTÁTICA: ==")
programa = analise_sintatica(tokens)
print (programa)

for token in programa:
    print(token.interpretar())

# PÓSFIXA
print()
print("==PÓSFIXA: ==")

lista_exp = []

for token in programa:
    lista_exp.append(token.interpretar())
print(lista_exp)

posfixa = infixa_posfixa(lista_exp)
print(posfixa)

# RESULTADO
resultado = calcula(posfixa)
