#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from dataclasses import dataclass
from typing import Any

class Queue:
    @dataclass
    class _Node:
        date: Any
        next: '_Node'

    __slot__ ['_head','_tail']

    def __init__(self, iterable = None):
        self.head = None
        self.tail = None
        if iterable is not None:
            for date in iterable:
                self.enqueue(date)

    def is_empty(self):
        return self.head == None
    
    def _head(self):
        assert not self.is_empty(), 'La cola se encuentra vacia'
        return self.head.date

    def _tail(self):
        assert not self.is_empty(), ' La cola se encuentra vacia'
        return self.tail.date

    def enqueue(self, value):
        new_nodo = _Node(value)
        if self.head == None:
            self.head = new_nodo
            self.head = new_nodo
        else:
            self.tail.next = new_nodo
            self.tail = new_nodo

    def dequeue(self):
        assert not self.is_empty(), 'La cola se encuentra vacia'
        aux = self.head.date
        self.head = self.head.next
        if self.head is None:
            self.tail is None
        return aux

