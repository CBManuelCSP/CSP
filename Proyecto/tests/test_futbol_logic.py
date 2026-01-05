import unittest
from app.futbol_logic import listar_posiciones, calcular_total_jugadores

class TestFutbolLogic(unittest.TestCase):
    """Probamos todas las funciones del data_manager.py"""
    def setUp(self):
        self.plantilla = [
            {"nombre": "Juan", "posicion": "Portero"},
            {"nombre": "Pedro", "posicion": "Defensa"},
            {"nombre": "Luis", "posicion": "Defensa"},
            {"nombre": "Carlos", "posicion": "Delantero"},
        ]

    def test_listar_posiciones_defensa(self):
        resultado = listar_posiciones(self.plantilla, "Defensa")
        self.assertEqual(resultado, ["Pedro", "Luis"])

    def test_listar_posiciones_sin_resultados(self):
        resultado = listar_posiciones(self.plantilla, "Centrocampista")
        self.assertEqual(resultado, [])

    def test_calcular_total_jugadores(self):
        lista, total = calcular_total_jugadores(self.plantilla)
        self.assertEqual(total, 4)
        self.assertIn("Juan (POR)", lista)
        self.assertIn("Pedro (DEF)", lista)

if __name__ == "__main__":
    unittest.main()