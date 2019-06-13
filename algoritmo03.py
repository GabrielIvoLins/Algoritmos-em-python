#!/usr/bin/python3
# -*- coding: utf-8 -*-
__author__ = 'Gabriel Ivo Lins'

l = 'Olá mundo'
print(l.upper())# upper() deixa a string maiuscula 

x = 'OLÁ MUNDO'
print(x.lower())# lower() deixa a string minuscula

var = 'O rato roeu a roupa do rei de Roma'
print(var.split())# split() trasforma uma string em uma lista

print(var.split('r'))

busca = var.find('rei')# find() retorna o índice da busca
print(busca)
print(var[busca:])