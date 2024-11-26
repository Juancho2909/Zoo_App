import tkinter as tk



class InformacionVista:
    def __init__(self, controlador):
        self.controlador = controlador
        self.ventana = tk.Tk()
        self.ventana.title("Información de Animal")
        self.ventana.geometry("600x600")  # Aumenté el tamaño para acomodar los campos de entrada
        self.ventana.configure(bg="lightgreen")

        # Etiqueta de título
        self.etiqueta = tk.Label(
            self.ventana,
            text="Información de Animales",
            font=("Helvetica", 20),
            bg="lightblue",
        )
        self.etiqueta.pack(pady=20)

        
        # Campos de entrada para información de un animal
        self.frame_entrada = tk.Frame(self.ventana, bg="lightgreen")
        self.frame_entrada.pack(pady=20)


        self.label_tipo = tk.Label(self.frame_entrada, text="tipo:", font=("Helvetica", 12), bg="lightgreen")
        self.label_tipo.grid(row=1, column=0, padx=5, pady=5)
        self.entry_tipo = tk.Entry(self.frame_entrada, font=("Helvetica", 12))
        self.entry_tipo.grid(row=1, column=1, padx=5, pady=5)

        self.label_nombre = tk.Label(self.frame_entrada, text="nombre:", font=("Helvetica", 12), bg="lightgreen")
        self.label_nombre.grid(row=2, column=0, padx=5, pady=5)
        self.entry_nombre = tk.Entry(self.frame_entrada, font=("Helvetica", 12))
        self.entry_nombre.grid(row=2, column=1, padx=5, pady=5)

        self.label_sexo = tk.Label(self.frame_entrada, text="sexo:", font=("Helvetica", 12), bg="lightgreen")
        self.label_sexo.grid(row=3, column=0, padx=5, pady=5)
        self.entry_sexo = tk.Entry(self.frame_entrada, font=("Helvetica", 12))
        self.entry_sexo.grid(row=3, column=1, padx=5, pady=5)

        self.label_fechaingreso = tk.Label(self.frame_entrada, text="fechaingreso:", font=("Helvetica", 12), bg="lightgreen")
        self.label_fechaingreso.grid(row=4, column=0, padx=5, pady=5)
        self.entry_fechaingreso = tk.Entry(self.frame_entrada, font=("Helvetica", 12))
        self.entry_fechaingreso.grid(row=4, column=1, padx=5, pady=5)

        # Botón para guardar la información
        self.boton_guardar = tk.Button(self.ventana, text="Guardar", font=("Helvetica", 15), command=self.guardar_datos, bg="lightblue")
        self.boton_guardar.pack(pady=20)

        # Botón para salir
        self.boton_salir = tk.Button(self.ventana, text="Atrás", font=("Helvetica", 15), command=self.ventana.destroy, bg="lightcoral")
        self.boton_salir.pack(pady=20)

    def mostrar(self):
        self.ventana.mainloop()


    def cargar_datos(self, datos_animal):
        """Carga los datos del animal en los campos de entrada."""
        if datos_animal:
            tipo, nombre, sexo, fechaingreso = datos_animal
            self.entry_tipo.insert(0, tipo)
            self.entry_nombre.insert(0, nombre)
            self.entry_sexo.insert(0, sexo)
            self.entry_fechaingreso.insert(0, fechaingreso)



    def bind_guardar(self, callback):
        self.boton_guardar.config(command=callback)
        
    

    def guardar_datos(self):
        """Recoge los datos de los campos de entrada y los pasa al controlador."""
        tipo = self.entry_tipo.get()
        nombre = self.entry_nombre.get()        
        sexo = self.entry_sexo.get()
        fechaingreso = self.entry_fechaingreso.get()
        return tipo,nombre,sexo,fechaingreso


