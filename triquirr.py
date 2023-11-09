# Importamos el módulo random para la elección aleatoria de movimientos por la máquina
import random

# Variables globales
tablero = [[' ', ' ', ' '],
           [' ', ' ', ' '],
           [' ', ' ', ' ']]  # Representa el tablero del Triqui
jugador_actual = 'X'  # Indica el jugador actual ('X' o 'O')
jugadores = {'X': '', 'O': 'Máquina'}  # Nombres de los jugadores ('X' humano, 'O' máquina)

# Función para imprimir el tablero de manera bonita
def imprimir_tablero():
    print("  c1 c2 c3")  # Etiquetas de columnas
    for i, fila in enumerate(tablero):
        print(f"r{i + 1}|", end="")  # Etiquetas de filas
        for casilla in fila:
            print(casilla + "|", end="")  # Imprime el contenido de cada casilla
        print("\n-----------")

# Función para verificar si hay un ganador
def verificar_ganador():
    # Verificar filas y columnas
    for i in range(3):
        # Verifica si todas las casillas en la fila o columna son del jugador_actual
        if all(tablero[i][j] == jugador_actual for j in range(3)) or all(tablero[j][i] == jugador_actual for j in range(3)):
            return True

    # Verificar diagonales
    if all(tablero[i][i] == jugador_actual for i in range(3)) or all(tablero[i][2 - i] == jugador_actual for i in range(3)):
        return True

    return False

# Función para realizar un movimiento del jugador
def hacer_movimiento(fila, columna):
    global jugador_actual

    if tablero[fila][columna] == ' ':
        tablero[fila][columna] = jugador_actual  # Coloca el símbolo del jugador en la casilla seleccionada
        return True  # Indica que el movimiento fue exitoso
    else:
        print("Casilla ocupada. Intenta de nuevo.")
        return False  # Indica que la casilla ya estaba ocupada

# Función para realizar un movimiento de la máquina
def hacer_movimiento_maquina():
    global jugador_actual

    casillas_disponibles = [(i, j) for i in range(3) for j in range(3) if tablero[i][j] == ' ']
    if casillas_disponibles:
        fila, columna = random.choice(casillas_disponibles)  # Elige aleatoriamente una casilla disponible
        tablero[fila][columna] = jugador_actual  # Coloca el símbolo del jugador en la casilla seleccionada por la máquina
        return True  # Indica que el movimiento fue exitoso
    else:
        return False  # Indica que no hay casillas disponibles (empate)

# Función para ingresar nombres de jugadores
def ingresar_nombres():
    global jugadores
    jugadores['X'] = input("Ingrese el nombre del Jugador X: ")

# Función para mostrar el menú
def mostrar_menu():
    print("¡Bienvenido al Triqui!")
    print("1. Jugar Triqui")
    print("2. Salir")

# Función principal del juego
def jugar_triqui():
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
    global tablero
    tablero = [[' ', ' ', ' '],
               [' ', ' ', ' '],
               [' ', ' ', ' ']]
    global jugador_actual
    jugador_actual = 'X'

# Iniciar el juego
jugar_triqui()

