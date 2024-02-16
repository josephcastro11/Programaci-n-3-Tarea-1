# Importamos las librerías necesarias para ejecutar el programa, os para interactuar con el sistema operativo, y graphviz para poder realizar la gráfica
import os
import graphviz
from graphviz import Digraph

#Creamos la ruta donde se va a ejecutar el dot necesario para realizar la grafica
os.environ["PATH"] += os.pathsep + "C:/Program Files/Graphviz/bin"


#Creamos la clase nodo con las variables de los datos que vamos a usar
class Nodo:
    #Creamos la funcion init que guardara nuestra variables
    def __init__(self, nombre, apellido, carnet):
        self.nombre = nombre
        self.apellido = apellido
        self.carnet = carnet
        self.anterior = None
        self.siguiente = None

#Creamos la clase donde se realizará la Lista Doblemente Enlazada
class ListaDoblementeEnlazada:
    #Creamos la funcion init donde le indicamos que tanto el inicio como el final están vacíos al principio
    def __init__(self):
        self.cabeza = None
        self.cola = None

    #Creamos la funcion insertar inicio
    def insertar_al_principio(self, nombre, apellido, carnet):
        nuevo_nodo = Nodo(nombre, apellido, carnet)
        if not self.cabeza:
            self.cabeza = nuevo_nodo
            self.cola = nuevo_nodo
        else:
            nuevo_nodo.siguiente = self.cabeza
            self.cabeza.anterior = nuevo_nodo
            self.cabeza = nuevo_nodo
    
    #Creamos la funcion insertar al final
    def insertar_al_final(self, nombre, apellido, carnet):
        nuevo_nodo =   Nodo(nombre, apellido, carnet)
        if not self.cabeza:
            self.cabeza = nuevo_nodo
            self.cola = nuevo_nodo
        else:
            nuevo_nodo.anterior = self.cabeza
            self.cola.siguiente = nuevo_nodo
            self.cola = nuevo_nodo
    
    #Creamos la funcion elimar por valor
    def eliminar_por_valor(self, carnet):
        nodo_actual = self.cabeza
        while nodo_actual:
            if nodo_actual.carnet == carnet:
                if nodo_actual.anterior:
                    nodo_actual.anterior.siguiente = nodo_actual.siguiente
                else:
                    self.cabeza = nodo_actual.siguiente

                if nodo_actual.siguiente:
                    nodo_actual.siguiente.anterior = nodo_actual.anterior
                else:
                    self.cola = nodo_actual.anterior

                return
            nodo_actual = nodo_actual.siguiente

    #Creamos la función que muestra nuestra lista
    def mostrar_lista(self):
        nodo_actual = self.cabeza
        print(" ", end=" <- ")
        while nodo_actual:
            print(f"{nodo_actual.nombre} {nodo_actual.apellido} ({nodo_actual.carnet})", end=" <-> ")
            nodo_actual = nodo_actual.siguiente
        print(" ")

    #Creamos la función que genera nuestro grafo
    def generar_grafo(self, filename="lista_doble"):
        dot = Digraph(comment='Lista Doble Enlazada', format='png', engine='dot')
        actual = self.cabeza
        while actual:
            dot.node(str(actual.carnet), f"{actual.nombre} {actual.apellido}\n({actual.carnet})")
            if actual.anterior:
                dot.edge(str(actual.anterior.carnet), str(actual.carnet), dir='both')
            actual = actual.siguiente

        dot.render(filename, format='png', cleanup=True)

#Iniciamos nuestro menú
if __name__ == "__main__":
    nuevalista = ListaDoblementeEnlazada()
    #Creamos el bucle de nuestro menú
    while True:
        print("\n1. Insertar al principio")
        print("2. Insertar al final")
        print("3. Eliminar por carnet")
        print("4. Mostrar lista")
        print("5. Generar Grafo")
        print("6. Salir")

        opcion = input("Ingrese su elección: ")

        if opcion == '1':
            nombre = input("Ingrese el nombre: ")
            apellido = input("Ingrese el apellido: ")
            carnet = input("Ingrese el carnet: ")
            nuevalista.insertar_al_principio(nombre, apellido, carnet)
        elif opcion == '2':
            nombre = input("Ingrese el nombre: ")
            apellido = input("Ingrese el apellido: ")
            carnet = input("Ingrese el carnet: ")
            nuevalista.insertar_al_final(nombre, apellido, carnet)
        elif opcion == '3':
            carnet = input("Ingrese el carnet a eliminar: ")
            nuevalista.eliminar_por_valor(carnet)
        elif opcion == '4':
            nuevalista.mostrar_lista()
        elif opcion == '5':
            nuevalista.generar_grafo()
        elif opcion == '6':
            break
        else:
            print("Opción no válida. Por favor, ingrese una opción válida.")
