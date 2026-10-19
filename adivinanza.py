import random

def juego_adivinanza():
    print("¡Bienvenido al juego de adivinanza de números!")
    print("He pensado en un número entre 1 y 100. ¿Puedes adivinar cuál es?")

    # Genera un número aleatorio entre 1 y 100
    numero_secreto = random.randint(1, 100)
    intentos = 0
    adivinado = False

    # El bucle se repite hasta que el usuario adivine el número
    while not adivinado:
        try:
            # Pedimos al usuario que ingrese un número
            intento_usuario = int(input("\nIngresa tu número: "))
            intentos += 1

            # Comparamos el número ingresado con el secreto
            if intento_usuario < numero_secreto:
                print("Demasiado bajo. Intenta con uno más alto.")
            elif intento_usuario > numero_secreto:
                print("Demasiado alto. Intenta con uno más bajo.")
            else:
                adivinado = True
                print(f"\n¡Felicidades! ¡Adivinaste el número {numero_secreto}!")
                print(f"Lo lograste en {intentos} intentos.")

        except ValueError:
            # Esto se ejecuta si el usuario escribe letras o deja vacío en lugar de un número
            print("Por favor, ingresa un número válido.")

if __name__ == "__main__":
    juego_adivinanza()