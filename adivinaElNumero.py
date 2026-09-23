import random

numero_secreto = random.randint(1, 10)

intentos = 0

while True:
    intento = int(input("Adivina el número (entre 1 y 10): "))
    intentos += 1

    if intento == numero_secreto:
        print(f"¡Correcto! Adivinaste el número en {intentos} intentos.")
        break
    elif intento < numero_secreto:
        print("Muy bajo, intenta de nuevo.")
    else:
        print("Muy alto, intenta de nuevo.")