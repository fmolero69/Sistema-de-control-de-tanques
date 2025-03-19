from database import execute_query
from models.sensor import Sensor

class SensorRepository:
    @staticmethod
    def obtener_por_tanque(tanque_id):
        query = "SELECT id, tipo, subtipo, valor, tanque_id FROM sensores WHERE tanque_id = %s ORDER BY id;"
        resultados = execute_query(query, (tanque_id,))
        return [Sensor(*fila) for fila in resultados]

    @staticmethod
    def obtener_temperaturas():
        query = "SELECT id, tipo, subtipo, valor, tanque_id FROM sensores WHERE tipo = 'temperatura' ORDER BY tanque_id;"
        resultados = execute_query(query)
        return [Sensor(*fila) for fila in resultados]
