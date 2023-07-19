import json
from obj_a_json import Persona

def de_json(data):
    tipo = data.get('tipo')
    if tipo == 'Persona':
        del data['tipo']
        return Persona(**data)

with open('persona.json', 'r') as f:
    data = json.load(f)
    persona = de_json(data)

print(f"{type(persona)= }")