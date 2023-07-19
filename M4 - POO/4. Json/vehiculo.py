class Vehiculo:
    def __init__(self,marca, modelo, motor):
        self.marca= marca
        self.modelo= modelo
        #self.motor= Motor(tipo,potencia)
        self.motor= motor

class Motor:
  def __init__(self,tipo,potencia):
    self.tipo= tipo
    self.potencia= potencia
  
  def __str__(self):
    return f"Potencia: {self.potencia} tipo: {self.tipo}"

motor= Motor('naftero',150)
v= Vehiculo('toyota','Etios',motor)
v2= Vehiculo('Fiat','uno',motor)
print(f"{v= }")
print(f"{v2= }")
print(f"{motor}")
print(v.motor)
del motor
print(f"{v= }")
print(f"{v2= }")
#print(f"{motor}")
print(v.motor)