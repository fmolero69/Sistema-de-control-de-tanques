from flask import jsonify
from services.evento_service import reporte_fallos as reporte_fallos_service

def reporte_fallos():
    """
    Genera un reporte de fallos (eventos de tipo "fallo").

    Returns:
        JSON: Lista de fallos o un mensaje de error.
    """
    try:
        fallos = reporte_fallos_service()
        if fallos:
            return jsonify({"fallos": fallos}), 200
        return jsonify({"error": "No se encontraron fallos"}), 404
    except Exception as e:
        print(f"Error inesperado en /reporte-fallos: {e}")
        return jsonify({"error": "Error interno del servidor"}), 500
