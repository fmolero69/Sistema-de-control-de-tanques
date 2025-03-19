from repositories.valvula_repository import ValvulaRepository
from repositories.tanque_repository import TanqueRepository
from models.valvula import Valvula
from database import execute_query

class ValvulaService:
    @staticmethod
    def abrir_valvula(valvula_id):
        """
        Abre una válvula y transfiere líquido entre tanques.
        """
        valvula = ValvulaRepository.obtener_por_id(valvula_id)
        if not valvula:
            return "Válvula no encontrada"

        # Abrir la válvula
        ValvulaRepository.actualizar_estado(valvula_id, 'abierta')

        # Obtener la válvula opuesta
        valvula_opuesta = ValvulaRepository.obtener_por_tanques(valvula.tanque_destino_id, valvula.tanque_origen_id)
        if valvula_opuesta:
            ValvulaRepository.actualizar_estado(valvula_opuesta.id, 'abierta')

        # Simular el flujo entre tanques
        TanqueRepository.transferir_liquido(valvula.tanque_origen_id, valvula.tanque_destino_id, 10)

        return "Válvula abierta y flujo iniciado"

    @staticmethod
    def cerrar_valvula(valvula_id):
        """
        Cierra una válvula y detiene el flujo entre tanques.
        """
        valvula = ValvulaRepository.obtener_por_id(valvula_id)
        if not valvula:
            return "Válvula no encontrada"

        # Cerrar la válvula
        ValvulaRepository.actualizar_estado(valvula_id, 'cerrada')

        # Obtener la válvula opuesta
        valvula_opuesta = ValvulaRepository.obtener_por_tanques(valvula.tanque_destino_id, valvula.tanque_origen_id)
        if valvula_opuesta:
            ValvulaRepository.actualizar_estado(valvula_opuesta.id, 'cerrada')

        return "Válvula cerrada y flujo detenido"

    @staticmethod
    def obtener_estado_valvulas():
        """
        Obtiene el estado de todas las válvulas desde el repositorio.
        """
        try:
            # Obtener todas las válvulas desde el repositorio
            valvulas = ValvulaRepository.obtener_todas()
            return valvulas
        except Exception as e:
            print(f"Error al obtener el estado de las válvulas: {e}")
            raise

    @staticmethod
    def simular_transferencia(valvula_id):
        """
        Simula la transferencia de líquido entre tanques cuando una válvula está abierta.
        """
        valvula = ValvulaRepository.obtener_por_id(valvula_id)
        if valvula.estado == 'abierta':
            tanque_origen = TanqueRepository.obtener_por_id(valvula.tanque_origen_id)
            tanque_destino = TanqueRepository.obtener_por_id(valvula.tanque_destino_id)

            # Simular la transferencia de líquido
            cantidad_transferida = 10  # Por ejemplo, 10 unidades por segundo
            if tanque_origen.nivel_actual >= cantidad_transferida:
                tanque_origen.nivel_actual -= cantidad_transferida
                tanque_destino.nivel_actual += cantidad_transferida
                TanqueRepository.actualizar(tanque_origen)
                TanqueRepository.actualizar(tanque_destino)
