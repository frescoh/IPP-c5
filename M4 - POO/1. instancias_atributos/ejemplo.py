# Mundo real world                          POO
# Verbo (accion,comportamiento)         -> Metodo
# Sustantivo   (descrir)                -> Atributos
lista= list()
print(type(lista))

lista.append(1)#[1]


class Persona:
    pass
    def saludar(self, nombre='humano'):
        print(f"Saludos {nombre}")

cyn= Persona()

print(type(cyn))
cyn.saludar('Ezequiel')

