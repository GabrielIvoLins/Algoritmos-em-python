#!/usr/bin/python3
# -*- coding: utf-8 -*-
__author__ = 'Gabriel Ivo Lins'

from math import sqrt

print("Informe os coeficientes da equação de 2º grau:")
# As variáveis a,b,c recebem um valor digitado pelo usuário
a = float(input('a= '))
b = float(input('b= '))
c = float(input('c= '))

delta = (b**2) - (4 * a * c)# Fórmula de delta b² - 4 * a * c

if delta > 0:# Verifica se delta é maior que 0
    # Se delta maior que 0 então o bloco a baixo será executado
    x1 = (- b + sqrt(delta))/(2 * a)
    x2 = (- b - sqrt(delta))/(2 * a)

    print("A solução é: %.2f e %.2f" % (x2,x1))
else:
    # Se o delta for negativo o bloco abaixo será executado
    print("Como o delta é menor que 0, equação não possui raiz.")