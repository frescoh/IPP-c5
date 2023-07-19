# Atributos: nombre, raza, color
# Metodos: hablar, moverse, comer

 ##############################################################   
class Gato:
    def __init__(self,nombre,raza,color):
        self.nombre = nombre
        self.raza =raza
        self.color = color
    
    def hablar(self):
        print("miau")
    
    def moverse(self):
        print("Estoy caminando")
    
    def comer(self):
        print("Estoy comiendo poio")
        


################################################################
class Perro:
    def __init__(self,nombre,raza,color):
        self.nombre = nombre
        self.raza =raza
        self.color = color
    def hablar(self):
        print("Guauuuu")
    
    def moverse(self):
        print("Estoy caminando al gym, como el profe")
    
    def comer(self):
        print("Estoy comiendo alimento balanceado")
    

################################################################
class Tortuga:
    def __init__(self,nombre,raza,color):
        self.nombre = nombre
        self.raza =raza
        self.color = color
        
    def hablar(self):
        print("Estoy hablando como tortuga")
    
    def moverse(self):
        print("Estoy caminando")
    
    def comer(self):
        print("Estoy comiendo pizza")