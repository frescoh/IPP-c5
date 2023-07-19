class Empleado:
    id_empleado=0 # Atributo de clase
    def __init__(self,nombre):
        self.nombre = nombre # Atributo de instancia
        self.id = self.siguiente_id() 
    
    @classmethod
    def siguiente_id(cls):
        cls.id_empleado +=1
        return cls.id_empleado

    def __str__(self) -> str:
        return f"Nombre: {self.nombre} - ID: {self.id}"

empleados= []
for i in range(3):
    nombre= input("Ingrese su nombre: ")
    empleados.append(Empleado(nombre))

for empleado in empleados:
    print(empleado)