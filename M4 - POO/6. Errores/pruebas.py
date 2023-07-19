try:
    valor_1 = int(input("Ingrese el valor 1: "))
    valor_2 = int(input("Ingrese el valor 2: "))
except ValueError:
    print("Estoy en el except")

try:
    print(valor_1/valor_2)
except ZeroDivisionError:
    print("No se puede dividir en cero")