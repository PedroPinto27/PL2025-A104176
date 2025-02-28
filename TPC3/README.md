# TPC2 - Análise de um dataset de obras musicais

**Data:** 2025-02-28

**Autor:** Pedro Filipe Maneta Pinto

**Número Mecanográfico:** A104176

**Foto:**

![Foto](../img/image.jpg)  

## Sobre o TPC

Este projeto converte ficheiros Markdown em HTML, transformando títulos, negrito, itálico, listas, imagens e links no formato adequado. O programa lê um ficheiro Markdown, processa o conteúdo com expressões regulares e gera um ficheiro HTML formatado corretamente.

## Funcionalidades

**Converter Markdown para HTML:**

-Lê um ficheiro Markdown e processa o seu conteúdo para HTML.

**1 - Conversão de Headers:**

-Transforma títulos Markdown em tags HTML.

**2 - Formatação de Texto:**

-Converte negrito e itálico.

**3 - Listas Ordenadas:**

-Identifica listas numeradas.

**4 - Conversão de Links e Imagens:**

-Identifica links e imagens.

**5 - Geração de Ficheiro HTML:**

-Cria um ficheiro HTML formatado e indentado com o conteúdo convertido.

Input: 

```
# Conversor de MarkDown para HTML

## Exemplos de Formatação
Este é um texto com **negrito** e *itálico*.

### Itens da Lista
1. Primeiro item
2. Segundo item
3. Terceiro item

Como pode ser consultado em [página da UC](http://www.uc.pt).

Como se vê na imagem seguinte: ![imagem dum coelho](http://www.coelho.com)...
```

Devolve o seguinte *Output*:
```
<h1>Conversor de MarkDown para HTML</h1>


<h2>Exemplos de Formatação</h2>

Este é um texto com <b>negrito</b> e <i>itálico</i>.

<h3>Itens da Lista</h3>

<ol>
	<li>Primeiro item</li>
	<li>Segundo item</li>
	<li>Terceiro item</li>
</ol>

Como pode ser consultado em <a href="http://www.uc.pt">página da UC</a>.

Como se vê na imagem seguinte: <img src="http://www.coelho.com" alt="imagem dum coelho"/>...
```