print("=========================================================")
print("           Ejercicio 3 de funciones                      ")
print("=========================================================")

def relacion (numero1,numero2): 
    if numero1>numero2:
        return 1  
    elif numero1<numero2:
        return -1
    elif numero1==numero2:
        return 0
print(relacion(5,10))
print(relacion(10,5))
print(relacion(5,5))