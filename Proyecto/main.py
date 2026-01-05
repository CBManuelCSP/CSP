from app import data_manager, futbol_logic, ui          # Están en un subdirectorio app/

def main():
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