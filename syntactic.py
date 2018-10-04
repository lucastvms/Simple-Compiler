import sys

class Token:
    def interpretar(this):
        return None

class Atribuicao (Token):
    def __init__(this, a, b, c, operacao):
        this.a = a
        this.b = b
        this.c = c
        this.operacao = operacao

    def interpretar(this):
        if this.c:
            return this.a + ' = ' + this.b + ' ' + this.operacao + ' ' + this.c + ' ;'
        return this.a + ' = ' + this.b + ' ;'

class Syntatic:
    def __init__(this):
        pass

    def atribuicao (this, tokens, pos):

        OPS = {'+': "SOMA", '-': "SUB", '*': "MULT", '/': "DIV"}


        # operações simples
        # A = 1;
        if len(tokens) >= (pos+4):
            if tokens[pos][1] == 'VAR' and tokens[pos+1][1] == 'IGUAL' and tokens[pos+2][1] == 'DIGITO' and tokens[pos+3][1] == 'SEPARADOR':
                return ((pos+4), Atribuicao(tokens[pos][0], tokens[pos+2][0], None, None))
        # A = B;
        if len(tokens) >= (pos+4):
            if tokens[pos][1] == 'VAR' and tokens[pos+1][1] == 'IGUAL' and tokens[pos+2][1] == 'VAR' and tokens[pos+3][1] == 'SEPARADOR':
                return ((pos+4), Atribuicao(tokens[pos][0], tokens[pos+2][0], None, None))

        # operações compostas

        # A = B op C;
        if len(tokens) >= (pos+6):
            if tokens[pos][1] == 'VAR' and tokens[pos+1][1] == 'IGUAL':
                if tokens[pos+2][1] == 'VAR' and tokens[pos+3][0] in OPS and tokens[pos+4][1] == 'VAR':
                    if tokens[pos+5][1] == 'SEPARADOR':
                        return ((pos+6), Atribuicao(tokens[pos][0], tokens[pos+2][0], tokens[pos+4][0], tokens[pos+3][0]))

        # A = 1 op 2;
        if len(tokens) >= (pos+6):
            if tokens[pos][1] == 'VAR' and tokens[pos+1][1] == 'IGUAL':
                if tokens[pos+2][1] == 'DIGITO' and tokens[pos+3][0] in OPS and tokens[pos+4][1] == 'DIGITO':
                    if tokens[pos+5][1] == 'SEPARADOR':
                        return ((pos+6), Atribuicao(tokens[pos][0], tokens[pos+2][0], tokens[pos+4][0], tokens[pos+3][0]))

        # A = B op 1
        if len(tokens) >= (pos+6):
            if tokens[pos][1] == 'VAR' and tokens[pos+1][1] == 'IGUAL':
                if tokens[pos+2][1] == 'VAR' and tokens[pos+3][0] in OPS and tokens[pos+4][1] == 'DIGITO':
                    if tokens[pos+5][1] == 'SEPARADOR':
                        return ((pos+6), Atribuicao(tokens[pos][0], tokens[pos+2][0], tokens[pos+4][0], tokens[pos+3][0]))

        # A = 1 op B
        if len(tokens) >= (pos+6):
            if tokens[pos][1] == 'VAR' and tokens[pos+1][1] == 'IGUAL':
                if tokens[pos+2][1] == 'DIGITO' and tokens[pos+3][0] in OPS and tokens[pos+4][1] == 'VAR':
                    if tokens[pos+5][1] == 'SEPARADOR':
                        return ((pos+6), Atribuicao(tokens[pos][0], tokens[pos+2][0], tokens[pos+4][0], tokens[pos+3][0]))
        #END
        return (pos, None)

    def analise_sintatica(this, tokens):
        pos = 0
        programa = []
        while pos < len(tokens):
            posAtual, att = this.atribuicao(tokens, pos)
            if pos != posAtual:
                programa.append(att)
                pos = posAtual
            else:
                sys.stderr.write('Problema no programa: %s\n' % pos)
                sys.exit(1)
        return programa

