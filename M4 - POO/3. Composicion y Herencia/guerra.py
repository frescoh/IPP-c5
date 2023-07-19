class Arma:
    pass

class Espada(Arma):
    pass

class Enemigo:
    pass

class Armadura:
    pass

class Soldado(Enemigo):
    def __init__(self,arma,armadura=None):
        self.arma =arma
        self.armadura = armadura
        