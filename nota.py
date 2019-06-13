#!/usr/bin/python3
# -*- coding: utf-8 -*-
__author__ = 'Gabriel Ivo Lins'

print('Digite duas notas: ')
n1 = float(input('--> '))# recebe a 1º nota
n2 = float(input('--> '))# recebe a 2º nota 

media = (n1 + n2) / 2 # cálcula a média

print('Sua media é: %.2f' % media)

if media >= 6:
    # se a media for iqual ou maior que 6 então será executado o bloco a baixo
    print("Você foi aprovado!")

else:
    # se a condição a cima não for satisfeita então será executado o bloco abaixo
    print("Você foi reprovado!")