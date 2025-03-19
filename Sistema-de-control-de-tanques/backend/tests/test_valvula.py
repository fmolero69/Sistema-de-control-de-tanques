import unittest
from models.valvula import Valvula
from services.valvula_service import ValvulaService

class TestValvula(unittest.TestCase):
    def test_creacion_valvula(self):
        # Prueba la creación de un objeto Valvula
        valvula = Valvula(id=1, estado="cerrada", tanque_origen_id=1, tanque_destino_id=2)
        self.assertEqual(valvula.estado, "cerrada")
        self.assertEqual(valvula.tanque_origen_id, 1)
        self.assertEqual(valvula.tanque_destino_id, 2)

    def test_abrir_valvula(self):
        # Prueba la función de abrir_valvula en ValvulaService
        valvula_id = 1
        mensaje = ValvulaService.abrir_valvula(valvula_id)
        self.assertEqual(mensaje, "Válvula abierta correctamente")

        # Verifica que el estado de la válvula se haya actualizado correctamente
        valvulas = ValvulaService.obtener_estado_valvulas()
        valvula_abierta = next((v for v in valvulas if v.id == valvula_id), None)
        self.assertIsNotNone(valvula_abierta)
        self.assertEqual(valvula_abierta.estado, "abierta")

    def test_cerrar_valvula(self):
        # Prueba la función de cerrar_valvula en ValvulaService
        valvula_id = 1
        mensaje = ValvulaService.cerrar_valvula(valvula_id)
        self.assertEqual(mensaje, f"Válvula {valvula_id} cerrada correctamente")

        # Verifica que el estado de la válvula se haya actualizado correctamente
        valvulas = ValvulaService.obtener_estado_valvulas()
        valvula_cerrada = next((v for v in valvulas if v.id == valvula_id), None)
        self.assertIsNotNone(valvula_cerrada)
        self.assertEqual(valvula_cerrada.estado, "cerrada")

if __name__ == '__main__':
    unittest.main()
