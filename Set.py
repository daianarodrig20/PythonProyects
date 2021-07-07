#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from dataclasses import dataclass
from typing import Any

"""
Funciones de un Conjunto:
- El conjunto se crea con una serie de elementos entre llaves
- Lo elementos repetidos se eliminan
- Para agregar un elemento en conjunto se utiliza 'add'
- Para eliminar un elemento en un conjunto se utiliza 'discard'
- Para dejar el conjunto vacio se utiliza 'clear'
"""

class Set():
    @dataclass
    class _Node:
        value: Any
        next: '_Node'

    __slots__ = ['_first'] # Creo un puntero al primer elemento del conjunto

    def __init__(self, iterable = None): 
        self._first = None # Creo un conjunto vacio
        if iterable is not None: # o a partir de una secuencia de elementos
            for value in iterable:
                self.add(value)

    def is_empty(): # Creo una funcion que retorna True o False si el conjunto esta vacio
        return self._first == None # Si el primer elemento es None retorna True

    def belongs(self, value): # Evalue si un elemento pertenece al conjunto
        assert not self.is_empty(), 'El conjunto esta vacio' # Si el conjunto esta vacio no realiza la evaluación
        aux = self._first # Creo un auxiliar con el primer elemento
        while aux.next != None and aux.next != aux.value: # Recorro el conjunto hasta que el siguiente no sea None y el siguiente no sea el elemento que buscaba
            aux = aux.next
        if aux.next == aux.value: # Si el siguiente al auxiliar es el elemento que buscaba entonces retorno True
            return True
        else:
            return False

    def add(self, value):
        new_node = Conjunto._Node(value, None) # Creo un nuevo nodo con el valor que se paso por parametro
        if self.is_empty() or new_node.value < self._first.dato: # Si el conjunto esta vacio o el nuevo nodo es menor al dato a ingresar
            aux = self._first # Creo un auxiliar para no perder el valor de mi nodo principal
            new_node.next = aux  # El siguiente del nuevo nodo pasa a ser quien era el primero
            self._first = new_node # El puntero al principio pasa al nuevo nodo
        else:
            aux2 = self._first # Sino creo un auxiliar donde voy a guardar el valor del primer elemento para no perderlo
            while aux2.next != None and aux2.next <= new_node.value: # Mientras que el siguiente del auxiliar no sea None y sea menor o igual al valor que quiero agregar
                if aux2.value == value:
                    print('Este elemento ya pertenece en el conjunto')
                    break
                aux2 = aux2.next
            if aux.value is not value:
                new_node.next = aux2.next
                aux2.next = new_node

    def discard(self, value): # Elimino un nodo especificado por parametro
        assert not self.is_empty(), ' No se puede operar en un conjunto vacio' 
        if self.belongs()

    def __repr__():
        conjunto = [] # Creo una lista llamada conjunto para mostrar mi conjunto por pantalla
        aux = self._first # Creo un auxiliar para recorrer mi conjunto
        while aux is not None:
            conjunto.append(aux.value) # Mientras que el auxiliar no sea None va a agregando su valor actual a la lista 'Conjunto' y pasando al siguiente
            aux = aux.next
        return 'Conjunto {' + ', '.join(repr(x) for x in Conjunto) + '}'
