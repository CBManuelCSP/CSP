import unittest
from app.futbol_logic import listar_posiciones, calcular_total_jugadores

class TestFutbolLogic(unittest.TestCase):
    """
    Pruebas unitarias para las funciones de 'data_manager.py'.

    Métodos probados:
        - listar_posiciones: Filtra jugadores según su posición.
        - calcular_total_jugadores: Devuelve la lista formateada de jugadores
          y el total de jugadores.
    """
    def setUp(self):
        """Configura una plantilla de ejemplo para usar en las pruebas."""
        self.plantilla = [
            {"nombre": "Juan", "posicion": "Portero"},
            {"nombre": "Pedro", "posicion": "Defensa"},
            {"nombre": "Luis", "posicion": "Defensa"},
            {"nombre": "Carlos", "posicion": "Delantero"},
        ]

    def test_listar_posiciones_defensa(self):
        """Comprueba que listar_posiciones devuelve los jugadores de la posición 'Defensa' correctamente."""
        resultado = listar_posiciones(self.plantilla, "Defensa")
        self.assertEqual(resultado, ["Pedro", "Luis"])

    def test_listar_posiciones_sin_resultados(self):
        """Comprueba que listar_posiciones devuelve una lista vacía si no hay coincidencias."""
        resultado = listar_posiciones(self.plantilla, "Centrocampista")
        self.assertEqual(resultado, [])

    def test_calcular_total_jugadores(self):
        """Comprueba que calcular_total_jugadores devuelve el total correcto y la lista formateada de jugadores."""
        lista, total = calcular_total_jugadores(self.plantilla)
        self.assertEqual(total, 4)
        self.assertIn("Juan (POR)", lista)
        self.assertIn("Pedro (DEF)", lista)

if __name__ == "__main__":
    unittest.main()