# database_queries.py
from database import execute_query

def obtener_niveles_tanques():
    """
    Obtiene los niveles actuales de los tanques.

    Returns:
        list: Lista de niveles de los tanques.
    """
    query = "SELECT nivel_actual FROM tanques ORDER BY id;"
    return execute_query(query)

def obtener_temperaturas():
    """
    Obtiene las temperaturas actuales de los tanques.

    Returns:
        list: Lista de temperaturas de los tanques.
    """
    query = "SELECT valor FROM sensores WHERE tipo = 'temperatura' ORDER BY tanque_id;"
    return execute_query(query)

def abrir_valvula(valvula_id):
    """
    Abre una válvula y transfiere líquido entre tanques.

    Args:
        valvula_id (int): ID de la válvula a abrir.

    Returns:
        str: Mensaje de éxito.
    """
    # Abrir la válvula
    query_valvula = "UPDATE valvulas SET estado = 'abierta' WHERE id = %s;"
    execute_query(query_valvula, (valvula_id,))

    # Transferir líquido entre tanques
    cantidad_transferencia = 10  # Cantidad fija de líquido a transferir
    if valvula_id == 1:
        query1 = "UPDATE tanques SET nivel_actual = nivel_actual - %s WHERE id = 1;"
        query2 = "UPDATE tanques SET nivel_actual = nivel_actual + %s WHERE id = 2;"
    elif valvula_id == 2:
        query1 = "UPDATE tanques SET nivel_actual = nivel_actual - %s WHERE id = 2;"
        query2 = "UPDATE tanques SET nivel_actual = nivel_actual + %s WHERE id = 1;"
    else:
        raise ValueError("Válvula no válida")

    execute_query(query1, (cantidad_transferencia,))
    execute_query(query2, (cantidad_transferencia,))

    return "Válvula abierta y líquido transferido correctamente"

def cerrar_valvula(valvula_id):
    """
    Cierra una válvula específica.

    Args:
        valvula_id (int): ID de la válvula a cerrar.

    Returns:
        str: Mensaje de éxito.
    """
    query = "UPDATE valvulas SET estado = 'cerrada' WHERE id = %s;"
    execute_query(query, (valvula_id,))
    return f"Válvula {valvula_id} cerrada correctamente"

def obtener_estado_valvulas():
    """
    Obtiene el estado actual de las válvulas.

    Returns:
        list: Lista de estados de las válvulas.
    """
    query = "SELECT id, estado FROM valvulas ORDER BY id;"
    return execute_query(query)

def reporte_fallos():
    """
    Genera un reporte de fallos (eventos de tipo "fallo").

    Returns:
        list: Lista de fallos.
    """
    query = "SELECT * FROM eventos WHERE tipo_evento = 'fallo';"
    return execute_query(query)

def simular_llenado():
    """
    Simula el llenado de todos los tanques al 100%.

    Returns:
        str: Mensaje de éxito.
    """
    query = "UPDATE tanques SET nivel_actual = 100;"
    execute_query(query)
    return "Llenado simulado correctamente"
