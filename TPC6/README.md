# TPC6 - Recursivo Descendente para expressões aritméticas
**Data:** 2025-03-23

**Autor:** Pedro Filipe Maneta Pinto

**Número Mecanográfico:** A104176

**Foto:**

![Foto](../img/image.jpg)  

## Sobre o TPC

O código implementa um parser LL(1) recursivo descendente em Python para reconhecer e calcular o valor de expressões aritméticas. Ele processa expressões que envolvem adição, subtração, multiplicação, divisão e parênteses, respeitando a precedência dos operadores.

## Funcionalidades

**Parser LL(1) Recursivo Descendente:**

- Implementa um analisador sintático recursivo descendente com lookahead de um token.

**Reconhecimento de Tokens:**

- Utiliza o módulo `ply.lex` para análise léxica, reconhecendo:
  - `NUMBER`: Números inteiros.
  - `PLUS`, `MINUS`, `TIMES`, `DIVIDE`: Operadores aritméticos.
  - `LPAREN`, `RPAREN`: Parênteses.

**Funcionalidades:**

- **Parsing e Cálculo:**
  - Processa expressões aritméticas seguindo a gramática:
    - operacao → calc { + calc | - calc }
    - calc → factor { * factor | / factor }
    - factor → NUMBER | ( operacao )
  - Respeita a prioridade da multiplicação e divisão antes de adição e subtração.
  - Calcula o resultado final da expressão.

Input: 

```
2+3
67-(2+3*4)
(9-2)*(13-4)
```

Devolve o seguinte *Output*:
```
Exemplo: 2+3 = 5
Exemplo: 67-(2+3*4) = 53
Exemplo: (9-2)*(13-4) = 63
```