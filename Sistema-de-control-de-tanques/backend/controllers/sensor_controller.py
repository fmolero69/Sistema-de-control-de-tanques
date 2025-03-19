from flask import jsonify
from services.sensor_service import obtener_temperaturas as obtener_temperaturas_service

def obtener_temperaturas():
    """
    Obtiene las temperaturas actuales de los tanques.

    Returns:
        JSON: Temperaturas de los tanques o un mensaje de error.
    """
    try:
        temperaturas = obtener_temperaturas_service()
        if temperaturas:
            return jsonify({"temperaturas": temperaturas}), 200
        return jsonify({"error": "No se encontraron datos"}), 404
    except Exception as e:
        print(f"Error inesperado en /temperaturas: {e}")
        return jsonify({"error": "Error interno del servidor"}), 500
