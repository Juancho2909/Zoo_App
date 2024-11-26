from vista.main_vista import VentanaVista
from modelo.modelo_login import ModeloLogin
from vista.seleccion_vista import SeleccionVista  # Importa la clase de la nueva ventana
from vista.animales_vista import AnimalesVista
from vista.articulos_vista import ArticulosVista
from vista.desperfectos_vista import DesperfectosVista
from vista.jaulas_vista import JaulasVista
from vista.tecnicos_vista import TecnicosVista
from vista.visitas_vista import VisitasVista
from modelo.modelo_animales import ModeloAnimales  # Asegúrate de importar el modelo de animales
from vista.usuario_vista import SupervisorVista
from modelo.modelo_articulos import ModeloArticulos
from modelo.modelo_desperfectos import ModeloDesperfectos
from modelo.modelo_jaulas import ModeloJaulas
from modelo.modelo_tecnicos import ModeloTecnicos
from modelo.modelo_visitas import ModeloVisitas
from vista.informacion_vista import InformacionVista



class VentanaControlador:
    def __init__(self):
        # Instancias de vistas
        self.main_vista = VentanaVista()  # Ventana principal
        self.seleccion_vista = None       # Inicializada al mostrarla
        self.animales_vista = None        # Inicializada al mostrarla
        self.usuario_vista = None
        self.articulos_vista = None       # Inicializada al mostrarla
        self.desperfectos_vista = None        # Inicializada al mostrarla
        self.seleccion_vista = None
        self.tecnicos_vista = None
        self.visitas_vista = None
        self.jaulas_vista = None 
        self.informacion_vista = None       
        
        # Modelos
        self.modelo_login = ModeloLogin()
        self.modelo_animales = ModeloAnimales()  # Instancia del modelo de animales
        self.modelo_articulos = ModeloArticulos()
        self.modelo_desperfectos = ModeloDesperfectos()
        self.modelo_jaulas = ModeloJaulas()
        self.modelo_tecnicos = ModeloTecnicos()
        self.modelo_visitas = ModeloVisitas()
        
        # Conectar eventos de la ventana principal
        self.main_vista.bind_iniciar_sesion(self.iniciar_sesion)

    def iniciar(self):
        """Inicia la aplicación mostrando la ventana principal."""
        self.main_vista.mostrar()

    def iniciar_sesion(self):
        """Lógica que se ejecuta al presionar 'Iniciar sesión'."""
        correo, licencia = self.main_vista.obtener_datos_login()

        
        if self.modelo_login.validar_usuario(correo, licencia):
            
            self.main_vista.mostrar_mensaje_bienvenida()
            
            self.abrir_seleccion_vista()  # Cambiar a la nueva ventana
        else:
            self.main_vista.mostrar_error_login()
              

    def abrir_seleccion_vista(self):
        """Cierra la ventana principal y abre la ventana de selección."""
        self.main_vista.ventana.quit()  # Cierra la ventana principal
        self.seleccion_vista = SeleccionVista()  # Crea la nueva ventana de selección
        self.seleccion_vista.bind_animales(self.abrir_animales_vista)  # Conecta el evento
        self.seleccion_vista.bind_cuenta(self.abrir_usuario_vista)
        self.seleccion_vista.bind_articulos(self.abrir_articulos_vista)
        self.seleccion_vista.bind_desperfectos(self.abrir_desperfectos_vista)
        self.seleccion_vista.bind_jaulas(self.abrir_jaulas_vista)
        self.seleccion_vista.bind_tecnicos(self.abrir_tecnicos_vista)
        self.seleccion_vista.bind_visitas(self.abrir_visitas_vista)           
                        
        self.seleccion_vista.mostrar()

    
    def abrir_usuario_vista(self):
        """Lógica que se ejecuta al presionar 'Iniciar sesión'."""
        self.usuario_vista = SupervisorVista()
        correo, licencia = self.main_vista.obtener_datos_login()             
        supervisor=self.modelo_login.obtener_empleado(correo, licencia)        
        # Si hay supervisores, cargarlos en la vista
        if supervisor:
            self.usuario_vista.cargar_datos(supervisor)
        # Mostrar la ventana con la información del supervisor
        self.usuario_vista.mostrar()
        
    
    
    
    def abrir_animales_vista(self):
        """Abre la ventana de Animales desde la vista de selección."""
        self.seleccion_vista.ventana.quit()  # Cierra la ventana de selección
        self.animales_vista = AnimalesVista(self)  # Crea la nueva ventana de Animales
        self.animales_vista.on_row_click(self.abrir_informacion_vista)
        correo, licencia = self.main_vista.obtener_datos_login()                
        # Obtener todos los animales desde el modelo
        animales = self.modelo_animales.obtener_todos_los_animales(correo,licencia)
        # Si hay animales, cargarlos en la vista
        if animales:
            self.animales_vista.cargar_datos(animales)
        # Mostrar la ventana de animales
        self.animales_vista.mostrar()
        
        
    def abrir_articulos_vista(self):
        """Abre la ventana de Animales desde la vista de selección."""
        self.articulos_vista = ArticulosVista(self)  # Crea la nueva ventana de Animales     
        correo, licencia = self.main_vista.obtener_datos_login()                
        # Obtener todos los animales desde el modelo
        articulos = self.modelo_articulos.obtener_todos_los_articulos(correo,licencia)                  
        # Si hay animales, cargarlos en la vista
        if articulos:
            self.articulos_vista.cargar_datos(articulos)
        # Mostrar la ventana de animales
        self.articulos_vista.mostrar()        
        
    def abrir_desperfectos_vista(self):
        """Abre la ventana de Animales desde la vista de selección."""
        self.seleccion_vista.ventana.quit()  # Cierra la ventana de selección
        self.desperfectos_vista = DesperfectosVista(self)  # Crea la nueva ventana de Animales               
        # Obtener todos los animales desde el modelo
        correo, licencia = self.main_vista.obtener_datos_login()             
        desperfectos = self.modelo_desperfectos.obtener_todos_los_desperfectos(correo,licencia)   
        # Si hay animales, cargarlos en la vista
        if desperfectos:
            self.desperfectos_vista.cargar_datos(desperfectos)

        # Mostrar la ventana de animales
        self.desperfectos_vista.mostrar()        
                
    def abrir_jaulas_vista(self):
        """Abre la ventana de Animales desde la vista de selección."""
        self.seleccion_vista.ventana.quit()  # Cierra la ventana de selección
        self.jaulas_vista = JaulasVista(self)  # Crea la nueva ventana de Animales      
        correo, licencia = self.main_vista.obtener_datos_login()             
        jaulas = self.modelo_jaulas.obtener_todas_las_jaulas(correo,licencia)                    
        
        # Si hay animales, cargarlos en la vista
        if jaulas:
            self.jaulas_vista.cargar_datos(jaulas)

        # Mostrar la ventana de animales
        self.jaulas_vista.mostrar()              
        
    def abrir_tecnicos_vista(self):
        """Abre la ventana de Animales desde la vista de selección."""
        self.seleccion_vista.ventana.quit()  # Cierra la ventana de selección
        self.tecnicos_vista = TecnicosVista(self)  # Crea la nueva ventana de Animales      
        correo, licencia = self.main_vista.obtener_datos_login()             
        tecnicos = self.modelo_tecnicos.obtener_todos_los_tecnicos(correo,licencia)                    
        
        # Si hay animales, cargarlos en la vista
        if tecnicos:
            self.tecnicos_vista.cargar_datos(tecnicos)

        # Mostrar la ventana de animales
        self.tecnicos_vista.mostrar()                   
        
        
    def abrir_visitas_vista(self):
        """Abre la ventana de Animales desde la vista de selección."""
        self.seleccion_vista.ventana.quit()  # Cierra la ventana de selección
        self.visitas_vista = VisitasVista(self)  # Crea la nueva ventana de Animales      
        correo, licencia = self.main_vista.obtener_datos_login()             
        visitas = self.modelo_visitas.obtener_todos_los_visitas(correo,licencia)                    
        
        # Si hay animales, cargarlos en la vista
        if visitas:
            self.visitas_vista.cargar_datos(visitas)

        # Mostrar la ventana de animales
        self.visitas_vista.mostrar()                           
 
    def abrir_informacion_vista(self, idanimal):
        """Abre la ventana de información de un animal específico."""
        self.informacion_vista = InformacionVista(self)
        correo, licencia = self.main_vista.obtener_datos_login()
    
        # Obtener la información específica del animal a editar
        animales_editar = self.modelo_animales.obtener_todos_los_animales_restriccion_especifico(correo, licencia, idanimal)
        tupla = animales_editar[0]
        arreglo_animales_editar = list(tupla)
        # Si hay animales, cargar el primero en la vista
        if animales_editar:
            self.informacion_vista.cargar_datos(arreglo_animales_editar)
    
        # Asignar la funcionalidad al botón Guardar
        self.informacion_vista.bind_guardar(lambda: self.guardar_informacion(idanimal))
    
        # Mostrar la ventana
        self.informacion_vista.mostrar()


    def guardar_informacion(self, idanimal):
        """Guarda la información editada de un animal."""
        tipo, nombre, sexo, fechaingreso = self.informacion_vista.guardar_datos()
        datos_animal_editado = (tipo, nombre, sexo, fechaingreso)
        self.modelo_animales.editar_animales(idanimal, datos_animal_editado)
        
        
        
        
         
                
                   

        

        
        

