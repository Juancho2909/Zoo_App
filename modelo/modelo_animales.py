import mysql.connector  # Biblioteca para la conexión a MySQL


class ModeloAnimales:
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
    
    def obtener_todos_los_animales(self,correo,licencia):
        """Obtiene todos los animales relacionados con el id_supervisor."""
        try:
            conexion = mysql.connector.connect(**self.db_config)
            cursor = conexion.cursor()
            query = "SELECT * FROM animales WHERE idzona = %s"
            cursor.execute(query, (self.obtener_idzonaempleado(correo,licencia)))
            resultado = cursor.fetchall()
            conexion.close()
            return resultado
        except mysql.connector.Error as err:
            print(f"Error al obtener animales: {err}")
            return None
        
    def obtener_todos_los_animales_restriccion_zona(self,correo,licencia):
        """Obtiene todos los animales relacionados con el id_supervisor."""
        try:
            conexion = mysql.connector.connect(**self.db_config)
            cursor = conexion.cursor()
            query = "SELECT tipo,nombre,sexo,fechaingreso FROM animales WHERE idzona = %s"
            cursor.execute(query, (self.obtener_idzonaempleado(correo,licencia)))
            resultado = cursor.fetchall()
            conexion.close()
            return resultado
        except mysql.connector.Error as err:
            print(f"Error al obtener animales: {err}")
            return None        
        
    def obtener_todos_los_animales_restriccion_especifico(self,correo,licencia,id_animal):
        """Obtiene todos los animales relacionados con el id_supervisor."""
        try:
            conexion = mysql.connector.connect(**self.db_config)
            cursor = conexion.cursor()
            query = "SELECT tipo,nombre,sexo,fechaingreso FROM animales WHERE idzona = %s and idanimal =%s"
            zona_empleado = self.obtener_idzonaempleado(correo, licencia)
            cursor.execute(query,(zona_empleado[0],id_animal))
            resultado = cursor.fetchall()
            conexion.close()
            return resultado
        except mysql.connector.Error as err:
            print(f"Error al obtener animales: {err}")
            return None                
        
    def obtener_todos_los_animales_idanimal(self,correo,licencia):
        """Obtiene todos los animales relacionados con el id_supervisor."""
        try:
            conexion = mysql.connector.connect(**self.db_config)
            cursor = conexion.cursor()
            query = "SELECT idanimal FROM animales WHERE idzona = %s"
            cursor.execute(query, ((self.obtener_idzonaempleado(correo,licencia))))
            resultado = cursor.fetchall()
            conexion.close()
            idanimal = resultado
            return idanimal
        except mysql.connector.Error as err:
            print(f"Error al obtener animales: {err}")
            return None                
                

    def obtener_animales_ordenados(self, orden_por):
        """Obtiene animales ordenados por el campo seleccionado, filtrados por la zona del trabajador."""
        try:
            conexion = mysql.connector.connect(**self.db_config)
            cursor = conexion.cursor()
            query = f"SELECT * FROM animales WHERE idzona = %s ORDER BY {orden_por}"
            cursor.execute(query)
            resultado = cursor.fetchall()
            conexion.close()
            return resultado
        except mysql.connector.Error as err:
            print(f"Error al obtener animales ordenados: {err}")
            return None


    def editar_animales(self, idanimal, nuevos_datos):
        """Edita los datos de un animal específico."""
        try:
            conexion = mysql.connector.connect(**self.db_config)
            cursor = conexion.cursor()
            query = """
            UPDATE animales
            SET tipo = %s, nombre = %s, sexo = %s, fechaingreso = %s
            WHERE idanimal = %s
            """
            cursor.execute(query, (*nuevos_datos, idanimal))
            conexion.commit()
            conexion.close()
            return True
        except mysql.connector.Error as err:
            print(f"Error al editar el animal: {err}")
            return False

    def crear_animales(self, nuevos_datos):
        """Crea un nuevo animal en la base de datos."""
        try:
            conexion = mysql.connector.connect(**self.db_config)
            cursor = conexion.cursor()
            query = """
            INSERT INTO animales (idzona, idjaula, tipo, nombre, sexo, fechaingreso)
            VALUES (%s, %s, %s, %s, %s, %s)
            """
            cursor.execute(query, nuevos_datos)
            conexion.commit()
            conexion.close()
            return True
        except mysql.connector.Error as err:
            print(f"Error al crear el animal: {err}")
            return False

    def eliminar_animales(self, idanimal):
        """Elimina un animal de la base de datos."""
        try:
            conexion = mysql.connector.connect(**self.db_config)
            cursor = conexion.cursor()
            query = "DELETE FROM animales WHERE idanimal = %s"
            cursor.execute(query, (idanimal,))
            conexion.commit()
            conexion.close()
            return True
        except mysql.connector.Error as err:
            print(f"Error al eliminar el animal: {err}")
            return False