# Escribir una función que reciba una cantidad arbitraria de números enteros y obtenga el promedio.

def promedio(*args:float)->float:
    """
    Calcula el promedio de los numeros ingresados 

    Returns:
        _float_: suma de los numeros/ cantidad de numeros. 0 si la cantidad de numeros ingresados es 0
    """
    if len(args) ==0:
        return 0
    else:
        return sum(args)/len(args)


materias= {
    'lengua': 5,
    'matematicas':10,
    'geografia':10,
}
a,b,c= materias.values()
prom= promedio(a,b,c)
print(round(prom,2))
print(f"{prom:.2f}")