#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def factorial_iterativo(n):
    resultado = 1
    for i in range(n):
        resultado *=  (i+1)
    return resultado

print(factorial_iterativo(5))

"""
ITERACION: Permite repetir una sentencia o conjunto de ellas

VENTAJA: Es más eficiente en cuanto a memoria

DESVENTAJA: Suelen tener bucles que son complejos de leer y entender
"""
