#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def factorial_recursivo(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial_recursivo(n-1)

print(factorial_recursivo(5))

"""
RECURSIVIDAD: Se refiere a una situación en la que una función se llama a sí misma una y otra vez

VENTAJA: La recursividad es más clara y simple para dividir problemas complejos en piezas manejables
         Los códigos recursivos son más consistentes que el código con iteración
         Solo hay una sentencia en el método de recursividad, en cambio en el de iteración hay mas de una sentencia
         Soluciona problemas recurrentes
         Son programas cortos y de facil lectura

DESVENTAJA: Como la función se llama a si misma esto hace que involucre tiempo y espacio, por lo tanto hace que utilice mucha memoria
            de la pila de datos para trabajar los resultados. Por lo tanto esta función no es tan eficiente como la iterativa
            El mayor problema que presenta es que causa un error denominado: stack overflow
            Crea muchas variables
            Puede necesitar mucha memoria

La recursividad usa la pila por lo tanto facilita las llamadas recursivas. Esto significa que una función
es libre de llamarse de nuevo, porque se creará un nuevo stack frame para todas sus variables
locales. Entonces al ejecutarse por primera vez la función se guardarán la variables, si la función se
llama así misma guardará las variables nuevamente en la pila, junto a las variables anteriores. Si
nosotros hacemos que la función se llame miles de veces las variables ocupan demasiada memoria,
si queremos ejecutar varias instrucciones repetitivamente debemos de usar una iteración ya que no
usa la pila

Registro de activacion no es otra pila, es todo la misma pila

"""
