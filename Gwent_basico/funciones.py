import random
import configuracion

def fuerza(campo):
    total = 0
    for carta in campo:
        total += carta[1]
    return total

def nueva_ronda(reiniciar_todo=False):

    configuracion.mano_jugador = random.sample(configuracion.todas_cartas, 5)
    configuracion.mano_enemigo = random.sample(configuracion.todas_cartas, 5)
    configuracion.campo_jugador = []
    configuracion.campo_enemigo = []
    configuracion.turno = 0
    configuracion.ronda_terminada = False
    configuracion.esperando_clic = False
    configuracion.fin_del_juego = False
    configuracion.resultado_final = ""
    configuracion.efecto_jugador = None
    configuracion.efecto_enemigo = None

    if reiniciar_todo:
        configuracion.jugador_rondas = 0
        configuracion.enemigo_rondas = 0

def jugar_carta(indice):
    carta = configuracion.mano_jugador.pop(indice)
    configuracion.campo_jugador.append(carta)
    aplicar_efecto(carta, configuracion.campo_jugador, configuracion.campo_enemigo)
    jugar_turno_enemigo()

def jugar_turno_enemigo():
    if configuracion.mano_enemigo:
        carta = configuracion.mano_enemigo.pop(0)
        configuracion.campo_enemigo.append(carta)
        aplicar_efecto(carta, configuracion.campo_enemigo, configuracion.campo_jugador)
        
def aplicar_efecto(carta, campo_propio, campo_enemigo):
    if len(carta) > 2 and callable(carta[2]):
        carta[2](campo_propio, campo_enemigo)

def aplicar_efectos_persistentes():
    if configuracion.efecto_jugador:
        _, efecto = configuracion.efecto_jugador
        configuracion.campo_jugador[:] = efecto(configuracion.campo_jugador)
    if configuracion.efecto_enemigo:
        _, efecto = configuracion.efecto_enemigo
        configuracion.campo_enemigo[:] = efecto(configuracion.campo_enemigo)

def revisar_final():
    if configuracion.jugador_rondas == 2:
        configuracion.resultado_final = "¡Victoria!"
        configuracion.fin_del_juego = True
    if configuracion.enemigo_rondas == 2:
        configuracion.resultado_final = "Derrota"
        configuracion.fin_del_juego = True