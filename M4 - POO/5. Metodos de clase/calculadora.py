class Calculadora:      
    def __init__(self,valor_a,valor_b) -> None:
        self.valor_a = valor_a
        self.valor_b = valor_b
    
    def sumar_instancia(self):
        return self.valor_a + self.valor_b
    
    @classmethod
    def sumar(cls,x,y):
        return x+y

a= 5
b= 7
resultado = Calculadora.sumar(a,b)
print(f"El resultado de la suma entre {a} y {b} es: {resultado}")

casio=  Calculadora(a,b)
print(f"desde instancia - El resultado de la suma entre {a} y {b} es: {casio.sumar_instancia()}")