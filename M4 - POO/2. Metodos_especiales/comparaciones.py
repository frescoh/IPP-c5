class Persona:
    def __init__(self,nombre, edad, altura):
        self.nombre = nombre
        self.edad = edad
        self.altura = altura
    
    def __str__(self):
        return f"{self.nombre}"
    
    def __gt__(self, otra_persona):
        return self.edad>otra_persona.edad
    
    def __lt__(self, otra_persona):
        return self.edad<otra_persona.edad
    
    def __len__(self):
        return self.edad
        

    

cintia= Persona('Cintia',37,1.5)
jesus= Persona('Jesus',25,1.9)

print(f"{jesus<cintia= }") # jesus.__gt__(cintia) 

print(jesus)

print(f"{len(jesus)= }")
print(f"{jesus.edad =}")