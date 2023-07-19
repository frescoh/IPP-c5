
class Puerta:
    pass

class Rueda:
    pass

class Motor:
    pass

class Volante:
    pass

class Ventana:
    pass

class auto:
    def __init__(self,puerta,ventana,motor,ruedas,volante,marca:str) -> None:
        self.puerta = puerta
        self.ventana =ventana
        self.motor = motor
        self.ruedas =ruedas
        self.volante = volante
        self.marca = marca
        