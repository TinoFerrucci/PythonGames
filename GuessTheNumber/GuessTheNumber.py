from random import randint
import os

def ingresarNumeroCorrecto():
  eleccion = input("Ingrese un numero: ")
  while eleccion not in [str(i) for i in range(1, 101)]:
    eleccion = input("Ingrese un numero por favor: ")
  
  return int(eleccion)

n_maq = randint(1, 101)
intento = 1
n_usuario = ingresarNumeroCorrecto()

while intento <= 8:
	if n_usuario > 100 or n_usuario < 1:
		print("Numero fuera de rango")
	elif n_usuario < n_maq:
		print("Numero incorrecto y menor que el objetivo")
	elif n_usuario > n_maq:
		print("Numero incorrecto y mayor que el objetivo")
	else:
		print("Numero correcto")
		break
	intento += 1
	n_usuario = ingresarNumeroCorrecto()
  os.system("cls")
print(intento)
  

print("Programa terminado")
