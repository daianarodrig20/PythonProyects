#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class Node:
    def __init__(self, data):
        self.left = None # hijo izquierdo
        self.right = None # hijo derecho
        self.data = data

    def PrintTree(self):
        print(self.data)

root = Node(22)
root.PrintTree()
