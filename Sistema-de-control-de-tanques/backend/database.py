# database.py
import psycopg2
from psycopg2 import pool
import sys
import os

# Añadir la ruta del proyecto al PYTHONPATH
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from config.config import DB_CONFIG  # Importar la configuración de la base de datos

# Crear un pool de conexiones para mejorar el rendimiento
connection_pool = pool.SimpleConnectionPool(
    minconn=1,  # Mínimo de conexiones en el pool
    maxconn=10,  # Máximo de conexiones en el pool
    **DB_CONFIG  # Credenciales de la base de datos
)

def get_db_connection():
    """
    Obtiene una conexión del pool de conexiones.

    Returns:
        conexion: Objeto de conexión a la base de datos.
    """
    try:
        return connection_pool.getconn()
    except Exception as e:
        print(f"Error al obtener conexión del pool: {e}")
        return None

def release_db_connection(conn):
    """
    Libera una conexión y la devuelve al pool.

    Args:
        conn: Objeto de conexión a la base de datos.
    """
    if conn:
        connection_pool.putconn(conn)

def execute_query(query, params=None):
    """
    Ejecuta una consulta SQL en la base de datos.

    Args:
        query (str): Consulta SQL a ejecutar.
        params (tuple, optional): Parámetros para la consulta SQL. Defaults to None.

    Returns:
        resultado: Resultado de la consulta (si es un SELECT) o None (si es un INSERT/UPDATE/DELETE).
    """
    conn = get_db_connection()
    if not conn:
        return None

    try:
        with conn.cursor() as cursor:  # Usar un context manager para el cursor
            cursor.execute(query, params)
            if query.strip().upper().startswith("SELECT"):  # Si es un SELECT, retornar los resultados
                return cursor.fetchall()
            conn.commit()  # Confirmar cambios si es un INSERT/UPDATE/DELETE
    except Exception as e:
        print(f"Error al ejecutar la consulta: {e}")
        conn.rollback()  # Revertir cambios en caso de error
    finally:
        release_db_connection(conn)  # Liberar la conexión al pool

# Consulta DB
from database import execute_query

# Consultar los niveles de los tanques
query = "SELECT * FROM tanques;"
resultados = execute_query(query)
print("Niveles de los tanques:", resultados)

# Consultar las temperaturas
query = "SELECT * FROM sensores WHERE tipo = 'temperatura';"
resultados = execute_query(query)
print("Temperaturas:", resultados)

# Consultar el estado de las válvulas
query = "SELECT * FROM valvulas;"
resultados = execute_query(query)
print("Estado de las válvulas:", resultados)

# Consultar los eventos
query = "SELECT * FROM eventos;"
resultados = execute_query(query)
print("Eventos:", resultados)
