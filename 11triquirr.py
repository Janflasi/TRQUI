import random
from colorama import Fore, Style

# Variables globales
tablero = [[' ', ' ', ' '],
           [' ', ' ', ' '],
           [' ', ' ', ' ']]
jugador_actual = 'X'
jugadores = {'X': '', 'O': 'Máquina'}

# Función para imprimir el tablero de manera bonita
def imprimir_tablero():
    """
    Imprime el estado actual del tablero en la consola de manera visualmente atractiva.
    """
    print("  " + Fore.YELLOW + "c1 c2 c3" + Style.RESET_ALL)
    for i, fila in enumerate(tablero):
        print(f"r{i + 1}|", end="")
        for casilla in fila:
            if casilla == 'X':
                print(Fore.CYAN + casilla + Style.RESET_ALL + "|", end="")
            elif casilla == 'O':
                print(Fore.MAGENTA + casilla + Style.RESET_ALL + "|", end="")
            else:
                print(Fore.YELLOW + casilla + Style.RESET_ALL + "|", end="")
        print("\n" + "-" * 11)

# Función para verificar si hay un ganador
def verificar_ganador():
    """
    Verifica si hay un ganador en el juego revisando filas, columnas y diagonales.
    Devuelve True si hay un ganador, False en caso contrario.
    """
    for i in range(3):
        if all(tablero[i][j] == jugador_actual for j in range(3)) or all(tablero[j][i] == jugador_actual for j in range(3)):
            return True

    if all(tablero[i][i] == jugador_actual for i in range(3)) or all(tablero[i][2 - i] == jugador_actual for i in range(3)):
        return True

    return False

# Función para realizar un movimiento del jugador
def hacer_movimiento(fila, columna):
    """
    Realiza un movimiento del jugador en el tablero.
    Devuelve True si el movimiento es válido, False si la casilla está ocupada.
    """
    global jugador_actual

    if tablero[fila][columna] == ' ':
        tablero[fila][columna] = jugador_actual
        return True
    else:
        print("Casilla ocupada. Intenta de nuevo.")
        return False

# Función para realizar un movimiento de la máquina
def hacer_movimiento_maquina():
    """
    Realiza un movimiento aleatorio de la máquina en el tablero.
    Devuelve True si el movimiento es posible, False si no hay casillas disponibles.
    """
    global jugador_actual

    casillas_disponibles = [(i, j) for i in range(3) for j in range(3) if tablero[i][j] == ' ']
    if casillas_disponibles:
        fila, columna = random.choice(casillas_disponibles)
        tablero[fila][columna] = jugador_actual
        return True
    else:
        return False

# Función para ingresar nombres de jugadores
def ingresar_nombres():
    """
    Solicita al usuario ingresar el nombre del Jugador X y lo almacena en el diccionario de jugadores.
    """
    global jugadores
    jugadores['X'] = input("Ingrese el nombre del Jugador X: ")

# Función para mostrar el menú
def mostrar_menu():
    """
    Muestra las opciones del menú del juego.
    """
    print("¡Bienvenido al Triqui!")
    print("1. Jugar Triqui")
    print("2. Salir")

# Función principal del juego
def jugar_triqui():
    """
    Controla el flujo principal del juego, permitiendo que los jugadores realicen movimientos y determina el resultado.
    """
    global jugador_actual

    ingresar_nombres()

    while True:
        mostrar_menu()
        opcion = input("Selecciona una opción (1/2): ")

        if opcion == '1':
            reiniciar_juego()
            while True:
                imprimir_tablero()

                if jugador_actual == 'X':
                    movimiento = input(f"{jugadores[jugador_actual]}, elige la casilla (c1-c9): ")

                    if movimiento.startswith('c') and movimiento[1:].isdigit():
                        casilla = int(movimiento[1:]) - 1
                        fila, columna = divmod(casilla, 3)

                        if hacer_movimiento(fila, columna):
                            if verificar_ganador():
                                imprimir_tablero()
                                print(f"¡{jugadores[jugador_actual]} ha ganado!")
                                break
                            elif all(tablero[i][j] != ' ' for i in range(3) for j in range(3)):
                                imprimir_tablero()
                                print("¡Empate!")
                                break
                            else:
                                jugador_actual = 'O'
                        else:
                            continue
                    else:
                        print("Entrada inválida. Por favor, selecciona una casilla válida (c1-c9).")
                else:
                    # Turno de la máquina
                    if hacer_movimiento_maquina():
                        if verificar_ganador():
                            imprimir_tablero()
                            print(f"¡{jugadores[jugador_actual]} ha ganado!")
                            break
                        elif all(tablero[i][j] != ' ' for i in range(3) for j in range(3)):
                            imprimir_tablero()
                            print("¡Empate!")
                            break
                        else:
                            jugador_actual = 'X'
                    else:
                        print("¡Empate!")
                        break
        elif opcion == '2':
            print("¡Gracias por jugar! Hasta luego.")
            break
        else:
            print("Opción inválida. Por favor, selecciona 1 o 2.")

# Función para reiniciar el juego
def reiniciar_juego():
    """
    Reinicia el tablero y establece al jugador actual como 'X' al comenzar un nuevo juego.
    """
    global tablero
    tablero = [[' ', ' ', ' '],
               [' ', ' ', ' '],
               [' ', ' ', ' ']]
    global jugador_actual
    jugador_actual = 'X'

# Iniciar el juego
jugar_triqui()
