from database import execute_query
from models.valvula import Valvula

class ValvulaRepository:
    @staticmethod
    def obtener_todas():
        """
        Obtiene todas las válvulas de la base de datos.
        """
        query = "SELECT * FROM valvulas;"
        result = execute_query(query)
        return [Valvula(*row) for row in result]

    @staticmethod
    def obtener_por_id(valvula_id):
        """
        Obtiene una válvula por su ID.
        """
        query = "SELECT * FROM valvulas WHERE id = %s;"
        result = execute_query(query, (valvula_id,))
        if result:
            return Valvula(*result[0])
        return None

    @staticmethod
    def obtener_por_tanques(tanque_origen_id, tanque_destino_id):
        """
        Obtiene una válvula por los IDs de los tanques de origen y destino.
        """
        query = "SELECT * FROM valvulas WHERE tanque_origen_id = %s AND tanque_destino_id = %s;"
        result = execute_query(query, (tanque_origen_id, tanque_destino_id))
        if result:
            return Valvula(*result[0])
        return None

    @staticmethod
    def actualizar_estado(valvula_id, estado):
        """
        Actualiza el estado de una válvula.
        """
        query = "UPDATE valvulas SET estado = %s WHERE id = %s;"
        execute_query(query, (estado, valvula_id))
