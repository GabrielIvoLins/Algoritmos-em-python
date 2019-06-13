#!/usr/bin/python3
# -*- coding: utf-8 -*-
__author__ = 'Gabriel Ivo Lins'

from random import randint
from random import choice

personagem = ['mago','arqueiro','barbaro','guerreiro','bardo']
escolha_heroi = choice(personagem)
print(escolha_heroi)

#dado = randint(1,20)
#print(dado)

dado = lambda x,y: randint(x,y)
print(dado(1,20))


def dado_f(x,y):
    return randint(x,y)

print(dado_f(1,12))