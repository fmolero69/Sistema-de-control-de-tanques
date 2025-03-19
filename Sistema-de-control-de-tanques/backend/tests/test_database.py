import unittest
from database import execute_query

class TestDatabase(unittest.TestCase):
    def test_conexion_base_de_datos(self):
        # Prueba que la conexión a la base de datos funcione correctamente
        query = "SELECT 1"
        resultado = execute_query(query)
        self.assertEqual(resultado, [(1,)])

    def test_consulta_tanques(self):
        # Prueba una consulta básica a la tabla de tanques
        query = "SELECT id, nivel_actual, capacidad, tipo_pintura FROM tanques ORDER BY id;"
        resultados = execute_query(query)
        self.assertIsInstance(resultados, list)  # Verifica que se obtenga una lista de resultados

        # Verifica que los tanques tengan los campos esperados
        for tanque in resultados:
            self.assertIsInstance(tanque[0], int)  # id
            self.assertIsInstance(tanque[1], int)  # nivel_actual
            self.assertIsInstance(tanque[2], int)  # capacidad
            self.assertIsInstance(tanque[3], str)  # tipo_pintura

    def test_consulta_sensores(self):
        # Prueba una consulta básica a la tabla de sensores
        query = "SELECT id, tipo, subtipo, valor, tanque_id FROM sensores ORDER BY id;"
        resultados = execute_query(query)
        self.assertIsInstance(resultados, list)  # Verifica que se obtenga una lista de resultados

        # Verifica que los sensores tengan los campos esperados
        for sensor in resultados:
            self.assertIsInstance(sensor[0], int)  # id
            self.assertIsInstance(sensor[1], str)  # tipo
            self.assertIsInstance(sensor[3], float)  # valor
            self.assertIsInstance(sensor[4], int)  # tanque_id

if __name__ == '__main__':
    unittest.main()
