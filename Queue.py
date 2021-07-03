#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from dataclasses import dataclass
from typing import Any

class Queue:
    @dataclass
    class _Node:
        value: Any
        next: '_Node'

    __slot__ ['begin','end']

    def __init__(self, iterable = None):
        self.begin = None
        self.end = None
        if iterable is not None:
            for value in iterable:
                self.enqueue(value)

    def enqueue(self, value):

    def dequeur(self):

    def begin(self):
        if self.next is not None:
            return self.dato
        else:
            print('La cola esta vacia')

    def end(self):
