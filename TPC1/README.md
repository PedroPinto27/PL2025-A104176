# TPC1 - Somador ON/OFF/=

**Data:** 2024-02-12

**Autor:** Pedro Filipe Maneta Pinto

**Número Mecanográfico** A104176

## Sobre o TPC

Este projeto implementa um somador que funciona seguindo os comandos "on" e "off" dentro de uma sequência de números e operadores. 
O objetivo é processar uma mensagem de entrada contendo instruções e calcular a soma acumulada conforme os estados ativados ou desativados. 

**"*ON*": Ativa a soma.**

**"*OFF*": Desativa a soma.**

**"=": Imprime a soma atual.**

## Exemplo

Uma mensagem por exemplo: **"10a-5b=on3c4d=off6e-2f=on8g-10h=on5i="**

Devolve o seguinte *Output*:
- 5
- 12
- 12
- 10
- 15


