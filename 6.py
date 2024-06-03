#Enunciado

"""
Programe una aplicación de consola Python que brinde al usuario la posibilidad de a partir
de una lista vacía:
a. Agregar un elemento al final.
b. Agregar un elemento al principio.
c. Quitar un elemento al final.
d. Quitar un elemento al principio.

"""

#Solucion

lista = []

def ingresar_elemeto():
    e = input("Ingrese elemeto: ")
    return e

def menu():
    while True:
        x = input("""
            Bienvenidos !
            
            a - Agregar un elemento al final
            b - Agregar un elemento al inicio
            c - Eliminar un elemento del final
            d - Eliminar un elemento del inicio
            
            Seleccione una opcion: """)
        
        if x.lower() == 'a':
            lista.append(ingresar_elemeto())
            print(lista)
        elif x.lower() == 'b':
            lista.insert(0,ingresar_elemeto())
            print(lista)
        elif x.lower() == 'c':
            lista.pop()
            print(lista)
        elif x.lower() == 'd':
            lista.pop(0)
            print(lista)
        else:
            print("Opcion incorrecta")
        
        y = input("Desea elegir otra opcion? (s/n):")

        if y.lower() == "s":
            pass
        else:
            break



#Ejecutar
menu()