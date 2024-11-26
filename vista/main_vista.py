import tkinter as tk
from PIL import Image, ImageTk
from tkinter import messagebox
import itertools  # Para cambiar colores cíclicamente

class VentanaVista:
    def __init__(self):
        self.ventana = tk.Tk()
        self.ventana.title("Zoológico Montreal")
        self.ventana.geometry("600x400")
        self.ventana.configure(bg="lightgreen")
        self.ventana.attributes("-fullscreen", True)

        # Texto animado
        self.texto_animado = tk.Label(self.ventana, text="Gestión Zoológico Montreal", font=("Helvetica", 40), bg="green")
        self.texto_animado.pack(pady=20)

        # Imagen
        imagen_path = "C:/Users/judat/OneDrive/Desktop/zoo_app/Zoológico.png"  # Cambia esto por la ruta de tu imagen
        imagen = Image.open(imagen_path)
        imagen = imagen.resize((400, 250))  # Ajustar tamaño
        self.imagen = ImageTk.PhotoImage(imagen)
        self.label_imagen = tk.Label(self.ventana, image=self.imagen)
        self.label_imagen.pack(pady=60)

        # Campos de correo y licencia
        self.etiqueta_correo = tk.Label(self.ventana, text="Correo:", font=("Helvetica", 15))
        self.etiqueta_correo.pack(pady=10)

        self.entry_correo = tk.Entry(self.ventana, font=("Helvetica", 15))
        self.entry_correo.pack(pady=10)

        self.etiqueta_licencia = tk.Label(self.ventana, text="Licencia:", font=("Helvetica", 15))
        self.etiqueta_licencia.pack(pady=10)

        self.entry_licencia = tk.Entry(self.ventana, font=("Helvetica", 15))
        self.entry_licencia.pack(pady=10)

        # Botón Iniciar sesión
        self.boton_iniciar_sesion = tk.Button(self.ventana, text="Iniciar sesión", font=("Helvetica", 15), bg="lightblue")
        self.boton_iniciar_sesion.pack(pady=10)

        self.boton_cerrar = tk.Button(self.ventana, text="Cerrar", font=("Helvetica", 15), command=self.ventana.destroy, bg="lightcoral")
        self.boton_cerrar.pack(pady=10)

        # Colores del texto animado
        self.colores = itertools.cycle(["red", "blue", "yellow", "white", "pink"])
        self.cambiar_color_texto()

    def cambiar_color_texto(self):
        if self.ventana.winfo_exists():  # Verifica si la ventana sigue existiendo
            nuevo_color = next(self.colores)
            self.texto_animado.configure(fg=nuevo_color, bg="black")
            self.ventana.after(1000, self.cambiar_color_texto)  # Cambia cada 1 segundo


    def bind_iniciar_sesion(self, callback):
        """Conecta el evento del botón 'Iniciar sesión' con la función del controlador."""
        self.boton_iniciar_sesion.config(command=callback)

    def obtener_datos_login(self):
        """Obtiene los datos de correo y licencia ingresados."""
        correo = self.entry_correo.get()
        licencia = self.entry_licencia.get()
        return correo, licencia
    

    def mostrar_mensaje_bienvenida(self):
        """Muestra la ventana emergente con el mensaje de bienvenida."""
        messagebox.showinfo("Bienvenido", "Bienvenido al Zoológico Montreal")

    def mostrar_error_login(self):
        """Muestra la ventana emergente con el mensaje de error."""
        messagebox.showerror("Error", "Usuario o Contraseña incorrectos")

    def mostrar(self):
        self.ventana.mainloop()
