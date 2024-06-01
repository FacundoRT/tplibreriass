"""Escriba una función redondear() que permita redondear un número
decimal de acuerdo al criterio: Si el número es mayor a 3.50, devolver el
entero siguiente (en este caso, 4), si no devolver el entero inmediatamente
anterior (3).
2. Coloque el módulo del ejercicio anterior dentro de un paquete. En un
módulo que esté fuera de ese paquete, cree una función de suma de
decimales que redondee el resultado haciendo uso de la función
redondear() del paquete recién creado.
3. Usando el módulo datetime, escribe un programa que muestre la fecha
y hora actuales del sistema.
4. Escriba un programa que devuelva un número par al azar entre 2 y 10
(pista: para comprobar si se pueden generar todos los números, pruebe
ejecutar el programa dentro de un ciclo infinito).
5. Bola mágica: La bola mágica (Magic 8 ball) es un popular juguete usado
para la adivinación o para buscar consejo. Su mecanismo es muy simple:
ante una pregunta del usuario, la bola responde con una de 8 posibles
respuestas:
- Es seguro que sí
- Las chances son buenas
- Puedes contar con ello
- Pregúntame de nuevo más tarde
- Concéntrate y pregunta de nuevo
- No veo con claridad, intenta de nuevo
- Mi respuesta es no
- Mis fuentes me dicen que no
Escriba una función en Python para simular la bola mágica.
6. Encuentre el tiempo de ejecución de los programas de los ejercicios
anteriores (pista: use el módulo time)"""

#LO ESCRIBI COMO UNA LISTA DE OPCIONES A LOS PUNTOS 
import random
from datetime import datetime
import time


def redondear(numero):
    if numero > 3.50:
        return int(numero) + 1
    else:
        return int(numero)


def suma_redondeada(a, b):
    suma = a + b
    return redondear(suma)


def mostrar_fecha_hora_actual():
    ahora = datetime.now()
    print("Fecha y hora actuales:", ahora)


def numero_par_azar():
    return random.choice([2, 4, 6, 8, 10])


def bola_magica():
    respuestas = [
        "Es seguro que sí",
        "Las chances son buenas",
        "Puedes contar con ello",
        "Pregúntame de nuevo más tarde",
        "Concéntrate y pregunta de nuevo",
        "No veo con claridad, intenta de nuevo",
        "Mi respuesta es no",
        "Mis fuentes me dicen que no"
    ]
    return random.choice(respuestas)


def medir_tiempo(funcion, *args):
    inicio = time.time()
    resultado = funcion(*args)
    fin = time.time()
    tiempo_ejecucion = fin - inicio
    return resultado, tiempo_ejecucion


def menu():
    while True:
        print("\nSeleccione una opción:")
        print("1. Redondear un número")
        print("2. Sumar dos números y redondear el resultado")
        print("3. Mostrar la fecha y hora actuales")
        print("4. Obtener un número par al azar entre 2 y 10")
        print("5. Hacer una pregunta a la bola mágica")
        print("6. Salir")
        
        opcion = input("Ingrese el número de la opción deseada: ")
        
        if opcion == "1":
            numero = float(input("Ingrese un número decimal: "))
            resultado, tiempo = medir_tiempo(redondear, numero)
            print(f"Resultado de redondear({numero}): {resultado}, Tiempo de ejecución: {tiempo:.6f} segundos")
        
        elif opcion == "2":
            a = float(input("Ingrese el primer número decimal: "))
            b = float(input("Ingrese el segundo número decimal: "))
            resultado, tiempo = medir_tiempo(suma_redondeada, a, b)
            print(f"Resultado de suma_redondeada({a}, {b}): {resultado}, Tiempo de ejecución: {tiempo:.6f} segundos")
        
        elif opcion == "3":
            _, tiempo = medir_tiempo(mostrar_fecha_hora_actual)
            print(f"Tiempo de ejecución de mostrar_fecha_hora_actual: {tiempo:.6f} segundos")
        
        elif opcion == "4":
            resultado, tiempo = medir_tiempo(numero_par_azar)
            print(f"Resultado de numero_par_azar: {resultado}, Tiempo de ejecución: {tiempo:.6f} segundos")
        
        elif opcion == "5":
            pregunta = input("Haz tu pregunta a la bola mágica: ")
            resultado, tiempo = medir_tiempo(bola_magica)
            print(f"Bola mágica dice: {resultado}, Tiempo de ejecución: {tiempo:.6f} segundos")
        
        elif opcion == "6":
            print("Adiós")
            break
        
        else:
            print("Opción no válida. Por favor, intente de nuevo.")

menu()

