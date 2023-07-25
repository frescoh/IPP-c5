import tkinter as tk

class MiApp(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Aplicación con tkinter y clases")
        self.geometry("300x150")

        self.frame_principal = MiFrame(self)  # Creamos una instancia del frame personalizado
        self.frame_principal.pack()


class MiFrame(tk.Frame):
    def __init__(self, master):
        super().__init__(master)

        self.crear_widgets()

    def crear_widgets(self):
        # Colocamos un botón
        self.boton_saludo = tk.Button(self, text="¡Saludar!", command=self.saludar)
        self.boton_saludo.pack(pady=20)
        
        self.boton_limpiar = tk.Button(self, text="limpiar", command=self.limpiar)
        self.boton_limpiar.pack(pady=20)

        # Colocamos un cuadro de texto
        self.cuadro_texto = tk.Entry(self, font=("Arial", 12))
        self.cuadro_texto.pack()

    def saludar(self):
        nombre = self.cuadro_texto.get()  # Obtenemos el texto del cuadro de texto
        mensaje = f"Hola, {nombre}!"
        self.cuadro_texto.delete(0, tk.END)  # Limpiamos el cuadro de texto
        self.cuadro_texto.insert(0, mensaje)  # Insertamos el mensaje

    def limpiar(self):
        self.cuadro_texto.delete(0, tk.END) # Limpiamos el cuadro de texto completo

if __name__ == "__main__":
    app = MiApp()
    app.mainloop()
