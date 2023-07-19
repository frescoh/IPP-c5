# Ejercicio Nro 3:
# Crea una clase Auto con los atributos marca, modelo, y kilometraje. 
# Incluye el método 
# - viajar que reciba un número de kilómetros (mayor que cero) y aumente el kilometraje del
# automóvil en esa cantidad.

# Incluye los métodos especiales de comparación usando el kilometraje como atributo a comparar.

# Luego, crea una función (externa a la clase Auto) crear_autos(n) que reciba un número entero n 
# y devuelva una lista de n autos. Y una función viajar_autos(lista) que reciba dicha lista y 
# establezca un kilometraje aleatorio entre 10 y 100 para cada auto de la lista.

# Finalmente, crea un método mayor_viaje(lista) que reciba la lista de objetos, y devuelva toda 
# la información del auto que viajó más.

# Consejo: Para el método mayor_viaje puede inicializar un objeto mayor_auto en None para 
# actualizar esta instancia cada vez que se encuentre un auto con mayor kilometraje que el último 
# guardado. Y con esto se debe usar una variable de tipo entero para controlar el kilometraje más 
# alto actualmente.
import random as rd

class Auto:
    """
    _summary_
    """
    def __init__(self, marca, modelo, km):
        self.marca=marca
        self.modelo=modelo
        self.km=km
        
    def viajar(self,nKm):
        """
         reciba un número de kilómetros (mayor que cero) y aumente el kilometraje del
         automóvil en esa cantidad
         """
        if nKm>0:
            self.km+=nKm
        
    def __lt__(self,otro):
        return self.km < otro.km

    def __le__(self,otro):
        return self.km <= otro.km

    def __eq__(self,otro):
        return self.km == otro.km

    def __ne__(self,otro):
        return self.km != otro.km

    def __gt__(self,otro):  
        return self.km > otro.km

    def __ge__(self,otro):
        return self.km >= otro.km
    
#-------------Funciones fuera de la clase----------        
    

def crear_autos(n):
    autos  = []
    for i in range(n):
        marca= input("Ingrese la marca del auto: ")
        modelo= input("Ingrese el modelo: ")
        kilometraje= int(input("Ingrese el kilometraje del automovil: "))
        autos.append(Auto(marca,modelo,kilometraje))
    return autos

def viajar_autos(lista_autos):
    for auto in lista_autos:
        auto.viajar(rd.randint(10,100))

def mayor_viaje(lista_autos):
    lista_autos.sort(reverse=True)
    mayor= lista_autos[0]
    print(f"El auto que mayor kilometraje tiene es:\n {mayor.marca= } {mayor.modelo= } {mayor.km= }")

def mayor_viaje2(lista_autos):
    mayor= lista_autos[0]
    for auto in lista_autos[1:]:
        if auto>mayor:
            mayor= auto
    print(f"El auto que mayor kilometraje tiene es:\n {mayor.marca= } {mayor.modelo= } {mayor.km= }")

n= int(input("Ingrese la cantidad de autos: "))
lista= crear_autos(n)
viajar_autos(lista)
for auto in lista:
    print(auto.km)

mayor_viaje(lista)