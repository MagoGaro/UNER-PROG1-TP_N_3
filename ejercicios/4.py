#Enunciado

"""
Dada la siguiente lista: países = [“Argentina,”Brasil”, “Bolivia”,”Paraguay”,”Venezuela”],
realizar lo siguiente:
a. Imprimir la cantidad de elementos que tiene la lista.
b. Imprimir el primer y último elemento.
c. Imprimir el resto.
d. Permitir que el usuario ingrese un país e imprimir el índice si el país se encuentra en
la lista. Si no se encuentra, imprimir un mensaje advirtiendo al usuario.
e. Permitir al usuario ingresar un número igual o menor a la cantidad de elementos de
la lista. Quitar el elemento correspondiente de esa posición.
f. Imprimir la lista en orden inverso.
g. Vaciar la lista.

"""

#Solucion

paises = ['Argentina','Brasil', 'Bolivia','Paraguay','Venezuela']

def cant_elementos(list):
    print(f"La cantidad de elementos de la lista es: {len(list)}\n")

def primer_ulti_ele(list):
    print(f"El primer elemento de la lista es: {list[0]}")
    print(f"El ultimo elemento de la lista es: {list[-1]}\n")

def imprimir_restante(list):
    for i in range(1,len(list)-1):
        print(list[i])
    print("\n")

def buscar_elemento(list):
    ele = input("Ingrese un Pais: ")

    try:
        print(f"El indice de {ele} es: {list.index(ele)}")
    except ValueError:
        print(f"El Elemento {ele} no se encuentra en la lista.")

def borar_elemento(list):
    while True:
        n = input(f"Ingrese un numero entre 0 y {len(list)}: ")

        if n.isdigit():
            n = int(n)
            if n >= 0 and n <= len(list):
                del list[n]
                print("\nElemento Borrado.")
                print(list)
                break
            else:
                print("Numero fuera de rango, Ingrese otro")
        else:
            print("Solo se aceptan numeros.")

def imprimir_reverso(list):
    print(list[::-1])

def vaciar_lista(list):
    list.clear()
    print(list)



#ejecucion
cant_elementos(paises)
primer_ulti_ele(paises)
imprimir_restante(paises)
buscar_elemento(paises)
imprimir_reverso(paises)
vaciar_lista(paises)