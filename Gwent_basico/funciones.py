import random
import configuracion

def fuerza(campo):
    total = 0
    for carta in campo:
        total += carta[1]
    return total