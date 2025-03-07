import os
import sys
import ply.lex as lex

tokens = (
    "SELECT",
    "VARIABLE",
    "WHERE",
    "LC",
    "RC",
    "ATTRIBUTE",
    "STRING",
    "INTEGER",
    "ID",
    "DOT",
    "COMMENT",
    "LIMIT"
)

def t_SELECT(t):
    r'[Ss][Ee][Ll][Ee][Cc][Tt]'   
    return t

def t_VARIABLE(t):
    r'\?\w*'
    return t

def t_WHERE(t):
    r'[Ww][Hh][Ee][Rr][Ee]'
    return t

def t_LC(t):
    r'{'
    return t

def t_RC(t):
    r'}'
    return t

def t_ATTRIBUTE(t):
    r'a'
    return t

def t_STRING(t):
    r'"([^"]+)"@([a-zA-Z]*)'
    return t

def t_INTEGER(t):
    r'\d+'
    return t

def t_ID(t):
    r'\w+:\w+'
    return t

def t_DOT(t):
    r'\.'
    return t

def t_COMMENT(t):
    r'\#.*$'
    return t

def t_LIMIT(t):
    r'[Ll][Ii][Mm][Ii][Tt]'
    return t

t_ignore = " \n"

def t_error(t):
    print(f"Caractere ilegal: {t.value[0]}")
    t.lexer.skip(1)

lexer = lex.lex()

def main():
    if len(sys.argv) != 2:
        print("python3 <path>")
        sys.exit(1)

    input_filename = sys.argv[1]

    output_filename = os.path.join(os.path.dirname(input_filename), "output.txt")

    print(f"Arquivo {input_filename} convertido para {output_filename}")
    try:
        with open(input_filename, "r") as file:
            with open(output_filename, "w") as output_file:
                for line in file:
                    lexer.input(line)
                    for token in lexer:
                        output_file.write(f"Token: {token.type}, Valor: {token.value}\n")
    except FileNotFoundError as e:
        print(f"Erro: Arquivo '{input_filename}' não encontrado. Detalhes: {e}")
    except Exception as e:
        print(f"Erro inesperado: {e}")

if __name__ == "__main__":
    main()