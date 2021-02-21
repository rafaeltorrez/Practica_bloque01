print("====================================================================")
print("                 Ejercicio 4 de datos compuestos                    ")
print("====================================================================")

i=1
numeros=[]
print("Serie del 1 al 10")
print("_______________________________________________________________________")
while i<=10:
      #print(i)
      numeros.append(i)
      i+=1
print(numeros)

print("Serie del 10 al 1")
print("________________________________________________________________________")
j=10
while j<=1:
     print(i)
     numeros.append(i)
     i-=1
numeros.reverse()
print(numeros)