# Recibe una lista de numeros
def promedio(lista):
    """
    Calcula el promedio de los numeros ingresados 

    Returns:
        _float_: suma de los numeros/ cantidad de numeros. 0 si la cantidad de numeros ingresados es 0
    """
    if len(lista) ==0:
        return 0
    else:
        return sum(lista)/len(lista)

numeros= []
numero= float(input("Ingrese un numero, 0 para salir: "))
while numero!=0:
    numeros.append(numero)
    numero = float(input("Ingrese un numero, 0 para salir: "))

print(promedio(numeros))
    