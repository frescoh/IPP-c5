import json

persona = {
  "nombre": "John Doe",
  "edad": 33,
  "pais": "Narnia"
}

persona_json = json.dumps(persona) # str
print(f"{type(persona_json)= }")

