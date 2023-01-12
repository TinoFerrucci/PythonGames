from random import *
import os

def crearCartones(nombres):
    cartones = {}
    for nombre in nombres:
        lista = [num for num in range(1, 100)]
        cartones[nombre] = []
        for num in range(20):
            numeroDeLista = choice(lista)
            lista.remove(numeroDeLista)
            cartones[nombre].append(numeroDeLista)
        cartones[nombre].sort()
    return cartones

def crearLoteriaDeNumeros():
    return [num for num in range(1, 100)]

def sacarNumeroDeLoteria(lista, num):
    lista.remove(num)

def elegirNumeroAleatorio(lista):
    return choice(lista)

def sacarNumeroDeCartones(cartones, num):
    for carton, cartonNumeros in cartones.items():
        for index, numero in enumerate(cartonNumeros):
            if num == numero:
                cartonNumeros[index] = "XX"

def evaluarGanador(cartones):
    listaGanadora = ["XX"] * 20
    for carton, cartonNumeros in cartones.items():
        if cartonNumeros == listaGanadora:
            return True
    return False

def imprimirCartones(cartones):
    for carton, cartonNumeros in cartones.items():
        print(carton + "\n")
        for i in range(4):
            print(" ".join([str(x) if len(str(x)) == 2 else "0" + str(x) for x in cartonNumeros[i * 5: (i+1) * 5]]))
        print("\n")

def ganador(cartones):
  lista = []
  for carton, cartonNumeros in cartones.items():
    if cartonNumeros == ["XX"] * 20:
      lista.append(carton)

  return lista

def imprimirGanador(lista):
    if len(lista) > 1:
        print("Felicidades: " + " - ".join(lista) + "\nHan ganado el juego!" + "\n")
    else:
        print("Felicidades " + lista[0] + ", has ganado el juego!" + "\n")

    print("Juego Terminado, gracias por jugar!")
    print("\n\n\n\n\n\n\n\n\nCopyright Constantino Ferrucci - 2023")

def elegirCantidadCartones():
    return int(input("Cantidad de jugadores: "))

def elegirNombreCartones(cantidad):
    nombres = []
    for i in range(cantidad):
        nombres.append(input("Ingrese el nombre del jugador Nº" + str(i + 1) + ": "))
    return nombres


cantCartones = elegirCantidadCartones()
nombres = elegirNombreCartones(cantCartones)
cartones = crearCartones(nombres)
os.system("clear")
lista = crearLoteriaDeNumeros()
print("Los cartones de los jugadores son los siguientes: \n")
imprimirCartones(cartones)
input("\nPulse ENTER para continuar")
os.system("clear")

while not evaluarGanador(cartones):
    numeroElegido = elegirNumeroAleatorio(lista)
    print("Numero elegido:", numeroElegido if len(str(numeroElegido)) == 2 else "0" + str(numeroElegido), "\n")
    sacarNumeroDeLoteria(lista, numeroElegido)
    sacarNumeroDeCartones(cartones, numeroElegido)
    imprimirCartones(cartones)
    input("Pulse ENTER para continuar.")
    os.system("clear")

imprimirGanador(ganador(cartones))
