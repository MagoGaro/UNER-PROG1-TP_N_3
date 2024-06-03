#Enunciado

"""
Crear un programa que almacene en una lista las materias de esta u otra carrera y que las
muestre por pantalla. (La lista debe ser predefinida, no debe ser ingresada por el usuario)

"""

#Solucion

tudw = ['Progrmación I','Progrmación II','Progrmación III','Introducción a la Informática','Ingeniería de Software','Bases de Datos','Arquitectura de Computadoras','Desarrollo de Aplicaciones Web','Introducción al Desarrollo Web','Redes de Datos','Sistemas Operativos','Diseño Gráfico']

def mostrar_materias(lista):
    for m in lista:
        print(m)
    print("\n")

#Ejecución

print("\nListado Materias Tecnicatura Universitaria en Desarrollo Web - UNER: \n")
mostrar_materias(tudw)