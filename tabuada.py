#!/usr/bin/python3
# -*- coding: utf-8 -*-
__author__ = 'Gabriel Ivo Lins'

x = int(input('Informe um número da tabuada que deseja:\n--> '))
cont = 1

for i in range(1,11):
    print('{} X {} = {}'.format(x,cont,cont * x))
    cont += 1