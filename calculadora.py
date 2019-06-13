#!/usr/bin/python3
# -*- coding: utf-8 -*-
__author__ = 'Gabriel Ivo Lins'

print('Digite dois números:')# Imprime uma mensagem
# n1 e n2 recebem números digitados pelo usuário
# sinal recebe um sinal matemático digitado pelo usuário
n1 = float(input('--> '))
n2 = float(input('--> '))
operador = input('Digite um operador matemático: ')

'''Abaixo cada estrutura condicional ira verificar se na variavel |operador|
tem os seguintes sinais: *, /, -, +,**,% e realizar a operação matemática de
accordo com o sinal inserido pelo usuário.
'''

if operador == '*':
    mult = n1 * n2
    print('O resultado da multiplicação é: %.2f' % mult)

elif operador == '/':
    div = n1 / n2
    print('O resultado da divisão é: %.2f' % div)

elif operador == '%':
    # o modulo % exibi o resto de uma divisão
    modulo  = n1 % n2
    print('O resultado do resto é: %.2f' % modulo)

elif operador == '-':
    sub = n1 - n2
    print('O resultado da subtrasão é: %.2f' % sub)

elif operador == '+':
    adicao = n1 + n2
    print('O resultado da adição é: %.2f' % adicao)

elif operador == '**':
    potenciacao = n1**n2
    print('O resultado da potenciação é %.2f'% potenciacao)

else:
    print('Sinal invalido!')
