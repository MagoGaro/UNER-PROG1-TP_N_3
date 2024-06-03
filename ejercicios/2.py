#Enunciado

"""
Pedir al usuario que ingrese 5 números para luego almacenarlos en una lista y ordenarlos.
Imprimir por pantalla el resultado

"""

#Solucion

num1 = []

def insertar_n():
    for i in range(5):
        n = int(input("Ingrese un numero: "))
        num1.append(n)
    

def mostrar_ord():
    num1.sort()
    for i in num1:
        print(f"{i}",end=" ")

#Ejecución
print("\nIngrese 5 números\n")
insertar_n()
print("\nLos números ingresados en orden son: \n")
mostrar_ord()