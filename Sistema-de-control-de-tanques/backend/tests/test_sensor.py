import unittest
from models.sensor import Sensor
from services.sensor_service import SensorService

class TestSensor(unittest.TestCase):
    def test_creacion_sensor(self):
        # Prueba la creación de un objeto Sensor
        sensor = Sensor(id=1, tipo="temperatura", subtipo="TempF", valor=25.0, tanque_id=1)
        self.assertEqual(sensor.valor, 25.0)
        self.assertEqual(sensor.tipo, "temperatura")
        self.assertEqual(sensor.tanque_id, 1)

    def test_obtener_temperaturas(self):
        # Prueba la función de obtener_temperaturas en SensorService
        temperaturas = SensorService.obtener_temperaturas()
        self.assertGreater(len(temperaturas), 0)  # Verifica que se obtuvieron resultados
        for sensor in temperaturas:
            self.assertEqual(sensor.tipo, "temperatura")  # Verifica que todos los sensores sean de tipo temperatura

if __name__ == '__main__':
    unittest.main()
