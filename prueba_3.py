import prueba_3_funciones as fn
import random
import numpy as np
import string

while True:
    print("***** NÚMERO DE IDENTIFICACIÓN FISCAL *****")
    print("1.- Grabar NIF.\n2.- Buscar NIF.\n3.- Imprimir Certificados.\n4.- Salir.\n")
    try:
        menu_op = int(input())
        if menu_op >=1 and menu_op <=5:
            if menu_op == 1:
                fn.GrabarNif()
            elif menu_op == 2:
                fn.BuscarNif()
            elif menu_op == 3:
                fn.ImprimirCert()
            elif menu_op == 4:
                fn.Salir()
                break
            elif menu_op == 5:
                print("*** Menu oculto para revisar info en arreglo ***")
                fn.ImprimirArreglo()
                                     
    except:
        print("Opciòn no Valida. Intente nuevamente.\n")