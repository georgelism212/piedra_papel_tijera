import random

def juego_ppt():
    opciones = ['piedra', 'papel', 'tijera']
    
    # El jugador elige una opción
    jugador = input("Elige piedra, papel o tijera: ").lower()
    while jugador not in opciones:
        print("Opción inválida. Por favor, elige piedra, papel o tijera.")
        jugador = input("Elige piedra, papel o tijera: ").lower()
    
    # La computadora elige una opción aleatoria
    computadora = random.choice(opciones)
    
    # Determinar el ganador
    if jugador == computadora:
        print(f"Empate. Ambos eligieron {jugador}.")
    elif (jugador == 'piedra' and computadora == 'tijera') or \
         (jugador == 'papel' and computadora == 'piedra') or \
         (jugador == 'tijera' and computadora == 'papel'):
        print(f"Ganaste. La computadora eligió {computadora}.")
    else:
        print(f"Perdiste. La computadora eligió {computadora}.")

# Ejecutar el juego
juego_ppt()
