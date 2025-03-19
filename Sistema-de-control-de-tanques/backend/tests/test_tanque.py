import unittest
from models.tanque import Tanque
from services.tanque_service import TanqueService

class TestTanque(unittest.TestCase):
    def test_creacion_tanque(self):
        # Prueba la creación de un objeto Tanque
        tanque = Tanque(id=1, nivel_actual=100, capacidad=80000, tipo_pintura="Pintura Base Agua")
        self.assertEqual(tanque.nivel_actual, 100)
        self.assertEqual(tanque.capacidad, 80000)
        self.assertEqual(tanque.tipo_pintura, "Pintura Base Agua")

    def test_simular_llenado(self):
        # Prueba la función de simular_llenado en TanqueService
        mensaje = TanqueService.simular_llenado()
        self.assertEqual(mensaje, "Llenado simulado correctamente")

        # Verifica que los niveles de los tanques se hayan actualizado correctamente
        tanques = TanqueService.obtener_niveles_tanques()
        for tanque in tanques:
            self.assertEqual(tanque.nivel_actual, 100)

if __name__ == '__main__':
    unittest.main()
