POSICIONES = ["Portero", "Defensa", "Centrocampista", "Delantero"]

def mostrar_menu():
    """Muestra en consola el menú principal del gestor de plantillas."""
    print("\n--- GESTOR DE PLANTILLAS ---")
    print("1. Añadir nuevo jugador")
    print("2. Ver jugadores de una posición")
    print("3. Ver jugadores totales")
    print("4. Salir")

def pedir_posicion() -> int:
    """
    Pide la posición al usuario y la valida, de forma que de esa manera se puedan listar los jugadores de esa posición.
    
    La función muestra un menú con las posiciones disponibles y espera que el usuario
    introduzca un número entre 1 y 4. Si la entrada no es válida, se solicita nuevamente
    hasta que el usuario proporcione un valor correcto.

    Returns:
        int: Número correspondiente a la posición seleccionada según la lista `POSICIONES`.
    """
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
    """
    Pide los datos del nuevo jugador al usuario y los valida.
    
    La función pide al usuario:
        - El nombre del jugador.
        - La posición del jugador mediante un número del 1 al 4, correspondiente
          a la lista `POSICIONES`. Si la entrada no es válida, se solicita de nuevo
          hasta que el usuario introduzca un número correcto.

    Returns:
        dict: Diccionario con los datos del jugador, con las claves:
            - "nombre" (str): Nombre del jugador introducido.
            - "posicion" (str): Nombre de la posición seleccionada según POSICIONES.
    """
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