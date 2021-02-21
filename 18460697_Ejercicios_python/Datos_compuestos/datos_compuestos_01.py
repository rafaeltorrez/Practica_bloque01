print("====================================================================")
print("                 Ejercicio 1 de datos compuestos                    ")
print("====================================================================")
#creamos nuestra funcion
def separar_lista():
    #definimos una lista con los valores
    lista=[5,13,23,56,70,20,5,11,64,100,99,7]
    #definimos otra lista en la que se van a guardar los numeros pares
    num_pares=[]
    #definimos otra listas en la que se van a guardar los numeros impares
    num_impar=[]
    print("Lista de los numeros capturados")
    print(lista)
    print("_________________________________________________________________")
    print("Lista de numeros pares")
    #Utilizamos el ciclo for para recorra toda nuestra lista
    for i in lista:
        #Hacemos una comparacion si lo que esta en la posicion de i le aplicamos el modulo y si el resultado es cero es par
        if i %2==0:
            #Ese valor lo guardamos en nuestra lista de num_pares
            num_pares.append(i)
            #con la instrucciion sort lo ordenamos
            num_pares.sort()
        else:
            #Si no entro en la 1 primera condicion entonces el numero es impar 
            #Ese valor lo guardamos en la lista num_impar
            num_impar.append(i)
            num_impar.sort()
    print(num_pares)
    print("_______________________________________________________________")
    print("Lista de numeros impares")
    print(num_impar)
separar_lista()