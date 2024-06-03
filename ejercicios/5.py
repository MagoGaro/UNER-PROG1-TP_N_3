#Enunciado

"""
Escriba un programa Python que solicite al usuario el ingreso de números enteros. Cuando el
usuario ingrese la palabra “fin” el programa deberá concluir con la carga de datos.  Cada uno
de los números ingresados por el usuario deberá ser almacenado en una lista. A
continuación, realice las siguientes tareas:
a. Determinar el máximo.
b. Obtener segundo valor máximo. Es decir el que le sigue al máximo.
c. Determinar el mínimo.
d. Calcular la multiplicación de  todos los números de la lista.
e. Contar los valores pares e impares.
f. Remover los elementos repetidos

"""

#Solucion

listado = []

def ingresar_datos():
    corte = ""
    
    while corte != "fin":
        n = input("Ingrese numeros enteros para finalizar escriba 'Fin': ")

        if n.isdigit():
            n = int(n)
            listado.append(n)
        elif n.isalpha():
                corte = n.lower()
    
def maximo(list):
     return max(list)

def maximo_dos(list):
     lista2 = sorted(list, reverse=True)
     return lista2[1]

def minimo(list):
     return min(list)

def multiplicar(list):
    r = 1

    for x in list:
        r *=x
    
    return r

def par_impar(list):
    par = 0
    impar = 0

    for e in list:
        if e %2 == 0:
              par +=1
        else:
             impar +=1

    print(f"La cantidad de Numeros pares es: {par}")
    print(f"La cantidad de Numeros impares es: {impar}")
    
def eliminar_repetidos(lista):
     listado = list(set(lista))
     return listado
    
#Ejecucion
ingresar_datos()
print(f"\nEl maixmo es: {maximo(listado)}")
print(f"\nEl segundo numero mas alto es: {maximo_dos(listado)}")
print(f"\nEl minimo es: {minimo(listado)}")
print(f"\nLa multiplicacion de los valores de la lista da: {multiplicar(listado)}\n")
par_impar(listado)
print(f"\nLa lista sin elementos repetidos: \n{eliminar_repetidos(listado)}")