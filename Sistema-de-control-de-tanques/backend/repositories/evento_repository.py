from database import execute_query
from models.evento import Evento

class EventoRepository:
    @staticmethod
    def obtener_fallos():
        query = "SELECT id, tipo_evento, fecha_hora, tanque_id, descripcion, duracion FROM eventos WHERE tipo_evento = 'fallo';"
        resultados = execute_query(query)
        return [Evento(*fila) for fila in resultados]
