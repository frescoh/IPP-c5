class Entero:
    def __init__(self, valor):
        self.valor = valor
    
    def __str__(self):
        return f"{self.valor}"
    
    def __lt__(self, other): # self<other
        self.valor < other.valor
    

def crear_enteros(inicio,fin,n):
    import random
    enteros= []
    for i in range(n):
        enteros.append(Entero(random.randint(inicio,fin)))
    return enteros

lista= crear_enteros(0,50,20)
lista.sort(key=lambda x: x.valor)
for numero in lista:
    print(numero, end=' - ')