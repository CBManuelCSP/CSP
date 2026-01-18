def listar_posiciones(plantilla: list, posicion: int) -> dict:
    """
    Recibe la lista de jugadores.
    Devuelve una lista con los jugadores de la posición pedida
    Ej: [{'nombre': 'Juan', 'posicion': "Portero"}, ...] -> {"Juan", ...}
    
    Args:
        plantilla (list): Lista de jugadores. Cada jugador es un diccionario con "nombre" y "posicion'.
        posicion (int): Posición de la que se quiera ver los jugadores.

    Returns:
        totales (list): lista con los nombres de los jugadores que ocupan la posición indicada.
        En caso de no haber jugadores en la posición indicada, devuelve una lista vacía.
    """
    totales = []

    for j in plantilla:
        if j["posicion"] == posicion:
            totales.append(j["nombre"])
        
    return totales

def calcular_total_jugadores(jugadores: list) -> tuple[list[str],int]:
    """
    Comprueba el total de los jugadores que hay en plantilla.
    
    Args:
        jugadores (list): Lista de jugadores. Cada jugador es un diccionario con "nombre" y "posicion'.

    Returns:
        tuple[list[str],int]: Devuelve una tupla con la lista de jugadores (formateado como "Nombre (POS)") y el total de jugadores
    """
    lista_jugadores = [f"{j['nombre']} ({j['posicion'][:3].upper()})" for j in jugadores]

    return lista_jugadores,len(jugadores)