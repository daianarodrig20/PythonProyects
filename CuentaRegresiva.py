#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Cuenta regresiva que se comporta como "Range" pero contando al revés
"""

def cuenta_regresiva(iterable):
    contador = len(iterable)
    regresiva = reversed(iterable)
    while contador <= 0:

        
