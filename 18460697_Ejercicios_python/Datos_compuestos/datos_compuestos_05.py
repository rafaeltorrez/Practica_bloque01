print("====================================================================")
print("                 Ejercicio 5 de datos compuestos                    ")
print("====================================================================")

baraja=(5,1,5,5,6)
def poker(baraja,sipoker,nopoker):
        for i in range(len(baraja)):
            if baraja[i]==5:
                sipoker+=1
            else:
                nopoker+=1
        if sipoker==4:
            print("Conseguiste un poker de {}")
        else:
             print("No lograste conseguir un poker")
poker(baraja,0,0)