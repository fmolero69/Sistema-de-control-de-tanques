from flask import Flask, jsonify, request
from flask_cors import CORS
from services.tanque_service import TanqueService
from services.sensor_service import SensorService
from services.valvula_service import ValvulaService
from services.evento_service import EventoService
from database import execute_query

app = Flask(__name__)
CORS(app)  # Permitir solicitudes desde el frontend

def reiniciar_base_de_datos():
    """
    Función para reiniciar la base de datos a un estado inicial.
    """
    try:
        # Limpiar la tabla de tanques
        execute_query("DELETE FROM tanques;")
        execute_query("ALTER SEQUENCE tanques_id_seq RESTART WITH 1;")

        # Insertar datos iniciales en la tabla de tanques
        execute_query("""
            INSERT INTO tanques (nivel_actual, capacidad, tipo_pintura)
            VALUES (100, 80000, 'Pintura Base Agua'),
                   (0, 80000, 'Pintura Base Aceite'),
                   (100, 80000, 'Pintura Base Aceite'),
                   (0, 80000, 'Pintura Base Agua');
        """)

        # Limpiar la tabla de sensores
        execute_query("DELETE FROM sensores;")
        execute_query("ALTER SEQUENCE sensores_id_seq RESTART WITH 1;")

        # Insertar datos iniciales en la tabla de sensores
        execute_query("""
            INSERT INTO sensores (tipo, subtipo, valor, tanque_id)
            VALUES ('temperatura', 'TempF', 25.0, 1),
                   ('temperatura', 'TempH', 22.0, 1),
                   ('temperatura', 'TempT', 23.0, 1),
                   ('nivel', NULL, 100, 1),
                   ('nivel', NULL, 0, 2),
                   ('nivel', NULL, 100, 3),
                   ('nivel', NULL, 0, 4);
        """)

        # Limpiar la tabla de válvulas
        execute_query("DELETE FROM valvulas;")
        execute_query("ALTER SEQUENCE valvulas_id_seq RESTART WITH 1;")

        # Insertar datos iniciales en la tabla de válvulas
        execute_query("""
            INSERT INTO valvulas (estado, tanque_origen_id, tanque_destino_id)
            VALUES ('cerrada', 1, 2),
                   ('cerrada', 2, 1),
                   ('cerrada', 3, 4),
                   ('cerrada', 4, 3);
        """)

        # Limpiar la tabla de eventos
        execute_query("DELETE FROM eventos;")
        execute_query("ALTER SEQUENCE eventos_id_seq RESTART WITH 1;")

        print("Base de datos reiniciada correctamente.")
    except Exception as e:
        print(f"Error al reiniciar la base de datos: {e}")

@app.route('/niveles', methods=['GET'])
def obtener_niveles():
    try:
        niveles = TanqueService.obtener_niveles_tanques()
        return jsonify({"niveles": [tanque.__dict__ for tanque in niveles]}), 200
    except Exception as e:
        print(f"Error inesperado en /niveles: {e}")
        return jsonify({"error": "Error interno del servidor"}), 500

@app.route('/temperaturas', methods=['GET'])
def obtener_temperaturas_route():
    try:
        temperaturas = SensorService.obtener_temperaturas()
        return jsonify({"temperaturas": [sensor.__dict__ for sensor in temperaturas]}), 200
    except Exception as e:
        print(f"Error inesperado en /temperaturas: {e}")
        return jsonify({"error": "Error interno del servidor"}), 500

@app.route('/abrir-valvula', methods=['POST'])
def abrir_valvula_route():
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

@app.route('/cerrar-valvula', methods=['POST'])
def cerrar_valvula_route():
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

@app.route('/estado-valvulas', methods=['GET'])
def obtener_estado_valvulas_route():
    try:
        valvulas = ValvulaService.obtener_estado_valvulas()
        return jsonify({"valvulas": [valvula.__dict__ for valvula in valvulas]}), 200
    except Exception as e:
        print(f"Error inesperado en /estado-valvulas: {e}")
        return jsonify({"error": "Error interno del servidor"}), 500

@app.route('/reporte-fallos', methods=['GET'])
def reporte_fallos_route():
    try:
        fallos = EventoService.reporte_fallos()
        return jsonify({"fallos": [fallo.__dict__ for fallo in fallos]}), 200
    except Exception as e:
        print(f"Error inesperado en /reporte-fallos: {e}")
        return jsonify({"error": "Error interno del servidor"}), 500

@app.route('/simular-llenado', methods=['POST'])
def simular_llenado_route():
    try:
        mensaje = TanqueService.simular_llenado()
        return jsonify({"mensaje": mensaje}), 200
    except Exception as e:
        print(f"Error inesperado en /simular-llenado: {e}")
        return jsonify({"error": "Error interno del servidor"}), 500

if __name__ == '__main__':
    # Reiniciar la base de datos al iniciar el sistema
    reiniciar_base_de_datos()

    # Iniciar el servidor Flask
    app.run(host='0.0.0.0', port=5000, debug=True)
