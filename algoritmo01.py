#!/usr/bin/python3
# -*- coding: utf-8 -*-
__author__ = "Gabriel Ivo Lins"

nome = input("Digite seu nome: ")
print(f'seja bem vindo {nome}')

print('Digite dois números:')

n1 = float(input('--> '))
n2 = float(input('--> '))

soma = n1 + n2
sub = n1 - n2
mult = n1 * n2
div = n1 / n2

print("""O resultado da soma: %.2f 
O resultado da subtração: %.2f
O resultado da multiplicação: %.2f
O resultado da divisão: %.2f
""" % (soma,sub,mult,div))