#Enunciado

"""
Dada la siguiente lista de frutas [“banana”, “manzana”, “pera”], permitir al usuario ingresar 3
frutas más para agregarlas al final de lista. Luego, mostrar por pantalla la lista completa y
debajo la misma lista pero sólo con las frutas que añadió el usuario

"""

#Solucion

frutas1 = ['banana', 'manzana', 'pera']

def agregar_frutas(n):
    print(f"Por favor ingrese {n} frutas mas")
    for i in range(n):
        fruta = input("Ingrese fruta: ")
        frutas1.append(fruta)

def mostrar_listado(listado):
    print("\nListado completo de frutas:")
    for f in frutas1:
        print(f)

    print("\nLas frutas que usted agrego:")
    for i in range(len(frutas1)):
        if i > 2:
            print(frutas1[i])
    
#ejecucion
agregar_frutas(3)
mostrar_listado(frutas1)

