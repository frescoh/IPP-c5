import tkinter as tk
root = tk.Tk()

label1 = tk.Label(root, text="Estoy en la fila 0, columna 0 y ocupo 2 columnas")
label1.grid(row=0, column=0, columnspan=2)

label2 = tk.Label(root, text="Estoy en la fila 1, columna 0")
label2.grid(row=1, column=0)

label3 = tk.Label(root, text="Estoy en la fila 1, columna 1")
label3.grid(row=1, column=1)

root.mainloop()
