# Escribir una función que reciba un operador (+, -, *, //) y una cantidad 
# indefinida de números, y realice dicha operación a todos los números
# devolviendo un resultado.

def operacion(operador,*args):
    
    resultado=0
    if operador == '+':
        return operacion_lista(suma,args,0)     
    elif operador == '*':
        return operacion_lista(producto,args,1) 
    elif operador == '-':
        return operacion_lista(resta,args,2*args[0])
    elif operador == '//':
        return operacion_lista(div_ent,args,args[0]**2)
    

# 5,4 -> 1
# 
# 0-5= -5
# -5-4=-9 

# x -5= 5 
# neutro = lista[0]*2 
# lista[0]=x
# neutro= 2x
# primera resta= 2x-x= x


def div_ent(a,b):
    """
    Si b es 0, devuelve a

    Args:
        a (int): _description_
        b (int): Distinto de cero

    Returns:
        int: a//b  Si b es 0, devuelve a
    """
    if b!=0:
        return a//b
    else:
        return a

def resta(a,b):
    return a-b
    
def suma(a,b):
    return a+b

def producto(a,b):
    return a*b

def operacion_lista(funcion,lista,neutro):
    salida=neutro
    for numero in lista:
        salida= funcion(salida,numero)
    return salida

print(operacion('//',12,5,2,7))