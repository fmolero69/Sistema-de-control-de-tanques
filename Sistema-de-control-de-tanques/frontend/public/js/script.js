from database import execute_query
from models.tanque import Tanque

class TanqueRepository:
    @staticmethod
    def obtener_todos():
        """
        Obtiene todos los tanques desde la base de datos.

        Returns:
            List[Tanque]: Lista de objetos Tanque.
        """
        query = "SELECT * FROM tanques;"
        result = execute_query(query)
        return [Tanque(*row) for row in result]

    @staticmethod
    def obtener_por_id(tanque_id):
        """
        Obtiene un tanque por su ID desde la base de datos.

        Args:
            tanque_id (int): ID del tanque.

        Returns:
            Tanque: Objeto Tanque si se encuentra, None en caso contrario.
        """
        query = "SELECT * FROM tanques WHERE id = %s;"
        result = execute_query(query, (tanque_id,))
        if result:
            return Tanque(*result[0])
        return None

    @staticmethod
    def actualizar(tanque):
        """
        Actualiza un tanque en la base de datos.

        Args:
            tanque (Tanque): Objeto Tanque con los datos actualizados.
        """
        query = """
            UPDATE tanques
            SET nivel_actual = %s, capacidad = %s, tipo_pintura = %s
            WHERE id = %s;
        """
        execute_query(query, (tanque.nivel_actual, tanque.capacidad, tanque.tipo_pintura, tanque.id))

    @staticmethod
    def transferir_liquido(tanque_origen_id, tanque_destino_id, cantidad):
        """
        Transfiere líquido entre dos tanques.

        Args:
            tanque_origen_id (int): ID del tanque de origen.
            tanque_destino_id (int): ID del tanque de destino.
            cantidad (int): Cantidad de líquido a transferir.
        """
        # Verificar que los tanques existen
        tanque_origen = TanqueRepository.obtener_por_id(tanque_origen_id)
        tanque_destino = TanqueRepository.obtener_por_id(tanque_destino_id)

        if not tanque_origen or not tanque_destino:
            raise ValueError("Uno de los tanques no existe")

        # Verificar que el tanque de origen tiene suficiente líquido
        if tanque_origen.nivel_actual < cantidad:
            raise ValueError("El tanque de origen no tiene suficiente líquido")

        # Actualizar los niveles de los tanques
        tanque_origen.nivel_actual -= cantidad
        tanque_destino.nivel_actual += cantidad

        # Guardar los cambios en la base de datos
        TanqueRepository.actualizar(tanque_origen)
        TanqueRepository.actualizar(tanque_destino)
