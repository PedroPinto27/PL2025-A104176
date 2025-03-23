from calc_lex import lexer

class Token:
    def __init__(self, type, value):
        self.type = type
        self.value = value

class Parser:
    def __init__(self, input_str):
        lexer.input(input_str)
        self.tokens = []
        while True:
            tok = lexer.token()
            if not tok:
                break
            self.tokens.append(Token(tok.type, tok.value))
        self.tokens.append(Token('EOF', None)) 
        self.pos = 0
    
    def lookahead(self):
        if self.pos < len(self.tokens):
            return self.tokens[self.pos].type
        return 'EOF'
    
    def consume(self, expected_type):
        if self.lookahead() == expected_type:
            token = self.tokens[self.pos]
            self.pos += 1
            return token
        else:
            raise SyntaxError("Erro")

    
    def operacao(self):
        result = self.calc()
        while self.lookahead() in ['PLUS', 'MINUS']:
            if self.lookahead() == 'PLUS':
                self.consume('PLUS')
                result = result + self.calc()
            elif self.lookahead() == 'MINUS':
                self.consume('MINUS')
                result = result - self.calc()
        return result
    
    def calc(self):
        result = self.factor()
        while self.lookahead() in ['TIMES', 'DIVIDE']:
            if self.lookahead() == 'TIMES':
                self.consume('TIMES')
                result = result * self.factor()
            elif self.lookahead() == 'DIVIDE':
                self.consume('DIVIDE')
                result = result / self.factor()
        return result
    
    def factor(self):
        if self.lookahead() == 'NUMBER':
            token = self.consume('NUMBER')
            return token.value
        elif self.lookahead() == 'LPAREN':
            self.consume('LPAREN')
            result = self.operacao()
            self.consume('RPAREN')
            return result
        else:
            raise SyntaxError("Erro")
    
    def parse(self):
        result = self.operacao()
        if self.lookahead() != 'EOF':
            raise SyntaxError("Expressão incompleta")
        return result

def main():
    exemplos = [
        "2+3",
        "67-(2+3*4)",
        "(9-2)*(13-4)"
    ]
    
    for exp in exemplos:
        parser = Parser(exp)
        result = parser.parse()
        print(f"Exemplo: {exp} = {result}")

if __name__ == "__main__":
    main()