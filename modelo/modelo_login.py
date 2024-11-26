import mysql.connector  # Biblioteca para la conexión a MySQL

class ModeloLogin:
    def __init__(self):
        # Configuración de la conexión a la base de datos
        self.db_config = {
            'host': 'localhost',
            'user': 'root',         # Cambia con tu usuario de MySQL
            'password': 'Roger5417*',   # Cambia con tu contraseña de MySQL
            'database': 'zoo'     # Cambia con el nombre de tu base de datos
        }

    
    def validar_usuario(self, correo, licencia):
        """Valida si el correo y la licencia existen en la base de datos."""
        try:
            conexion = mysql.connector.connect(**self.db_config)
            cursor = conexion.cursor()
            query = "SELECT * FROM supervisores WHERE correo = %s AND licencia = %s"
            cursor.execute(query, (correo, licencia))
            resultado = cursor.fetchone()
            conexion.close()

            if resultado:
                return True  # Usuario válido
            else:
                return False  # Usuario no encontrado
        except mysql.connector.Error as err:
            print(f"Error de conexión: {err}")
            return False

    def obtener_empleado(self, correo,licencia):
        """Consulta para obtener todos los animales de la base de datos."""
        try:
            conexion = mysql.connector.connect(**self.db_config)
            cursor = conexion.cursor()
            query = "SELECT * FROM supervisores WHERE correo=%s AND licencia = %s"
            cursor.execute(query,(correo,licencia))
            resultado = cursor.fetchall()
            conexion.close()
            return resultado  # Retorna todos los registros de la tabla animales
        except mysql.connector.Error as err:
            print(f"Error al obtener supervisor: {err}")
            return None


    def obtener_idzonaempleado(self, correo,licencia):
        """Consulta para obtener todos los animales de la base de datos."""
        try:
            conexion = mysql.connector.connect(**self.db_config)
            cursor = conexion.cursor()
            query = "SELECT idzona FROM supervisores WHERE correo=%s AND licencia = %s"
            cursor.execute(query,(correo,licencia))
            resultado = cursor.fetchall()
            zona = resultado[0]
            conexion.close()
            return zona  # Retorna todos los registros de la tabla animales
        except mysql.connector.Error as err:
            print(f"Error al obtener supervisor: {err}")
            return None