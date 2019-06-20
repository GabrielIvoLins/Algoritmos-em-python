#!/usr/bin/python3
# -*- coding: utf-8 -*-
__author__ = 'Gabriel Ivo Lins'

while True:
    escolha = int(input('''1.fahrenhit para celsius
2.celsius para fahrenhit
3.encerrar programa\n--> '''))

    if escolha == 1:
        t = float(input('Digite uma temperatura a ser convertida:\n--> '))
        c = ( 5 * (t - 32) / 9)
        print('Em celsius: %.4f' % c)
    
    elif escolha == 2:
        t = float(input('Digite uma temperatura a ser convertida:\n--> '))
        f = ((t / 5) * 9) + 32
        print('Em fahrenhit: %.4f' % f)
    
    elif escolha == 3:break
    
    else:
        print('Opção inválida!')