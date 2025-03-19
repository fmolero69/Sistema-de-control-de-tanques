# controllers/tanque_controller.py
from flask import jsonify
from services.tanque_service import obtener_niveles as obtener_niveles_service

def obtener_niveles():
    """
    Obtiene los niveles actuales de los tanques.

    Returns:
        JSON: Niveles de los tanques o un mensaje de error.
    """
    try:
        niveles = obtener_niveles_service()
        if niveles:
            return jsonify({"niveles": niveles}), 200
        return jsonify({"error": "No se encontraron datos"}), 404
    except Exception as e:
        print(f"Error inesperado en /niveles: {e}")
        return jsonify({"error": "Error interno del servidor"}), 500
