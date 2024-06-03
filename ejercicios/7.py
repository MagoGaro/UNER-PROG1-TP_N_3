#Enunciado

"""
Escriba un programa Python que cuente con dos listas, la primera de ellas almacenará strings
con tareas pendientes y la segunda almacenará strings con tareas terminadas. Permita al
usuario:
a. Agregar nuevas tareas pendientes.
b. Marcar las tareas pendientes como terminadas. Al hacer esto, la tarea deberá pasar
de la lista de pendientes a la de terminadas.
Nota: posterior a cada operación deberá mostrar por pantalla el estado actual de ambas
listas.

"""

#Solucion

pendientes = []
terminiadas = []

def mostrar_estado(list,t):

    if len(list) == 0:
        print(f"\nNo hay tareas {"pendientes" if t == 1 else "realizadas"}\n")
    else:
        print(f"\nSus tareas {"pendientes" if t == 1 else "realizadas"}:")
        for i in range(len(list)):
            print(f"{i+1} - {list[i]}")
    

def menu():
    print("""
    Bienvenidos al sistema de gestion de tareas
""")
    while True:
        x = input("""Seleccione una opcion:
                a - Agregar Tarea Pendiente
                b - Marcar Tarea Como realizada
                
                  Ingresar seleccion: """)

        if x.lower() == 'a':
            mostrar_estado(pendientes,1)
            mostrar_estado(terminiadas,0)
            ta = input("Ingrese Tarea: ")
            pendientes.append(ta)
        elif x.lower() == 'b':
            mostrar_estado(pendientes,1)
            mostrar_estado(terminiadas,0)

            n = int(input("Ingrese numero de la tarea: "))

            terminiadas.append(pendientes[n-1])
            pendientes.remove(pendientes[n-1])
        else:
            print("Opcion invalida")
        
        y = input("Desea elegir otra opcion? (s/n):")

        if y.lower() == "s":
            pass
        else:
            break
        


#ejecucion
menu()