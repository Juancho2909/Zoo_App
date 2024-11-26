import mysql.connector  # Biblioteca para la conexión a MySQL

class ModeloJaulas:
    def __init__(self):
        # Configuración de la conexión a la base de datos
        self.db_config = {
            'host': 'localhost',
            'user': 'root',         # Cambia con tu usuario de MySQL
            'password': 'Roger5417*',   # Cambia con tu contraseña de MySQL
            'database': 'zoo'     # Cambia con el nombre de tu base de datos
        }

    def obtener_idzona_empleado(self, correo, licencia):
        """
        Obtiene el ID de la zona asociada a un supervisor.
        """
        try:
            with mysql.connector.connect(**self.db_config) as conexion:
                cursor = conexion.cursor()
                query = "SELECT idzona FROM supervisores WHERE correo=%s AND licencia=%s"
                cursor.execute(query, (correo, licencia))
                resultado = cursor.fetchone()
                return resultado[0] if resultado else None
        except mysql.connector.Error as err:
            print(f"Error al obtener la zona del supervisor: {err}")
            return None

    def obtener_jaulas_por_zona(self, correo, licencia):
        """
        Obtiene todos los IDs de jaulas asociadas a los animales supervisados en una zona.
        """
        try:
            idzona = self.obtener_idzona_empleado(correo, licencia)
            if idzona is None:
                print("No se encontró una zona asociada al supervisor.")
                return None

            with mysql.connector.connect(**self.db_config) as conexion:
                cursor = conexion.cursor()
                query = "SELECT idjaula FROM animales WHERE idzona = %s"
                cursor.execute(query, (idzona,))
                resultado = cursor.fetchall()
                return [row[0] for row in resultado] if resultado else None
        except mysql.connector.Error as err:
            print(f"Error al obtener jaulas de la zona: {err}")
            return None

    def obtener_todas_las_jaulas(self, correo, licencia):
        """
        Obtiene todos los detalles de las jaulas asociadas a los animales de una zona.
        """
        try:
            idjaulas = self.obtener_jaulas_por_zona(correo, licencia)
            if not idjaulas:
                print("No se encontraron jaulas asociadas a los animales.")
                return None

            with mysql.connector.connect(**self.db_config) as conexion:
                cursor = conexion.cursor()
                # Consulta dinámica para obtener detalles de las jaulas
                query = "SELECT * FROM jaulas WHERE idjaula IN (%s)" % ','.join(['%s'] * len(idjaulas))
                cursor.execute(query, tuple(idjaulas))
                resultado = cursor.fetchall()
                return resultado if resultado else None
        except mysql.connector.Error as err:
            print(f"Error al obtener detalles de las jaulas: {err}")
            return None
