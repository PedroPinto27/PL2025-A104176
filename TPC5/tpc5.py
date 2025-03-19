import json
import ply.lex as lex
import datetime

tokens = (
    'LISTAR',
    'MOEDA',
    'SELECIONAR',
    'SAIR',
    'CODIGO',
    'VALOR',
    'DOT'
)

t_LISTAR = r'LISTAR'
t_MOEDA = r'MOEDA'
t_SELECIONAR = r'SELECIONAR'
t_SAIR = r'SAIR'
t_CODIGO = r'[A-Z][0-9]{2}'
t_VALOR = r'(2e|1e|50c|20c|10c|5c|2c|1c)(,\s*(2e|1e|50c|20c|10c|5c|2c|1c))*'
t_DOT = r'\.'

t_ignore = ' \t'

def t_error(t):
    print(f"Caractere inválido: {t.value[0]}")
    t.lexer.skip(1)

lexer = lex.lex()

# Definição global de moedas
moedas = {
    "2e": 2.0,
    "1e": 1.0,
    "50c": 0.5,
    "20c": 0.2,
    "10c": 0.1,
    "5c": 0.05,
    "2c": 0.02,
    "1c": 0.01
}

def formatar_saldo(saldo):
    euros = int(saldo)
    centimos = int(round((saldo - euros) * 100))
    if euros > 0 and centimos > 0:
        return f"{euros}e{centimos}c"
    elif euros > 0:
        return f"{euros}e"
    else:
        return f"{centimos}c"

def listar_produtos(stock):
    print("cod   | nome       | quantidade | preço")
    print("---------------------------------------")
    
    for p in stock['stock']:
        print(f"{p['cod']:5} | {p['nome']:10} | {p['quant']:5} | {p['preco']}")

def inserir_moedas(saldo, token):
    valor = token.split(", ")
    saldo += sum(moedas[moeda] for moeda in valor if moeda in moedas)
    return saldo

def selecionar_produto(codigo, saldo, stock):
    for p in stock['stock']:
        if p['cod'] == codigo:
            if p['quant'] <= 0:
                print(f"maq: Produto {p['nome']} esgotado.")
                return saldo
            if saldo >= p['preco']:
                saldo -= p['preco']
                p['quant'] -= 1
                print(f"maq: Pode retirar o produto dispensado {p['nome']}")
                print(f"maq: Saldo = {formatar_saldo(saldo)}")
                return saldo
            else:
                print("maq: Saldo insuficiente para satisfazer o seu pedido")
                print(f"maq: Saldo = {formatar_saldo(saldo)}; Pedido = {p['nome']}")
                return saldo
    print("maq: Produto não encontrado.")
    return saldo

def calcular_troco(saldo):
    troco = []
    for nome, valor in moedas.items():
        while saldo >= valor:
            troco.append(nome)
            saldo = round(saldo - valor, 2)
    return troco

def processar_comando(comando, saldo, stock):
    lexer.input(comando)
    tokens = [tok for tok in lexer]
    if not tokens:
        print("maq: Comando inválido.")
        return saldo

    primeiro_token = tokens[0].type

    if primeiro_token == "LISTAR":
        listar_produtos(stock)
    elif primeiro_token == "MOEDA":
        saldo = inserir_moedas(saldo, tokens[1].value)
        print(f"maq: Saldo = {formatar_saldo(saldo)}")
    elif primeiro_token == "SELECIONAR":
        saldo = selecionar_produto(tokens[1].value, saldo, stock)
    elif primeiro_token == "SAIR":
        troco = calcular_troco(saldo)
        if troco:
            troco_str = ", ".join([f"{troco.count(m)}x {m}" for m in sorted(set(troco), key=lambda x: moedas[x], reverse=True)])
            print(f"maq: Pode retirar o troco: {troco_str}.")
        print("maq: Até à próxima.")
        exit()
    else:
        print("maq: Comando inválido.")
        
    return saldo

def carregar_stock():
    try:
        with open("stock.json", "r", encoding='utf-8') as f:
            return json.load(f)
    except FileNotFoundError:
        print("Erro: arquivo de estoque não encontrado.")
        return {"stock": []}

def update_stock(stock):
    with open("stock.json", "w", encoding='utf-8') as f:
        return json.dump(stock, f, indent=4)

def main():
    global saldo, stock
    stock = carregar_stock()
    saldo = 0.0

    data = str(datetime.date.today())
    print(f"maq: {data}, Stock carregado, Estado atualizado.")
    print("maq: Bom dia. Estou disponível para atender o seu pedido.")

    while True:
        comando = input(">> ")
        saldo = processar_comando(comando, saldo, stock)

if __name__ == "__main__":
    main()