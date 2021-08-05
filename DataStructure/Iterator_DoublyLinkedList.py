#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
- Los iteradores fueron inspirados en los punteros,
  imitando su sintaxis y uso

- El tipo de iterador depende de la estructura de datos sobre la que itera y,
  a su vez, está limita las capacidades del iterador(por ejemplo, no es buena idea
  un iterador de acceso aleatorio para una lista enlazada simple

- Los iteradores permiten independizar a un algoritmo de la estructura de datos sobre
  la cuál opera (por ejemplo, es el mismo algoritmo el usado para buscar un valor en un arreglo
  desordenado o en una lista enlazada simple).

- Un iterador es un objeto que hace referencia a elementos de una secuencia. Esos elementos pueden
  ser calculados (como en el caso de range()) o tomados de un contenedor(como en el caso de las
  cadenas de caracteres o las tuplas)
  Es posible obtener un iterador sobre un objeto usando iter()

- Es posible obtener uno a uno los elementos del objeto sobre el que se esta iterando usando next()
  hasta que indique el fin de la iteracion con un error de tipo StopIteration

- Se podrá iterar con for/in a cualquier objeto que iter() pueda obtener un iterador. A dicho
  objeto se lo denominara iterable
  No todo objeto es iterable(por ejemplo: int, float, etc)
  En python existen muchos objetos iterables. Todos se comportan de la misma manera

- Para poder iterar sobre nuetra lista doble vamos a implementar entonces
  la clase _Iterator con los métodos iter() y next
  y el método iter() en la lista doble

"""
class _Iterator():
    __slots__ = ['_node', '_end']


def __init__(self, head, end):
    self._node = head
    self._end = end


def __iter__(self):
    return self


def __next__(self):
    if self._node is self._end:
        raise StopIteration
    value = self._node.value
    self._node = self._node.next
    return value


def __iter__(self):
    return DoublyLinkedList._Iterator(self._head.next, self._head)
