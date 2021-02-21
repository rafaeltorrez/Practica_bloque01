print("====================================================================")
print("                 Ejercicio 3 de datos compuestos                    ")
print("====================================================================")
#Declaramos nuestro iterador 
i=0
#declaramos una lista en la que vamos a ir almacenando los valores 
lista=[]
#en la loteria solo son 6 numeros haci que el ciclo va de 0 a hasta 5
while i<6:
        #Le pedimos al usuario que capture el numero del boleto
        numero=int(input("Ingresa el numero del boleto de la loteria "))
        #condicion si el numero ingresado esta en el rango del 1 al 49 
        if numero>=1 and numero<=49:
                #guardamos el valor en la lista, pasandole como parametro el numero
                lista.append(numero)
                #incrementamos nuestro contador
                i+=1
        else:
              print("Solo puedes ingresar numeros del 1 al 49")
print("Numeros capturados de la loteria")                                         
print(lista)
print("______________________________________________________________________")
print("Lista ordenada de menor a mayor")
lista.sort()
print(lista)
