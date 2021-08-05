#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class Node:
    def __init__(self, data):
        self.left = None # hijo izquierdo
        self.right = None # hijo derecho
        self.data = data

    def insert(self, data):
        # Compara el nuevo valor con el nodo padre
        if self.data:
            if data < self.data:
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.insert(data)
            elif data > self.data:
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.insert(data)
        else:
            self.data = data

    def PrintTree(self):
        if self.left:
            self.left.PrintTree()
        print(self.data)
        if self.right:
            self.right.PrintTree()

#    def PrintTree(self):
#        print(self.data)

print("Agrego '15' a mi Árbol Binario")
root = Node(15)
root.PrintTree()
print("Agrego 85, 4, 65, 42, 2, 10, 75" )
root.insert(85)
root.insert(4)
root.insert(65)
root.insert(42)
root.insert(2)
root.insert(10)
root.insert(75)

print("Finalmente el orden de mi Árbol Binario queda de la siguiente forma")
root.PrintTree()

