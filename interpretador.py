import sys, operator
from syntactic import Syntatic
from lexer import Lexer

class Core:
    def __init__(this):
        this.code = 'B = 1; ' \
               'B = B; ' \
               'A = 2 + 2; ' \
               'A = B - B; ' \
               'A = 100; ' \
               'A = B + 1000; ' \
               'A = B / 2; ' \
               'C = A;'
        print(this.code)
        this.lista_exp = []
        this.lexer = Lexer()
        this.syntactic = Syntatic()
        this.run()

    def run(this):
        # LÉXICO
        print("\n==LÉXICA: ==")
        tokens = this.lexer.analise_lexica(this.code)
        print(tokens)

        # SINTÁTICO
        print("\n==SINTÁTICA: ==")
        programa = this.syntactic.analise_sintatica(tokens)
        print(programa)

        for token in programa:
            print(token.interpretar())
            this.lista_exp.append(token.interpretar())

        # PÓSFIXA
        print("\n==PÓSFIXA: ==\n" + str(this.lista_exp))
        posfixa = this.infixa_posfixa(this.lista_exp)
        print(posfixa)
        # RESULTADO
        this.calcula(posfixa)

    def infixa_posfixa(this, expressions):
        #Compiler
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

    def calcula(this, posfixa):
        cont = 1
        dicio = {'A': None, 'B': None, 'C': None}
        ops = {"+": operator.add, "-": operator.sub, "*": operator.mul, "/": operator.truediv}
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

            print("\n==DICIONÁRIO: " + str(cont) + " ==")
            print(dicio)

            cont += 1

        return resultado

if __name__ == "__main__":
    Core()


