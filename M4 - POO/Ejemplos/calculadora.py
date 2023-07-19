class Calculadora:
    def __init__(self,uno:int,dos:int):
        self.uno =uno
        self.dos =dos
    
    def sumar(self):
        return self.uno + self.dos
    
    def restar(self):
        return self.uno - self.dos
    
    def multiplicar(self):
        return self.uno * self.dos
    
    def dividir(self):
        dividendo= self.uno
        divisor= self.dos
        
        if divisor == 0:
            return 0
        else:
            return dividendo/divisor

c= Calculadora(8,4)

print(f"{c.sumar()= }")
print(f"{c.dividir()= }")