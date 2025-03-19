# TPC5 - Vending Machine
**Data:** 2025-03-19

**Autor:** Pedro Filipe Maneta Pinto

**Número Mecanográfico:** A104176

**Foto:**

![Foto](../img/image.jpg)  

## Sobre o TPC

O código implementa uma simulação de uma máquina de venda automática em Python, utilizando o módulo PLY para análise léxica de comandos. A máquina permite listar produtos em Stock, inserir moedas, selecionar produtos pelo código e devolver troco ao sair. O Stock é carregado a partir de um ficheiro JSON (stock.json), e o programa processa comandos interativamente, atualizando o saldo e o Stock conforme as ações do utilizador.

## Funcionalidades

**Analisador Léxico:**

- Utiliza o PLY (Python Lex-Yacc) para criar um analisador léxico que identifica e classifica tokens nos comandos inseridos.

**Reconhecimento de Tokens:**

Identifica diversos tokens, como:
- Comandos: LISTAR, MOEDA, SELECIONAR, SAIR.
- Códigos de produtos: No formato [A-Z][0-9]{2} (ex.: A23).
- Valores de moedas: Combinações de 2e, 1e, 50c, 20c, 10c, 5c, 2c, 1c, separadas por vírgulas (ex.: 2e, 50c).
- Pontuação: . para finalizar comandos.

**Funcionalidades:**
- LISTAR: Exibe uma tabela com código, nome, quantidade e preço dos produtos em Stock.
- MOEDA: Permite inserir moedas e atualiza o saldo do utilizador.
- SELECIONAR: Permite escolher um produto pelo código, deduzindo o preço do saldo se houver quantidade disponível e saldo suficiente.
- SAIR: Calcula e devolve o troco em moedas, encerrando o programa.
- Gestão de Stock: Carrega o Stock de um ficheiro JSON e atualiza a quantidade de produtos conforme as compras.

Input: 

```
>> LISTAR
>> MOEDA 2e, 50c
>> SELECIONAR A23
>> SAIR
```

Devolve o seguinte *Output*:
```
maq: cod   | nome       | quantidade | preço
maq: ---------------------------------------
maq: A23   | Agua 0.5L  |     8      | 0.7
maq: D67   | Bolacha Maria |  18      | 1.0
maq: P67   | RedBull    |     2      | 1.3

maq: Saldo = 2e50c

maq: Pode retirar o produto dispensado Agua 0.5L
maq: Saldo = 1e80c

maq: Pode retirar o troco: 1x 1e, 1x 50c, 1x 20c, 1x 10c.
maq: Até à próxima.
```