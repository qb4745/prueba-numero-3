import random
import numpy as np
import string

lista = ["                                 " for x in range(15)]  #creamos una lista con caracteres de spacio para poder modificar en numpy
arreglo = np.array(lista).reshape(5,3)                 #divimos la lista en un arreglo multidimensional para poder trabajar con el
datos_requeridos = ["NIF:      ", "Nombre:   ", "Edad:     "]
cont = -1

#Funcion para validar si una string(cadena) contiene solo letras
def rev_letras(revisar):
    for letra in revisar:
        if letra not in string.ascii_letters:
            return False
    return True
#Funcion para validar si una string(cadena) contiene solo numeros
def rev_numeros(checkar):
    for numero in checkar:
        if numero not in string.digits:
            return False
    return True


def GrabarNif():
    global arreglo
    global Gr_NIF
    global nif_verificado
    global cont
    print("***** Siga los pasos para Grabar NIF *****")
    while True:
        print("Digite NIF sin puntos y con Guion. Ejemplo 99999999-RTX")
        Gr_NIF = input()
        if Gr_NIF[-4] == "-": #Comprobamos que el NIF tenga guion en la posicion -4
            nif, dv = Gr_NIF.split("-")
            ver_nif = rev_numeros(nif)
            if len(Gr_NIF) == 12 and ver_nif == True and len(dv) == 3: #Validar que el nif tenga 12 caracteres y que sea numerico y el digito verificador tenga 3 caracteres
                cont += 1 #cuando se verifica el nif se incrementa el contador
                nif_verificado = Gr_NIF
                arreglo[cont][0] = Gr_NIF  #despues de la validacion agrego el nif a mi arreglo.
                                        #con el contador como indice se pueden puedes agregar los datos de varios usuarios a tu arreglo
                break
            else:
                print("NIF no es valido intente nuevamente.\n")
        print("NIF no es valido intente nuevamente.\n")
    while True:
        print("Ingrese Nombre. Ejemplo: Jaime Vicencio")
        gr_nombre = input()
        rev_nombre = rev_letras(gr_nombre)
        if len(gr_nombre) >= 8:
            arreglo[cont][1] = gr_nombre #despues de la validacion agrego el nombre a mi arreglo.
            break
        else:
            print("Nombre no es vàlido.")
    while True:
        print("Ingrese Edad. Ejemplo: 42")
        try:
            gr_edad = int(input())
            if gr_edad >= 0:
                arreglo[cont][2] = gr_edad #despues de la validacion agrego la edad a mi arreglo.
                print("Datos Ingresados correctamente.\n")
                return cont
            else:
                print("Nombre no es vàlido.")
                
        except:
            print("Edad no valida, vuelva a intentarlo")
   
def BuscarNif():
    print("***** Siga los pasos para Buscar NIF *****")
    while True:
        print("Digite NIF sin puntos y con Guion. Ejemplo 99999999-RTX")
        bu_nif = input()
        if bu_nif in arreglo: #aca comprobamos que el nif que se busca este en el arreglo
            print("NIF verificado correctamente.\n")
            for nif in arreglo:             #aca nos crea una lista con los datos de cada usuario. Ejemplo lista = ['99999999-rtx', 'jaime vicencio', '42']
                if nif[0] == bu_nif:        #aca nos crea una lista con los datos de cada usuario. Ejemplo lista = ['99999999-rtx', 'jaime vicencio', '42']
                    lista_datos = nif       #aca nos crea una lista con los datos de cada usuario. Ejemplo lista = ['99999999-rtx', 'jaime vicencio', '42']
            for requerido,dato in zip(datos_requeridos,lista_datos):  
                        print(requerido,dato)
                        print()
            print(f"NIF: {bu_nif}, pertenece a la Union Europea")
            print()
            break
        else:
            print("NIF no es valido intente nuevamente.\n")

def ImprimirCert():
    print("***** Siga los pasos para Imprimir Certificados *****")
    while True:
        print("Digite NIF sin puntos y con Guion. Ejemplo 99999999-RTX")
        impr_nif = input()
        fecha_nac = "12 de Enero 1972"
        estado_con = "Casado/a"
        miembro = "SI"
        if impr_nif in arreglo: #aca comprobamos que el nif que se busca este en el arreglo
            for nif in arreglo:            #aca nos crea una lista con los datos de cada usuario. Ejemplo lista = ['99999999-rtx', 'jaime vicencio', '42']
                if nif[0] == impr_nif:     #aca nos crea una lista con los datos de cada usuario. Ejemplo lista = ['99999999-rtx', 'jaime vicencio', '42']
                    lista_datos = nif       #aca nos crea una lista con los datos de cada usuario. Ejemplo lista = ['99999999-rtx', 'jaime vicencio', '42']
            print("NIF verificado correctamente.\n")
            print("1.- Certificado de Nacimiento.\n2.- Certificado Estado Conyugal.\n3.- Certificado Estado Conyugal.\n4.- Salir.\n ")
            try:
                imprimir_op = int(input())
                if imprimir_op >= 1 and imprimir_op <= 4:
                    if imprimir_op == 1:
                        print("***** Certificado de Nacimiento *****")
                        print(f"Nombre:                {lista_datos[1]}") #imprimimos el nombre desde nuestra lista creada con el usuario que corresponde
                        print(f"NIF:                   {lista_datos[0]}")
                        print(f"Edad:                  {lista_datos[2]}")
                        print(f"Fecha Nacimiento:      {fecha_nac})")
                        break
                    if imprimir_op == 2:
                        print("***** Certificado Estado Conyugal *****")
                        print(f"Nombre:                {lista_datos[1]}")
                        print(f"NIF:                   {lista_datos[0]}")
                        print(f"Edad:                  {lista_datos[2]}")
                        print(f"Estado Conyugal:       {estado_con})")
                        break
                    if imprimir_op == 3:
                        print("***** Certificado Pertenencia Union Europea *****")
                        print(f"Nombre:                {lista_datos[1]}")
                        print(f"NIF:                   {lista_datos[0]}")
                        print(f"Edad:                  {lista_datos[2]}")
                        print(f"Miembro Union Europea: {miembro}")
                        break
                    if imprimir_op == 4:
                        break                        
            except:
                print("Opcion no Vàlida. Vuelva a intentarlo")
        else:
            print("nif no registrado.")            
    
def Salir():
    print("Realizado por Jaime Vicencio Rubilar. Adìos")
    return 
        
def ImprimirArreglo():
    print(arreglo)               

    


#arreglo = [[str(0) for x in range(3)] for x in range(5)]