import sys, re

class Lexer:
    def __init__(this):
        this.tokens_da_linguagem = [
            (r'[ \t\n]+', None),
            (r'#[^\n]*', None),
            (r'[A|B|C]', 'VAR'),
            (r'[=]', 'IGUAL'),
            (r'[+]', 'SOMA'),
            (r'[-]', 'SUB'),
            (r'[*]', 'MULT'),
            (r'[/]', 'DIV'),
            (r'[;]', 'SEPARADOR'),
            (r'[0|1|2|3|4|5|6|7|8|9]*', 'DIGITO')
        ]

    def analise_lexica(this, programa):
        posicao = 0
        tokens_identificados = []
        while posicao < len(programa):
            match = None
            for token_da_linguagem in this.tokens_da_linguagem:
                padrao, identificador = token_da_linguagem
                regex = re.compile(padrao)
                match = regex.match(programa, posicao)
                if match:
                    padrao_identificado = match.group(0)
                    if identificador:
                        token = (padrao_identificado, identificador)
                        tokens_identificados.append(token)
                    break
            if not match:
                sys.stderr.write('Problema no programa: %s\n' % programa[posicao])
                sys.exit(1)
            else:
                posicao = match.end(0)
        return tokens_identificados
