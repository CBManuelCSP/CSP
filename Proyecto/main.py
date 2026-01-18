from app import data_manager, futbol_logic, ui          # Están en un subdirectorio app/

def main():
    """
    Función principal del gestor de plantillas de fútbol.

    Este programa realiza las siguientes acciones:
        1. Antes de comenzar el bucle, carga la plantilla de jugadores desde un archivo JSON usando data_manager.cargar_datos.
        2. Comienza el bucle mostrando un menú al usuario con las opciones disponibles:
            - Añadir un nuevo jugador.
            - Ver jugadores de una posición concreta.
            - Ver la lista completa de jugadores y el total.
            - Salir del programa.
        3. Procesa la opción seleccionada:
            - Para añadir un jugador, solicita los datos, los agrega a la plantilla y guarda el archivo.
            - Para ver jugadores por posición, solicita la posición y muestra los jugadores filtrados.
            - Para ver jugadores totales, muestra la lista formateada como "Nombre (POS)" y el total de jugadores.
            - Para salir, termina el bucle y cierra el programa.
        4. Valida entradas inválidas mostrando un mensaje de error.

    Returns:
        None: Esta función controla el flujo principal y no devuelve ningún valor.
    """
    # 1. Carga del estado inicial
    plantilla = data_manager.cargar_datos()

    while True:
        ui.mostrar_menu()
        opcion = input("Elige una opción: ")

        match opcion:
            case "1":
                # Registrar
                nuevo_jug = ui.pedir_datos_jugador()
                plantilla.append(nuevo_jug)
                data_manager.guardar_datos(plantilla)
            
            case "2":
                # Ver jugadores por posición
                posicion = ui.pedir_posicion()
                jugadores = futbol_logic.listar_posiciones(plantilla,posicion)
                
                print(f"\nTOTAL DE {posicion.upper()}S:")
                for j in jugadores:
                    print(j)
            
            case "3":
                # Ver jugadores totales
                total = futbol_logic.calcular_total_jugadores(plantilla)
                for j in total[0]:
                    print(j)

                print(f"Jugadores totales: {total[1]}")
            
            case "4":
                print("Cerrando el programa...")
                break
            
            case _:
                print("Opción no válida.")

if __name__ == "__main__":
    main()