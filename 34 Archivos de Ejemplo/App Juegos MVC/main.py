import tkinter as tk

from models.juego import Juego
from views.vista_inicio import VistaInicio
from views.vista_juegos import VistaJuegos
from views.vista_info import VistaInfo
from controllers.controlador_inicio import ControladorInicio
from controllers.controlador_juegos import ControladorJuegos
from controllers.controlador_info import ControladorInfo


class Aplicacion(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.title("Aplicación de Videojuegos")
        self.geometry("330x300")
        self.resizable(False, False)
        self.inicializar()
        self.cambiar_frame(self.vista_inicio)

    def inicializar(self):
        juegos = Juego.cargar_de_json("data/juegos.json")

        controlador_inicio = ControladorInicio(self)
        controlador_juegos = ControladorJuegos(self, juegos)
        controlador_info = ControladorInfo(self)

        self.vista_inicio = VistaInicio(self, controlador_inicio)
        self.vista_juegos = VistaJuegos(self, controlador_juegos)
        self.vista_info = VistaInfo(self, controlador_info)

        self.ajustar_frame(self.vista_inicio)
        self.ajustar_frame(self.vista_juegos)
        self.ajustar_frame(self.vista_info)

    def ajustar_frame(self, frame):
        frame.grid(row=0, column=0, sticky="nsew")

    def cambiar_frame(self, frame_destino):
        frame_destino.tkraise()


if __name__ == "__main__":
    app = Aplicacion()
    app.mainloop()
