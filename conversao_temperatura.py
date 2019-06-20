#!/usr/bin/python3
# -*- coding: utf-8 -*-
__author__ = 'Gabriel Ivo Lins'

f = float(input('Digite uma temperatura em farenheit: '))

c = ( 5 * (f - 32) / 9)

print('Em celsius: %.4f' % c)