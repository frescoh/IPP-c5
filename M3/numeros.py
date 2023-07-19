"""
Módulo con funciones útiles para números enteros.
"""
PI = 3.141592   # definimos una variable

def es_primo(num):
    """Calcula si un numero es primo. Responde True o False."""
    cant = 0
    divisor = 2
    while divisor < num:
        if num % divisor == 0:
            cant = cant + 1
        divisor = divisor + 1
    if cant > 0:
        return False
    else:
        return True
    
def es_par(num):
  """Calcula si un numero es par. Responde True o False"""
  return num % 2 == 0