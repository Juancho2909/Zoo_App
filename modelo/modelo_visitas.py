import mysql.connector  # Biblioteca para la conexión a MySQL

class ModeloVisitas:
    def __init__(self):
        # Configuración de la conexión a la base de datos
        self.db_config = {
            'host': 'localhost',
            'user': 'root',         # Cambia con tu usuario de MySQL
            'password': 'Roger5417*',   # Cambia con tu contraseña de MySQL
            'database': 'zoo'     # Cambia con el nombre de tu base de datos
        }

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
    
    def obtener_todos_los_visitas(self,correo,licencia):
        """Obtiene todos los animales relacionados con el id_supervisor."""
        try:
            conexion = mysql.connector.connect(**self.db_config)
            cursor = conexion.cursor()
            query = "SELECT * FROM visitas WHERE idzona = %s"
            cursor.execute(query, (self.obtener_idzonaempleado(correo,licencia)))
            resultado = cursor.fetchall()
            conexion.close()
            return resultado
        except mysql.connector.Error as err:
            print(f"Error al obtener animales: {err}")
            return None
