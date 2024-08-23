#Un codigo que de un numero al azar si el nombre ingresado tiene 6 letras
import random

print("si su nombre posee la cantidad de letras correcta se le regalara un numero para la loteria")
nombre= input("Ingrese su nombre: ")


if len (nombre) == 6:
    numero_aleatorio = random.randint(1,400)
    print(f"Numero asignado: {numero_aleatorio}")
else:
    print("Gracias por su intento de participar")