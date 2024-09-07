import random

def adivinar_numero():
    numero_secreto = random.randint(1, 100)
    intentos = 7
    while intentos > 0:
        intento = int(input("Adivina el número (entre 1 y 100): "))
        if intento == numero_secreto:
            print("¡Correcto! Adivinaste el número.")
            break
        elif intento < numero_secreto:
            print("El número es mayor.")
        else:
            print("El número es menor.")
        
        intentos -= 1
        print(f"Te quedan {intentos} intentos.")
    
    if intentos == 0:
        print(f"Te quedaste sin intentos. El número era {numero_secreto}.")

adivinar_numero()
