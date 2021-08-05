#!/usr/bin/env python3

import time
import paramiko

from getpass import getpass

HOST = 'xxx.xxx.xxx.xxx' # IP del servidor al cual me quiero conectar
USER = 'root' # Usuario con el que quiero autenticarme, en mi caso root

if __name__ == '__main__':
    client = paramiko.SSHClient() # Uso la clase SSHClient, a partir de este objeto puedo establecer la conexion con el servidor y realizar los comandos que desee
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    password = getpass('Ingrese su contraseña: ') # Indico que se ingrese la contraseña por teclado para no tener que dejarla en texto plano
    client.connect(HOST, username=USER, password=password) # username para indicar con que usuario deseo loguearme
    
    stdin, stdout, stderr = client.exec_command('ls') # Recibe como parametro los comandos que quiero ejecutar en mi servidor

    time.sleep(1)

    result = stdout.read().decode()

    print(result)
