from flask import jsonify, request
from services.valvula_service import ValvulaService

def abrir_valvula():
    """
    Abre una válvula y transfiere líquido entre tanques.

    Returns:
        JSON: Mensaje de éxito o error.
    """
    data = request.json
    valvula_id = data.get('valvula_id')

    if not valvula_id:
        return jsonify({"error": "Datos incompletos"}), 400

    try:
        mensaje = ValvulaService.abrir_valvula(valvula_id)
        return jsonify({"mensaje": mensaje}), 200
    except Exception as e:
        print(f"Error inesperado en /abrir-valvula: {e}")
        return jsonify({"error": "Error interno del servidor"}), 500

def cerrar_valvula():
    """
    Cierra una válvula específica.

    Returns:
        JSON: Mensaje de éxito o error.
    """
    data = request.json
    valvula_id = data.get('valvula_id')

    if not valvula_id:
        return jsonify({"error": "Datos incompletos"}), 400

    try:
        mensaje = ValvulaService.cerrar_valvula(valvula_id)
        return jsonify({"mensaje": mensaje}), 200
    except Exception as e:
        print(f"Error inesperado en /cerrar-valvula: {e}")
        return jsonify({"error": "Error interno del servidor"}), 500

def simular_transferencia():
    """
    Simula la transferencia de líquido entre tanques cuando una válvula está abierta.

    Returns:
        JSON: Mensaje de éxito o error.
    """
    data = request.json
    valvula_id = data.get('valvula_id')

    if not valvula_id:
        return jsonify({"error": "Datos incompletos"}), 400

    try:
        ValvulaService.simular_transferencia(valvula_id)
        return jsonify({"mensaje": "Transferencia simulada correctamente"}), 200
    except Exception as e:
        print(f"Error inesperado en /simular-transferencia: {e}")
        return jsonify({"error": "Error interno del servidor"}), 500
