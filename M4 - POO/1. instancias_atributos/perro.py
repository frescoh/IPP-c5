# Ejercicio: Creación de una clase "Perro"

# Crea una clase llamada "Perro" que tenga los siguientes atributos:
# Nombre (cadena de texto)
# Raza (cadena de texto)
# Edad (entero)
# Color (cadena de texto)

# Define un constructor que reciba como parámetros el nombre, la raza, 
# la edad y el color del perro, y que inicialice los atributos correspondientes.

# Define un método llamado "ladrar" que imprima en la consola el mensaje "¡Guau, guau!".

# en el  programa, crea al menos dos objetos de la clase "Perro" y asigna valores
# a sus atributos utilizando el constructor.

# Utiliza los métodos de acceso para obtener los valores de los atributos de cada perro 
# y mostrarlos en la consola.

# Llama al método "ladrar" para cada perro creado y verifica que se imprima el 
# mensaje correspondiente.
pi= 3.1415
class Perro:
    def __init__(self,nombre:str,raza:str,edad:int,color:str):
        self.nombre = nombre
        self.raza =raza
        self.edad = edad
        self.color = color
    
    def ladrar(self):
        print("¡Guau, guau!")

lupita= Perro('Lupita','Salchicha',7,'Marron')
firulais= Perro('Firulais','dalmata',5,'Blanco y negro')

print(f"{lupita.nombre= } {lupita.raza= } {lupita.edad= } años {lupita.color= }")
print(f"{firulais.nombre= } {firulais.raza= } {firulais.edad= } años {firulais.color= }")

lupita.ladrar()
firulais.ladrar()

print(dir(Perro))