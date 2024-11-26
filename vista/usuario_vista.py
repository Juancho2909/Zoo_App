import tkinter as tk
from tkinter import ttk

class SupervisorVista:
    def __init__(self):
        self.ventana = tk.Tk()
        self.ventana.title("Supervisor")
        self.ventana.geometry("800x600")  # Ajusta el tamaño para acomodar la tabla
        self.ventana.configure(bg="lightgreen")
        
        etiqueta = tk.Label(self.ventana, text="Información del Supervisor", font=("Helvetica", 20), bg="lightblue")
        etiqueta.pack(pady=20)

        # Tabla para mostrar datos de supervisores
        self.tabla = ttk.Treeview(self.ventana, columns=("idsupervisor", "idzona", "nombre", "telefono", "correo", "licencia"), show="headings")
        self.tabla.pack(fill="both", expand=True, pady=10)

        # Configurar encabezados de las columnas
        self.tabla.heading("idsupervisor", text="ID Supervisor")
        self.tabla.heading("idzona", text="ID Zona")
        self.tabla.heading("nombre", text="Nombre")
        self.tabla.heading("telefono", text="Teléfono")
        self.tabla.heading("correo", text="Correo")
        self.tabla.heading("licencia", text="Licencia")

        # Configurar tamaños de las columnas
        self.tabla.column("idsupervisor", width=50, anchor="center")
        self.tabla.column("idzona", width=50, anchor="center")
        self.tabla.column("nombre", width=50, anchor="center")
        self.tabla.column("telefono", width=50, anchor="center")
        self.tabla.column("correo", width=50, anchor="center")
        self.tabla.column("licencia", width=50, anchor="center")

        # Botón para cerrar la ventana
        self.boton_salir = tk.Button(self.ventana, text="Cerrar", font=("Helvetica", 15), command=self.ventana.destroy, bg="lightcoral")
        self.boton_salir.pack(pady=20)

    def mostrar(self):
        self.ventana.mainloop()

    def cargar_datos(self, datos_supervisores):
        """Carga los datos en la tabla."""
        # Limpiar la tabla antes de insertar nuevos datos
        for item in self.tabla.get_children():
            self.tabla.delete(item)

        # Insertar los datos de los supervisores en la tabla
        for supervisor in datos_supervisores:
            self.tabla.insert("", "end", values=supervisor)