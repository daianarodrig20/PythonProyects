#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from dataclasses import dataclass

class Queue():
    # Puntero a los valores de la cola
    # Puntero a el 'frente' de la cola
    # Puntero al tamaño de la cola
    __slots__ = ['_values', '_front', '_lenght']

    def __init__(self, iterable = None):
        self._front = 0
        if iterable is not None:
            self._values = list(iterable)
        else:
            self._values = []
        self._lenght = len(self._values)

