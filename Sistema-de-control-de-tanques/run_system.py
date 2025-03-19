import os
import subprocess
import threading
import webbrowser
import time

# Configuración de rutas
BACKEND_DIR = os.path.join(os.path.dirname(__file__), "backend")  # Ruta al backend
FRONTEND_DIR = os.path.join(os.path.dirname(__file__), "frontend", "public")  # Ruta al frontend

def run_backend():
    """Función para ejecutar el backend (Flask)."""
    try:
        print(f"Backend running at http://localhost:5000")
        # Cambiar al directorio del backend y ejecutar app.py
        os.chdir(BACKEND_DIR)
        subprocess.run(["python3", "app.py"])
    except Exception as e:
        print(f"Error al ejecutar el backend: {e}")

def run_frontend():
    """Función para ejecutar el frontend (servidor HTTP)."""
    try:
        print(f"Frontend running at http://localhost:5001")
        # Cambiar al directorio del frontend y ejecutar el servidor HTTP
        os.chdir(FRONTEND_DIR)
        subprocess.run(["python3", "-m", "http.server", "5001"])
    except Exception as e:
        print(f"Error al ejecutar el frontend: {e}")

def open_browser():
    """Función para abrir automáticamente el navegador web."""
    try:
        # Esperar un momento para asegurarse de que el servidor esté listo
        time.sleep(2)
        # Abrir el navegador con la URL del frontend
        webbrowser.open("http://localhost:5001")
    except Exception as e:
        print(f"Error al abrir el navegador: {e}")

if __name__ == "__main__":
    # Ejecutar el backend en un hilo separado
    backend_thread = threading.Thread(target=run_backend)
    backend_thread.daemon = True  # El hilo se detendrá cuando el programa principal termine
    backend_thread.start()

    # Ejecutar el frontend en un hilo separado
    frontend_thread = threading.Thread(target=run_frontend)
    frontend_thread.daemon = True
    frontend_thread.start()

    # Abrir el navegador automáticamente
    open_browser()

    # Mantener el script en ejecución
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print("Deteniendo el sistema...")
