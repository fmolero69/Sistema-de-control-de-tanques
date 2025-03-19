import unittest
from models.evento import Evento
from services.evento_service import EventoService

class TestEvento(unittest.TestCase):
    def test_creacion_evento(self):
        # Prueba la creación de un objeto Evento
        evento = Evento(
            id=1,
            tipo_evento="fallo",
            fecha_hora="2023-10-01 12:00:00",
            tanque_id=1,
            descripcion="Fallo en el sensor de temperatura",
            duracion="00:30:00"
        )
        self.assertEqual(evento.tipo_evento, "fallo")
        self.assertEqual(evento.tanque_id, 1)
        self.assertEqual(evento.descripcion, "Fallo en el sensor de temperatura")

    def test_reporte_fallos(self):
        # Prueba la función de reporte_fallos en EventoService
        fallos = EventoService.reporte_fallos()
        self.assertIsInstance(fallos, list)  # Verifica que se obtenga una lista de fallos

        # Verifica que todos los eventos en el reporte sean de tipo "fallo"
        for fallo in fallos:
            self.assertEqual(fallo.tipo_evento, "fallo")

if __name__ == '__main__':
    unittest.main()
