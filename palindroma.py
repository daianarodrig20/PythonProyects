#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Escriba un programa que lea una secuencia de caracteres e informe si la
misma es palíndromo.
"""

def palindroma(palabra):
    inversa = ''.join(reversed(palabra))
    if str(palabra) == inversa:
        print(palabra + ": esta palabra es palindroma!! ")
    else:
        print(palabra + ": esta palabra no es palindroma")

# Tambien lo podria hacer pidiendole una palabra al usuario
#p = input("Ingrese una palabra para evaluar: ")
#palindroma(p)

## PRUEBA
palabra1 = 'perrito'
palabra2 = 'otto'

palindroma(palabra1)
palindroma(palabra2)
