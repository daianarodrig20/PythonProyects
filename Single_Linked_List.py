#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Lista enlazada simple

# Creo la clase Single linked list
class Single_Linked_List:
    class _Nodo: # Creo una clase interna llamada Nodo. Tiene '_' porque es una clase privada osea no debe poder accederse de afuera
        def __init__(self, valor): # Creo el contructor de la clase nodo
            self.valor = valor
            self.nodo_siguiente = None
    def __init__(self):
        self.cabeza = None
        self.cola = None
        self.tamanio = 0

    # Método para imprimir la lista simple
    def __str__(self): # Este metodo va a funcionar como automatico para cuando queramos imprimir
        # Muestra los elementos de la lista simple
        array = []
        nodo_actual = self.cabeza
        # Vamos a tener que iterar, avanzar en la lista simple por eso comienzo por la cabeza
        while nodo_actual != None: # Mientras que el nodo actual no sea None recorre la lista
            array.append(nodo_actual.valor) # Agrega al array el valor del nodo actual
            nodo_actual = nodo_actual.nodo_siguiente
        return str(array) + " Tamaño: " + str(self.tamanio) # Imprimo el array y el tamaño

    # Empiezo a crear los metodos
    def append(self, valor):
        # El agregar agregar un elemento al final de la lista simple
        nuevo_nodo = self._Nodo(valor)
        if self.cabeza == None and self.cola == None: # Comprueba si la lista esta vacia
        # En el caso que la lista se encontrara vacia:
            self.cabeza = nuevo_nodo # cabeza va a apuntar al nuevo nodo
            self.cola = nuevo_nodo # cola va a apuntar al nuevo nodo
        else:
            # En caso contrario, si existe uno o varios elementos quiero que el nuevo nodo se agregue siguiente a ese unico nodo o a esa secuencia de elementos
            self.cola.nodo_siguiente = nuevo_nodo # En siguiente de la cola va a apuntar al nuevo nodo
            self.cola = nuevo_nodo # A la vez la cola para a valer el nuevo nodo ya que pasa a ser el ultimo elemento de mi lista
        self.tamanio += 1 # Le sumo 1 al tamaño



s = Single_Linked_List()
s.append('P')
s.append('R')
s.append('U')
s.append('E')
s.append('B')
s.append('A')

print(s)
