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

def jugar_carta(indice):
    carta = configuracion.mano_jugador[indice]
    configuracion.mano_jugador.pop(indice)
    configuracion.campo_jugador.append(carta)

    carta_enemiga = configuracion.mano_enemigo[0]
    configuracion.mano_enemigo.pop(0)
    configuracion.campo_enemigo.append(carta_enemiga)

def revisar_final():
    if configuracion.jugador_rondas == 2:
        configuracion.resultado_final = "¡Victoria!"
        configuracion.fin_del_juego = True
    if configuracion.enemigo_rondas == 2:
        configuracion.resultado_final = "Derrota"
        configuracion.fin_del_juego = True