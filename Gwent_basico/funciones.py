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
    configuracion.efectos_jugador.clear()
    configuracion.efectos_enemigo.clear()
    configuracion.ronda_evaluada = False

    if reiniciar_todo:
        configuracion.jugador_rondas = 0
        configuracion.enemigo_rondas = 0

def jugar_carta(indice):
    carta = configuracion.mano_jugador[indice]
    if carta is None:
        return
    configuracion.mano_jugador[indice] = None
    configuracion.campo_jugador.append(carta)
    aplicar_efecto(carta, configuracion.campo_jugador, configuracion.campo_enemigo)
    jugar_turno_enemigo()

def jugar_turno_enemigo():
    if configuracion.mano_enemigo:
        carta_enemiga = configuracion.mano_enemigo.pop(0)
        configuracion.campo_enemigo.append(carta_enemiga)
        aplicar_efecto(carta_enemiga, configuracion.campo_enemigo, configuracion.campo_jugador)

def aplicar_efecto(carta, campo_propio, campo_enemigo):
    if len(carta) > 2 and callable(carta[2]):
        carta[2](campo_propio, campo_enemigo)

def aplicar_efectos_persistentes():
    for efecto in configuracion.efectos_jugador:
        configuracion.campo_jugador[:] = efecto["funcion"](configuracion.campo_jugador)
    for efecto in configuracion.efectos_enemigo:
        configuracion.campo_enemigo[:] = efecto["funcion"](configuracion.campo_enemigo)

def revisar_final():
    if configuracion.jugador_rondas == 2:
        configuracion.resultado_final = "¡Victoria!"
        configuracion.fin_del_juego = True
    if configuracion.enemigo_rondas == 2:
        configuracion.resultado_final = "Derrota"
        configuracion.fin_del_juego = True

def finalizar_ronda():
    if configuracion.ronda_evaluada:
        return
    configuracion.ronda_evaluada = True
    
    aplicar_efectos_persistentes()
    fj = fuerza(configuracion.campo_jugador)
    fe = fuerza(configuracion.campo_enemigo)
    if fj > fe:
        configuracion.jugador_rondas += 1
    elif fj < fe:
        configuracion.enemigo_rondas += 1
    revisar_final()