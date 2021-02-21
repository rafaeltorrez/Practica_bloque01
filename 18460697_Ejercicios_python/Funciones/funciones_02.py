print("=========================================================")
print("           Ejercicio 2 de funciones                      ")
print("=========================================================")

radio=5
pi=3.14
def area_circulo(radio):
    #la formula del circulo es a=pi*r**2
    area=pi*radio**2 
    print("El area del circulo es de: ", round(area,2))  
area_circulo(radio)