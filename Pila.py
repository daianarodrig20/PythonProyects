#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from dataclasses import dataclass
from typing import Any

class Pila:
    @dataclass
    class _Nodo:
        dato: Any
        sig: '_Nodo'

    __slots__ = ['_tope', 'tamanio'] # Puntero al tope

    # Inicializo mi pila vacia o con una iterable, osea, le puedo pasar una secuencia de elementos
    # Tambien la inicializo en 0
    def __init__(self, iterable = None):
        self._tope = None # El tope va a estar vacio
        tamanio = 0
        if iterable is not None:
            for dato in iterable:
                self.apilar(dato)

    # Booleano: Retorna true si mi pila esta vacia en caso contrario False
    def es_vacia(self):
        return self.tamanio == 0
        ## Tambien podria ser:
        # return self._tope is None

    # Vacio mi pila
    def vaciar(self):
        self._tope = None
        self.tamanio = 0

    @property
    def tope(self):
        assert not self.es_vacia(), 'No se puede operar en una pila vacia'
        return self._tope.dato

    def apilar(self, dato):
        self._tope = Pila._Nodo(dato, self._tope)

    def desapilar(self):
        assert not self.es_vacia(), 'La pila se encuentra vacia'
        dato = self._tope.dato
        self._tope = self._tope.sig
        return dato

    def copiar(self):
        nueva_pila = Pila()
        if not self.es_vacia():
            nodo = self._tope
            nuevo_nodo = Pila._Nodo(nodo.dato, None)
            nueva_pila._tope = nuevo_nodo
            while nodo.sig is not None:
                nodo = nodo.sig
                nuevo_nodo.sig = Pila._Nodo(nodo.dato, None)
                nuevo_nodo = nuevo_nodo.sig
        return nuevo_nodo

    # comparo dos pilas
    def __iguales__(self, otra):
        a = self._tope
        b = otra._tope

        while a is not None and b is not None:
            if a.dato != b.dato:
                return False
            a = a.sig
            b = b.sig
        return a is None and b is None

    def __repr__(self):
        datos = []
        nodo = self._tope
        while nodo is not None:
            datos.insert(0, nodo.dato)
            nodo = nodo.sig
        return ' Pila([' + ', '.join(repr(x) for x in datos) + '])'
