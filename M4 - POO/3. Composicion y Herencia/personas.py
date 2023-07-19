class Persona:
    def __init__(self,nombre,apellido,dni,profesion):
        self.nombre = nombre
        self.apellido = apellido
        self.dni = dni
        self.profesion = profesion
    
    def __str__(self) -> str:
        return f"{self.apellido}, {self.nombre}"


class Abogado(Persona):
    def __init__(self, nombre, apellido, dni, mp):
        super().__init__(nombre, apellido, dni, 'Abogado')
        self.mp = mp
    
    def __str__(self) -> str:
        return "Dr/a: "+super().__str__()+"\nProfesion: "+self.profesion


sil= Abogado('Sil','Aramayo','1234',987)
print(sil)