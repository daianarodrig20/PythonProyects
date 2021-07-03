#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from dataclasses import dataclass
from typing import Any

class Pila():
    @dataclass
    class _Node:
        value = Any
        siguiente = _Node

    __slots__=[_inicio]

    def __init__(self, iterable = None):
        self._inicio = None
        if iterable is not None:
            for value in iterable:
                self.apilar(value)

    def vacia(self):
        return self._inicio is None

    @property
    def tope(self):
        assert not self.vacia(), 'Pila vacia'
        return self._inicio

    def apilar(self, value):
        self._inicio=Pila._Node(value, self._inicio)

    def desapilar(self):
        assert not self.vacia(), 'Pila vacia'
        value = self._inicio.value
        self._inicio = self._inicio.siguiente
        return value

    def borrar(self):
        self._inicio = None

    def copiar(self):
        new_Pila = Pila()
        new_Pila._inicio = self._inicio
        return new_Pila

    def __len__(self):
        n = 0
        node = self._inicio
        while node is not None:
            node = node.siguiente
            n += 1
        return n

    def __eq__(self, other):
        x = self._inicio
        y = other._inicio
        while x is not None and y is not None:
            if x.value != y.value:
                return False
            x = x.siguiente
            y = y.siguiente
        return x is None and y is None

