import random
import configuracion

def fuerza(campo):
    total = 0
    for carta in campo:
        total += carta[1]
    return total

def nueva_ronda(reiniciar_todo=False):

    configuracion.mano_jugador = random.sample(configuracion.todas_cartas, 8)
    configuracion.mano_enemigo = random.sample(configuracion.todas_cartas, 8)
    configuracion.campo_jugador = []
    configuracion.campo_enemigo = []
    configuracion.turno = 0
    configuracion.ronda_terminada = False
    configuracion.esperando_clic = False
    configuracion.fin_del_juego = False
    configuracion.resultado_final = ""

    if reiniciar_todo:
        configuracion.jugador_rondas = 0
        configuracion.enemigo_rondas = 0