import tkinter as tk
from tkinter import ttk  # Para usar Treeview


class VisitasVista:
    def __init__(self,controlador):
        self.controlador = controlador
        self.ventana = tk.Tk()
        self.ventana.title("Visitas")
        self.ventana.geometry("600x400")
        self.ventana.configure(bg="lightgreen")
        self.ventana.attributes("-fullscreen", True)

        etiqueta = tk.Label(self.ventana, text="Visitas", font=("Helvetica", 20), bg="lightblue")
        etiqueta.pack(pady=20)
   
        # Configuración de la tabla
        self.tabla = ttk.Treeview(self.ventana, columns=("idvisita", "idzona", "fechavisita"), show="headings")
        self.tabla.heading("idvisita", text="idvisita")
        self.tabla.heading("idzona", text="idzona")
        self.tabla.heading("fechavisita", text="fechavisita")
        
        self.tabla.pack(pady=20, fill="both", expand=True)

        self.boton_salir = tk.Button(self.ventana, text="Atrás", font=("Helvetica", 15), command=self.ventana.destroy, bg="lightcoral")
        self.boton_salir.pack(pady=20)

    def mostrar(self):
        self.ventana.mainloop()
        
        
    def cargar_datos(self, datos_visitas):
        """Carga los datos en la tabla."""
        # Limpiar la tabla antes de insertar nuevos datos
        for item in self.tabla.get_children():
            self.tabla.delete(item)

        # Insertar los datos de los animales en la tabla
        for visita in datos_visitas:
            self.tabla.insert("", "end", values=visita)
                       

        
        



        
   