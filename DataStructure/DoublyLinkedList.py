#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from dataclasses import dataclass
from typing import Any

class DoublyLinkedList():
    @dataclass
    class _Node:
        value: Any
        anterior: '_Node' = None # prev: '_None' = None
        siguiente: '_Node' = None # next: '_None' = None

    @dataclass
    class _Head:
        anterior: '_Node' = None # prev: '_None' = None
        siguiente: '_Node' = None # next: '_None' = None

    __slots__ = ['_head']

    def __init__(self, iterable = None):
        self._head = ListaDoblementeEnlazada._Head()
        self._head.anterior = self._head.siguiente = self._head
        #self._head.prev = self._head.next = self._head
        if iterable is not None:
            for value in iterable:
                self.append_back(value)

    def __len__(self):
        n = 0
        nodo = self._head.siguiente
        # nodo = self._head.next
        while nodo is not self._head:
            n += 1
            nodo = nodo.siguiente
            # nodo = nodo.next
        return n
    def is_empty(self):
        return self._head.siguiente is self._head
        #return self._head.next is self._head

    @property
        def front(self):
            assert not self.is_empty(), 'La lista esta vacia'
            return self._head.siguiente.value
            #return self._head.next.value
    @property
        def back(self):
            assert not self.is_empty(), 'La lista esta vacia'
            return self._head.anterior.value
            #return self._head.prev.value
        def append_front(self, value):
            self.insert(self.begin(), value)
        def append_back(self, value):
            self.insert(self.end(), value)
        def copy(self):
            new_lista = ListaDoblementeEnlazada()
            # new_list = DoublyLinkedList()
            act = new_lista._head
            for value in self:
                node = ListaDoblementeEnlazada._Node(value)
                # node = DoblyLinkedList._Node(value)
                node.anterior = act
                # node.prev = act
                act.siguiente = node
                # act.next = node
                act = node
            new_lista._head.siguiente = act
            act.next = new_list._head
            return new_list

        def clear(self):
            self._head.prev = self._head.next = self._head
        def begin(self):
            return DoublyLinkedList._Coordinate(self._head.next)
        def end(self):
            return DoublyLinkedList._Coordinate(self._head)
        def __eq__(self, other):
            p = self.begin()
            q = self.begin()
            while p != self.end() and q != other.end():
                if p.value != q.value:
                    return False
                p.advance()
                q.advance()
            return p == self.end() and q == other.end()
        def __repr__(self):
            return 'DoublyLinkedList([' + ','.join(repr(x) for v in self) + '])'

        class _Coordinate():
            __slots__ = ['_node']
            def __init__(self, coordinate_or_node):
                if isinstance(coordinate_or_node, DoubkyLinkedList._Coordinate):
                    self._node = coordinate_or_node._node
                else:
                    self._node = coordinate_or_node

        @property
        def value(self):
            return self._node.value
        @value.setter
        def value(self, value):
            self._node.value = value

        def advance(self):
            self._node = self._node.next
            return self
        def next(self):
            return DoublyLinkedList._Coordinate(self._node).advance()
        def retreat(self):
            self._node = self._node.prev
            return self
        def prev(self):
            return DoublyLinkedList._Coordinate(self._node).retreat()
        def __eq__(self, other):
            return self._node is other._node
        def find(first, las, value):
            while first != last:
                if first.value == value:
                    return first
                first = first.next()
            return last
        def insert(self, coord, value):
            current = coord._node
            new_node = DoublyLinkedList._Node(value)
            new_node.prev = current.prev
            new_node.next = current
            new_node.prev.next = new_node
            new_node.next.prev = new_node
            #return DoublyLinkedList._Coordinate(current)
        def erase(self, coord):
            current = coord._node
            current.prev.next = current.next
            current.next.prev = current.prev
            return coor.next()

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

