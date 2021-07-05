#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from dataclasses import dataclass
from typing import Any

class SinglyLinkedList():
    @dataclass
    class _Head:
        next: '_Node' = None
 
    @dataclass
    class _Node:
        value: Any
        next: '_Node' = None

    __slots__ = ['_head']
 
    def __init__(self, iterable=None):
        self._head = SinglyLinkedList._Head(None)
        if iterable is not None:
            prev = self._head
            for value in iterable:
                node = SinglyLinkedList._Node(value, None)
                prev.next = node
                prev = node
