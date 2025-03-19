class Valvula:
    def __init__(self, id, estado, tanque_origen_id, tanque_destino_id, velocidad_flujo=None):
        self.id = id
        self.estado = estado
        self.tanque_origen_id = tanque_origen_id
        self.tanque_destino_id = tanque_destino_id
        self.velocidad_flujo = velocidad_flujo
