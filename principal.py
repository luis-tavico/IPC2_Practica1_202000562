from listaEnlazada import ListaEnlazada
from modeloOrden import Orden
from modeloShuco import Shuco
from grafica import Graficar

class Principal:
    def __init__(self):
        self.ordenes = ListaEnlazada()
        self.menuPrincipal()

    def menuPrincipal(self):
        numeroOrden = 0
        tiempoEnCola = 0
        while True:
            print(" -----Menu Principal-----")
            print("| 1. Nueva orden         |")
            print("| 2. Entregar orden      |")
            print("| 3. Ver ordenes         |")
            print("| 4. Acerca de           |")
            print("| 5. Salir               |")
            print(" ------------------------ ")
            try:
                opcion = int(input("Ingrese una opcion: "))
                if opcion == 1:
                    nombreCliente = input("\nIngrese el nombre del cliente: ")
                    cantidad = int(input("Ingrese la cantidad de shucos: "))              
                    shucos = ListaEnlazada()
                    tiempoTotal = 0
                    for numero in range(cantidad):
                        print("-Shuco No.", str(numero+1))
                        tiempo = 0        
                        ingrediente = input("Ingrese el ingrediente: ")
                        if ingrediente.lower() == "salchicha":
                            tiempo = 2
                        elif ingrediente.lower() == "chorizo":
                            tiempo = 3
                        elif ingrediente.lower() == "salami":
                            tiempo = 1.5
                        elif ingrediente.lower() == "longaniza":
                            tiempo = 4
                        elif ingrediente.lower() == "costilla":
                            tiempo = 6
                        tiempoTotal += tiempo      
                        tiempo = str(tiempo)+" minutos"
                        nuevoShuco = Shuco(ingrediente, tiempo)
                        shucos.push(nuevoShuco)
                    tiempoEnCola += tiempoTotal
                    numeroOrden += 1
                    tiempoTotal = str(tiempoTotal)+" minutos"
                    nuevaOrden = Orden(numeroOrden, nombreCliente, cantidad, shucos, tiempoTotal, str(tiempoEnCola))
                    self.ordenes.push(nuevaOrden)
                    print("")
                elif opcion == 2:      
                    ordenTerminada = self.ordenes.pop()
                    if ordenTerminada != None:
                        grafica = Graficar()
                        grafica.graficarOrdenTerminada(ordenTerminada)
                    else:
                        print("\n¡Sin ordenes!\n")
                elif opcion == 3:
                    ordenes = self.ordenes.values()
                    if ordenes == None:
                        print("\n¡Sin ordenes!\n")
                    else:
                        grafica = Graficar()
                        grafica.graficarOrdenes(ordenes)
                elif opcion == 4:
                    print("\nUniversidad de San Carlos de Guatemala")
                    print("Facultad de Ingenieria")
                    print("Escuela de Ciencias y Sistemas")
                    print("Introduccion a la Programacion y Computacion 2")
                    print("Seccion: N")
                    print("Ing: Edwin Zapeta")
                    print("Nombre: Pedro Luis Pu Tavico")
                    print("Carnet: 202000562\n")
                elif opcion == 5:
                    print("\n¡Ejecucion Finalizada!\n")
                    break
                else: 
                    print("\n¡Ingrese una opcion valida!\n")
            except ValueError:
                print("\n¡Ingrese solo numeros!\n")

if __name__ == "__main__":
    Principal()
