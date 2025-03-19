from repositories.evento_repository import EventoRepository

class EventoService:
    @staticmethod
    def reporte_fallos():
        return EventoRepository.obtener_fallos()
