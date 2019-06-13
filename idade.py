#!/usr/bin/python3
# -*- coding: utf-8 -*-
__author__ = 'Gabriel Ivo Lins'

idade = int(input('Digite a sua idade: '))# Recebe um número digitado pelo usuário

if idade >= 18:# verifica se o valor é iqual ou maior que 18
    # Se o valor for maior ou iqual a 18 então esse bloco será executado
    print('Você é maior de idade!')

elif idade < 18 and idade > 0:
    # Se o valor for menor que 18 e maior que 0 então esse bloco será executado
    print('Você é menor de idade!')

else:
    # Se nenhuma condição anterior for satisfeita então o bloco abaixo será executado
    print('Idade inválida')