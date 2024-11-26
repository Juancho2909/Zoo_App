import tkinter as tk

class SeleccionVista:
    def __init__(self):
        self.ventana = tk.Tk()
        self.ventana.title("Menú Principal")
        self.ventana.geometry("600x400")
        self.ventana.configure(bg="lightgreen")
        self.ventana.attributes("-fullscreen", True)

        self.boton_cuenta = tk.Button(self.ventana, text="Ver Cuenta", font=("Helvetica", 15), command=self.ventana.destroy,bg="lightblue")
        self.boton_cuenta.pack(padx=10,pady=20)        
        
        etiqueta = tk.Label(self.ventana, text="Bienvenido al menú principal de la Aplicación", font=("Helvetica", 20),fg="lightgreen" ,bg="black")
        etiqueta.pack(pady=20)

        self.boton_animales = tk.Button(self.ventana, text="Animales", font=("Helvetica", 15), command=self.ventana.destroy,bg="lightblue")
        self.boton_animales.pack(pady=20)
        
        self.boton_articulos = tk.Button(self.ventana, text="Articulos", font=("Helvetica", 15), command=self.ventana.destroy,bg="lightblue")
        self.boton_articulos.pack(pady=20)
        
        
        self.boton_desperfectos = tk.Button(self.ventana, text="Desperfectos", font=("Helvetica", 15), command=self.ventana.destroy,bg="lightblue")
        self.boton_desperfectos.pack(pady=20)
        
        self.boton_jaulas = tk.Button(self.ventana, text="Jaulas", font=("Helvetica", 15), command=self.ventana.destroy,bg="lightblue")
        self.boton_jaulas.pack(pady=20)

        self.boton_tecnicos = tk.Button(self.ventana, text="Tecnicos", font=("Helvetica", 15), command=self.ventana.destroy,bg="lightblue")
        self.boton_tecnicos.pack(pady=20)
        
        self.boton_visitas = tk.Button(self.ventana, text="Visitas", font=("Helvetica", 15), command=self.ventana.destroy,bg="lightblue")
        self.boton_visitas.pack(pady=20)
        
        
        self.boton_salir = tk.Button(self.ventana, text="Atrás", font=("Helvetica", 15), command=self.ventana.destroy,bg="lightcoral")
        self.boton_salir.pack(pady=20)
        
    def bind_animales(self, callback):
        self.boton_animales.config(command=callback)

    def bind_articulos(self, callback):
        self.boton_articulos.config(command=callback)
        
    def bind_desperfectos(self, callback):
        self.boton_desperfectos.config(command=callback)      

    def bind_jaulas(self, callback):
        self.boton_jaulas.config(command=callback)

    def bind_tecnicos(self, callback):
        self.boton_tecnicos.config(command=callback)
        
    def bind_visitas(self, callback):
        self.boton_visitas.config(command=callback)              
                
    def bind_cuenta(self,callback):
        self.boton_cuenta.config(command=callback)
        
        
    def mostrar(self):
        self.ventana.mainloop()
