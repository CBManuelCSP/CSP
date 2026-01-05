import unittest
from unittest.mock import patch, mock_open
from app import data_manager

class TestDataManager(unittest.TestCase):

    @patch("app.data_manager.Path.exists", return_value=False)
    def test_cargar_datos_archivo_no_existe(self, mock_exists):
        mock_exists.return_value = False
        resultado = data_manager.cargar_datos()
        self.assertEqual(resultado, [])

    @patch("app.data_manager.Path.exists", return_value=True)
    @patch("app.data_manager.Path.open", new_callable=mock_open,
           read_data='[{"nombre": "Juan", "posicion": "Portero"}]')
    def test_cargar_datos_correcto(self, mock_file, mock_exists):
        resultado = data_manager.cargar_datos()
        self.assertEqual(len(resultado), 1)
        self.assertEqual(resultado[0]["nombre"], "Juan")

    @patch("app.data_manager.Path.open", new_callable=mock_open)
    def test_guardar_datos(self, mock_file):
        datos = [{"nombre": "Pedro", "posicion": "Defensa"}]
        data_manager.guardar_datos(datos)
        mock_file.assert_called_once()
