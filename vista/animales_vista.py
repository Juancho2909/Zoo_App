import tkinter as tk
from tkinter import ttk  # Para usar Treeview


class AnimalesVista:
    def __init__(self,controlador):
        self.controlador = controlador
        self.ventana = tk.Tk()
        self.ventana.title("Animales")
        self.ventana.geometry("600x400")
        self.ventana.configure(bg="lightgreen")
        self.ventana.attributes("-fullscreen", True)

        etiqueta = tk.Label(self.ventana, text="Animales", font=("Helvetica", 20), bg="lightblue")
        etiqueta.pack(pady=20)
   
        # Configuración de la tabla
        self.tabla = ttk.Treeview(self.ventana, columns=("idanimal", "idzona", "idjaula", "tipo","nombre","sexo","fechaingreso"), show="headings")
        self.tabla.heading("idanimal", text="idanimal")
        self.tabla.heading("idzona", text="idzona")
        self.tabla.heading("idjaula", text="idjaula")
        self.tabla.heading("tipo", text="tipo")
        self.tabla.heading("nombre", text="nombre")
        self.tabla.heading("sexo", text="sexo")
        self.tabla.heading("fechaingreso", text="fechaingreso")
        
        self.tabla.pack(pady=20, fill="both", expand=True)
            
        
        self.boton_salir = tk.Button(self.ventana, text="Atrás", font=("Helvetica", 15), command=self.ventana.destroy, bg="lightcoral")
        self.boton_salir.pack(pady=20)


    def mostrar(self):
        self.ventana.mainloop()
        
    
    def cargar_datos(self, datos_animales):
        """Carga los datos en la tabla."""
        # Limpiar la tabla antes de insertar nuevos datos
        for item in self.tabla.get_children():
            self.tabla.delete(item)

        # Insertar los datos de los animales en la tabla
        for animal in datos_animales:
            self.tabla.insert("", "end", values=animal)
            
    def on_row_click(self, callback):
        """Asocia el evento de clic a una fila de la tabla y pasa el idanimal al callback."""
        def handle_click(event):
            seleccion = self.tabla.focus()  # Obtiene el identificador de la fila seleccionada
            if seleccion:
                valores = self.tabla.item(seleccion, "values")  # Obtiene los valores de la fila seleccionada
                if valores:  # Asegúrate de que hay valores en la fila
                    idanimal = valores[0]  # Asume que el idanimal es el primer valor
                    callback(idanimal)  # Llama al callback con el idanimal

        self.tabla.bind("<ButtonRelease-1>", handle_click)

        



        
   