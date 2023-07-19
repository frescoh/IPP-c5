class Persona:
    def __init__(self,nombre,apellido):
        self.nombre = nombre
        self.apellido = apellido
    
    def saludar(self,nombre):
        print(f"Hola {nombre}. Soy {self.nombre} {self.apellido}")
    
    def despedirse(self):
        print("Adios")
    
    def __str__(self) -> str:
        return f"Soy {self.apellido} {self.nombre}"

jesus= Persona('Jesus','Geronimo') # Se instancia el objeto jesus de la clase Persona
# jesus.saludar('Cintia') # Hola Cintia. Soy Jesus Geronimo
# print(jesus.nombre) # Jesus
print(jesus)