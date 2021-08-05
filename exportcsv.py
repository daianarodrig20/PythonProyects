#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

import pwd

archivo = open("proyecto.csv", "w")
entries = pwd.getpwall()

for row in entries:
    e = row[0:6]
    
    archivo.write(e[1])
    archivo.write(";")

    archivo.write(str(e[2]))
    archivo.write(";")

    archivo.write(str(e[3]))
    archivo.write(";")

    archivo.write(str(e[4]))
    archivo.write(";")

    archivo.write(str(e[5]))
    archivo.write(";")

    archivo.write("\n")

print("Archivo csv creado")
archivo.close()
