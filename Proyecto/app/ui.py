POSICIONES = ["Portero", "Defensa", "Centrocampista", "Delantero"]

def mostrar_menu():
    print("\n--- GESTOR DE PLANTILLAS ---")
    print("1. Añadir nuevo jugador")
    print("2. Ver jugadores de una posición")
    print("3. Ver jugadores totales")
    print("4. Salir")

def pedir_posicion() -> int:
    """Pide la posición al usuario y la valida, de forma que de esa manera se puedan listar los jugadores de esa posición."""
    while True:
        try:
            posicion = int(input("1. Portero\n2. Defensa\n3. Centrocampista\n4. Delantero\nIntroduce el número de la posición que quieres ver: "))
            if posicion > 0 and posicion < 5:
                break
            print("El número debe ser entre 1 y 4.")
        except ValueError:
            print("Por favor, introduce un número.")
    return POSICIONES[posicion - 1]

def pedir_datos_jugador() -> dict:
    """Pide los datos del nuevo jugador al usuario y los valida."""
    nombre = input("Introduce el nombre del jugador: ")
    while True:
        try:
            posicion = int(input(f"1. Portero\n2. Defensa\n3. Centrocampista\n4. Delantero\nIntroduce el número de la posición del jugador: "))
            if posicion > 0 and posicion < 5:
                break
            print("El número debe ser entre 1 y 4.")
        except ValueError:
            print("Por favor, introduce un número.")
            
    return {"nombre": nombre, "posicion": POSICIONES[posicion - 1]}