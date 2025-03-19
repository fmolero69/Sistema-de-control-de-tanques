from repositories.sensor_repository import SensorRepository

class SensorService:
    @staticmethod
    def obtener_temperaturas():
        return SensorRepository.obtener_temperaturas()
