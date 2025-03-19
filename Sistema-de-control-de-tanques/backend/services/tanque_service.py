from repositories.tanque_repository import TanqueRepository
from models.tanque import Tanque

class TanqueService:
    @staticmethod
    def obtener_niveles_tanques():
        return TanqueRepository.obtener_todos()

    @staticmethod
    def simular_llenado():
        tanques = TanqueRepository.obtener_todos()
        for tanque in tanques:
            TanqueRepository.actualizar_nivel(tanque.id, 100)
        return "Llenado simulado correctamente"
