def listar_posiciones(plantilla: list, posicion: int) -> dict:
    """
    Recibe la lista de jugadores.
    Devuelve una lista con la posición pedida
    Ej: [{'nombre': 'Juan', 'posicion': "Portero"}, ...] -> {"Juan", ...}
    """
    totales = []

    for j in plantilla:
        if j["posicion"] == posicion:
            totales.append(j["nombre"])
        
    return totales

def calcular_total_jugadores(jugadores: list) -> tuple[list[str],int]:
    """Comprueba el total de los jugadores que hay en plantilla."""
    lista_jugadores = [f"{j['nombre']} ({j['posicion'][:3].upper()})" for j in jugadores]

    return lista_jugadores,len(jugadores)