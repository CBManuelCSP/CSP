import unittest
from unittest.mock import patch, mock_open
from app import data_manager

class TestDataManager(unittest.TestCase):
    """
    Pruebas unitarias para las funciones cargar_datos y guardar_datos de data_manager.py.

    Se utilizan mocks para simular el comportamiento del sistema de archivos, de modo
    que no se dependan archivos reales en disco durante las pruebas.

    Métodos probados:
        - cargar_datos: Comprueba el comportamiento cuando el archivo no existe
          y cuando contiene datos válidos.
        - guardar_datos: Comprueba que se llama correctamente al método de escritura
          del archivo.
    """

    @patch("app.data_manager.Path.exists", return_value=False)
    def test_cargar_datos_archivo_no_existe(self, mock_exists):
        """Comprueba que cargar_datos devuelve una lista vacía si el archivo no existe."""
        mock_exists.return_value = False
        resultado = data_manager.cargar_datos()
        self.assertEqual(resultado, [])

    @patch("app.data_manager.Path.exists", return_value=True)
    @patch("app.data_manager.Path.open", new_callable=mock_open,
           read_data='[{"nombre": "Juan", "posicion": "Portero"}]')
    def test_cargar_datos_correcto(self, mock_file, mock_exists):
        """Comprueba que cargar_datos devuelve correctamente los datos del archivo JSON."""
        resultado = data_manager.cargar_datos()
        self.assertEqual(len(resultado), 1)
        self.assertEqual(resultado[0]["nombre"], "Juan")

    @patch("app.data_manager.Path.open", new_callable=mock_open)
    def test_guardar_datos(self, mock_file):
        """Comprueba que guardar_datos llama correctamente al método de escritura del archivo."""
        datos = [{"nombre": "Pedro", "posicion": "Defensa"}]
        data_manager.guardar_datos(datos)
        mock_file.assert_called_once()
