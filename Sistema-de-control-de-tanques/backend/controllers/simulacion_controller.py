from flask import jsonify
from services.simulacion_service import simular_llenado as simular_llenado_service

def simular_llenado():
    """
    Simula el llenado de todos los tanques al 100%.

    Returns:
        JSON: Mensaje de éxito o error.
    """
    try:
        mensaje = simular_llenado_service()
        return jsonify({"mensaje": mensaje}), 200
    except Exception as e:
        print(f"Error inesperado en /simular-llenado: {e}")
        return jsonify({"error": "Error interno del servidor"}), 500
