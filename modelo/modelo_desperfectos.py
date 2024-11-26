import mysql.connector  # Biblioteca para la conexión a MySQL

class ModeloDesperfectos:
    def __init__(self):
        # Configuración de la conexión a la base de datos
        self.db_config = {
            'host': 'localhost',
            'user': 'root',         # Cambia con tu usuario de MySQL
            'password': 'Roger5417*',   # Cambia con tu contraseña de MySQL
            'database': 'zoo'     # Cambia con el nombre de tu base de datos
        }

    def obtener_idzonaempleado(self, correo, licencia):
        """Consulta para obtener la idzona del supervisor."""
        try:
            conexion = mysql.connector.connect(**self.db_config)
            cursor = conexion.cursor()
            query = "SELECT idzona FROM supervisores WHERE correo=%s AND licencia=%s"
            cursor.execute(query, (correo, licencia))
            resultado = cursor.fetchone()  # Cambiar a fetchone() para obtener un único resultado
            conexion.close()
            return resultado[0] if resultado else None  # Retorna None si no hay datos
        except mysql.connector.Error as err:
            print(f"Error al obtener supervisor: {err}")
            return None

    def animales_jaulas(self, correo, licencia):
        """Obtiene todas las jaulas relacionadas con el id_supervisor."""
        try:
            idzona = self.obtener_idzonaempleado(correo, licencia)
            if idzona is None:
                print("No se encontró idzona para el supervisor.")
                return None

            conexion = mysql.connector.connect(**self.db_config)
            cursor = conexion.cursor()
            query = "SELECT idjaula FROM animales WHERE idzona = %s"
            cursor.execute(query, (idzona,))
            resultado = cursor.fetchall()
            conexion.close()

            # Devuelve una lista con todos los idjaula
            return [row[0] for row in resultado] if resultado else None
        except mysql.connector.Error as err:
            print(f"Error al obtener animales: {err}")
            return None

    def obtener_todos_los_desperfectos(self, correo, licencia):
        """Obtiene todos los desperfectos relacionados con las jaulas."""
        try:
            idjaulas = self.animales_jaulas(correo, licencia)
            if not idjaulas:
                print("No se encontraron jaulas para los animales.")
                return None

            conexion = mysql.connector.connect(**self.db_config)
            cursor = conexion.cursor()

            # Construir consulta dinámica para múltiples idjaula
            query = "SELECT * FROM desperfectos WHERE idjaula IN (%s)" % ','.join(['%s'] * len(idjaulas))
            cursor.execute(query, tuple(idjaulas))
            resultado = cursor.fetchall()
            conexion.close()

            return resultado if resultado else None  # Retorna los resultados o None si está vacío
        except mysql.connector.Error as err:
            print(f"Error al obtener desperfectos: {err}")
            return None
