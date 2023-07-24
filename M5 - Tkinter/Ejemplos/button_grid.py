import tkinter as tk
from tkinter import ttk
def mostrar_mensaje():
    print("Hola Tkinter")

# Crear la ventana
ventana = tk.Tk()
ventana.geometry("200x200")  # Establecer las dimensiones de la ventana

# Crear el botón
boton = ttk.Button(ventana, text="Haz clic", command=mostrar_mensaje)

# Centrar el botón con grid
boton.grid(row=0, column=0, padx=25, pady=25)

# Iniciar el bucle de eventos
ventana.mainloop()
