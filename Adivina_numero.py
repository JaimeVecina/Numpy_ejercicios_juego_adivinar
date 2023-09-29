import random

numero_azar = random.randint(1, 100)

intentos = 0
adivinado = False

print("Adivine el numero al azar")

while not adivinado:
    intento = input("Escribe tu número o escribe 'salir' para abandonar: ")

    if intento.lower() == 'salir':
        print("El número secreto era", numero_azar)
        break

    try:
        intento = int(intento)
    except ValueError:
        print("Por favor, ingresa un número válido.")
        continue

    intentos += 1

    if intento < numero_azar:
        print("El número secreto es más alto. Intentelo de nuevo.")
    elif intento > numero_azar:
        print("El número secreto es más bajo. Intentelo de nuevo")
    else:
        print(f"Felicidades, has adivinado el número secreto {numero_azar} en {intentos} intentos.")
        adivinado = True
