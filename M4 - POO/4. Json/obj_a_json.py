import json
	
class Persona:
    def __init__(self, nombre, edad, pais):
        self.nombre = nombre
        self.edad = edad
        self.pais = pais

    def a_dict(self):
        return {"tipo": "Persona", "nombre": self.nombre, "edad": self.edad, "pais": self.pais}

persona = Persona("John Doe", 33, "Narnia")

with open('persona.json', 'w') as f:
    json.dump(persona.a_dict(), f)


def de_json(data):
    tipo = data.get('tipo')
    if tipo == 'Persona':
        return Persona(**data)


    