# TPC4 - Analisador Léxico
**Data:** 2025-03-07

**Autor:** Pedro Filipe Maneta Pinto

**Número Mecanográfico:** A104176

**Foto:**

![Foto](../img/image.jpg)  

## Sobre o TPC

O código implementa um analisador léxico usando PLY para processar consultas em um formato semelhante ao SPARQL. Identifica-se diferentes tokens, como palavras-chave (SELECT, WHERE, LIMIT), variáveis (?var), identificadores (id:id), strings ("Texto"@en), números e comentários (# comentário). O programa lê um ficheiro de entrada, analisa o conteúdo e gera um ficheiro de saída com os tokens identificados. 

## Funcionalidades

**Analisador Léxico:**

- Utiliza o PLY (Python Lex-Yacc) para criar um analisador léxico que identifica e classifica tokens.

**Reconhecimento de Tokens:**

Identifica diversos tokens, como:
- Palavras-chave: SELECT, WHERE, LIMIT.
- Variáveis: Iniciadas com ?.
- Identificadores: No formato id:id.
- Strings: Com marcação de idioma (ex.: "Texto"@en).
- Comentários: Iniciados por #.
- Operadores de agrupamento: {, }.
- Números inteiros.
- Pontuação: Como .

**Tratamento de Erros:**

- Exibe mensagens de erro caso o ficheiro de entrada não seja encontrado ou ocorra qualquer outro erro inesperado.

Input: 

```
# DBPedia: obras de Chuck Berry
select ?nome ?desc where {
 ?s a dbo:MusicalArtist.
 ?s foaf:name "Chuck Berry"@en .
 ?w dbo:artist ?s.
 ?w foaf:name ?nome.
 ?w x:abstract ?desc
} LIMIT 1000
```

Devolve o seguinte *Output*:
```
Token: COMMENT, Valor: # DBPedia: obras de Chuck Berry
Token: SELECT, Valor: select
Token: VARIABLE, Valor: ?nome
Token: VARIABLE, Valor: ?desc
Token: WHERE, Valor: where
Token: LC, Valor: {
Token: VARIABLE, Valor: ?s
Token: ATTRIBUTE, Valor: a
Token: ID, Valor: dbo:MusicalArtist
Token: DOT, Valor: .
Token: VARIABLE, Valor: ?s
Token: ID, Valor: foaf:name
Token: STRING, Valor: "Chuck Berry"@en
Token: DOT, Valor: .
Token: VARIABLE, Valor: ?w
Token: ID, Valor: dbo:artist
Token: VARIABLE, Valor: ?s
Token: DOT, Valor: .
Token: VARIABLE, Valor: ?w
Token: ID, Valor: foaf:name
Token: VARIABLE, Valor: ?nome
Token: DOT, Valor: .
Token: VARIABLE, Valor: ?w
Token: ID, Valor: x:abstract
Token: VARIABLE, Valor: ?desc
Token: RC, Valor: }
Token: LIMIT, Valor: LIMIT
Token: INTEGER, Valor: 1000
```