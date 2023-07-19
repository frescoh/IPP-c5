# Itentos
# 1. ['__annotations__', '__builtins__', '__cached__', 
# '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__'] 

# 2. ['__annotations__', '__builtins__', '__cached__', '__doc__', '__file__',
# '__loader__', '__name__', '__package__', '__spec__', 'pi']

# 3. ['Perro', '__annotations__', '__builtins__', '__cached__', '__doc__', '__file__', 
# '__loader__', '__name__', '__package__', '__spec__', 'pi']


# 4. amespace_ej.py'  de Perro
# ['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__',
#  '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', 
# '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', 
# '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', 
# 'ladrar']



class Perro:    
    """Clase que representa  a un perro"""
    def __init__(self, name,raza,color,peso):
        self.name = name
        self.raza = raza
        self.color = color
        self.peso = peso
    
    def ladrar(self):
        print('guau  guau')


pi= 3.141516
# print(dir(Perro))
# print(Perro.__doc__)

july = Perro('July')    # Sustantivo -> Atributo
july.ladrar()           #verbo / accion -> Metodo
print(july.name," está ladrando")
