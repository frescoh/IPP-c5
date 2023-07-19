class Calculadora:
    """
    Esta clase permite hacer operaciones matematicas
    modelo: srt que indica el modelo de esta calcudora
    """
    def __init__(self,modelo):
        self.modelo = modelo
    
    def sumar(self,a,b):
        """
        _summary_

        Args:
            a (_type_): _description_
            b (_type_): _description_

        Returns:
            _type_: _description_
        """
        return a+b
    
    def multiplicar(self,a,b):
        return a*b
    
    def dividir(self,a,b):
        if b==0:
            return 0
        return a/b

    def restar(self,a,b):
        return a-b
    
c= Calculadora('casio9000')
a= 5
b= 7
print(c.multiplicar(a,b))
print(c.restar(a=b,b=a))
