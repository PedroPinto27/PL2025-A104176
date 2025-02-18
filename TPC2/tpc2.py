def parse_csv(file):
    data = []
    with open(file, 'r', encoding='utf-8') as f:
        linhas = f.readlines()

    cabecalho = linhas[0].strip().split(';')
    data.append(cabecalho)

    current_line = []
    in_quotes = False
    current_field = ''

    for linha in linhas[1:]:
        linha = linha.strip()

        for char in linha:
            if char == '"':
                in_quotes = not in_quotes
            elif char == ';' and not in_quotes:
                current_line.append(current_field)
                current_field = ''
            else:
                current_field += char

        if not in_quotes:
            current_line.append(current_field)
            data.append(current_line)
            current_line = []
            current_field = ''
        else:
            current_field += '\n'

    return data

def musicos_ordenados(dados):
    
    lista = set()
    posicao = dados[0].index("compositor")
    for linha in dados[1:]:
        lista.add(linha[posicao])
    
    return sorted(lista)
        
        
def musicasPorPeriodo(dados):
    dict={}
    posicao = dados[0].index("periodo")
    for linha in dados[1:]:
        key = linha[posicao]
        if key in dict:
            dict[key] += 1
        else:
            dict[key] = 1
    
    return dict

def listaPorPeriodo(dados):
    
    dict={}
    
    periodo = dados[0].index("periodo")
    nome = dados[0].index("nome")
    
    for linha in dados[1:]:
        key = linha[periodo]
        if key in dict:
            dict[key].append(linha[nome])
        else:
            dict[key] = [linha[nome]]
    
    for key in dict:
        dict[key] = sorted(dict[key])
    
    return dict

    
def main():
    file = 'obras.csv'
    dados = parse_csv(file)
    print("1 - Lista ordenada alfabeticamente dos compositores musicais;")
    print("2 - Distribuição das obras por período: quantas obras catalogadas em cada período;")
    print("3 - Dicionário em que a cada período está a associada uma lista alfabética dos títulos das obras desse período.")
    
    opcao = input()
    
    if int(opcao) == 1:
        lista = musicos_ordenados(dados)
        for elemento in lista:
            print(elemento)
            
    elif int(opcao) == 2:
        dict = musicasPorPeriodo(dados)
        for d in dict:
            print(d + "-" + str(dict[d]))
            
    elif int(opcao) == 3:
        dict = listaPorPeriodo(dados)

        for periodo in dict.keys():
            obras = ", ".join(dict[periodo])

            print(f"{periodo}: {obras}\n")

if __name__ == "__main__":
    main()