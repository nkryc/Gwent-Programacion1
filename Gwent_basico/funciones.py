import random
import configuracion
from datetime import datetime

def fuerza(campo):
    """
    Calcula la fuerza total de un conjunto de cartas en el campo.
    """
    total = 0
    for carta in campo:
        total += carta[1]
    return total

def nueva_ronda(reiniciar_todo=False):
    """
    Inicializa una nueva ronda, repartiendo nuevas manos y limpiando los campos.
    """
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
    """
    Juega una carta de la mano del jugador y aplica su efecto.
    """
    if carta is None:
        return  # Previene jugar la misma carta dos veces
    configuracion.mano_jugador[indice] = None
    configuracion.campo_jugador.append(carta)
    if carta[2]:
        carta[2](configuracion.campo_jugador, configuracion.campo_enemigo)
    # Juega el enemigo
    if configuracion.mano_enemigo:
        carta_enemiga = random.choice(configuracion.mano_enemigo)
        configuracion.mano_enemigo.remove(carta_enemiga)
        configuracion.campo_enemigo.append(carta_enemiga)
        if carta_enemiga[2]:
            carta_enemiga[2](configuracion.campo_enemigo, configuracion.campo_jugador)

def jugar_turno_enemigo():
    """
    Hace que el enemigo juegue una carta y aplique su efecto.
    """
    if configuracion.mano_enemigo:
        carta_enemiga = random.choice(configuracion.mano_enemigo)
        configuracion.mano_enemigo.remove(carta_enemiga)
        configuracion.campo_enemigo.append(carta_enemiga)
        aplicar_efecto(carta_enemiga, configuracion.campo_enemigo, configuracion.campo_jugador)

def aplicar_efecto(carta, campo_propio, campo_enemigo):
    """
    Aplica el efecto de una carta a los campos correspondiente.
    """
    if len(carta) > 2 and callable(carta[2]):
        carta[2](campo_propio, campo_enemigo)

def aplicar_efectos_persistentes():
    """
    Aplica todos los efectos activos en las listas de efectos del jugador y enemigo.
    Estos efectos modifican las cartas en el campo cada vez que se llaman.
    """
    for efecto in configuracion.efectos_jugador:
        configuracion.campo_jugador[:] = efecto["funcion"](configuracion.campo_jugador)
    for efecto in configuracion.efectos_enemigo:
        configuracion.campo_enemigo[:] = efecto["funcion"](configuracion.campo_enemigo)

def revisar_final():
    """
    Verifica si alguno de los jugadores ha ganado 2 rondas.
    Si es asi, marca el juego como finalizado.
    """
    if configuracion.jugador_rondas == 2:
        configuracion.resultado_final = "¡Victoria!"
        configuracion.fin_del_juego = True
    if configuracion.enemigo_rondas == 2:
        configuracion.resultado_final = "Derrota"
        configuracion.fin_del_juego = True

def finalizar_ronda():
    """
    Finaliza la ronda actual, aplica efectos persistentes,
    calcula la fuerza total de cada jugador, y actualiza el marcador de rondas ganadas.
    """
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
 
def guardar_resultado(nombre_archivo="registro_partidas.txt"):
    """
    Guarda el resultado de la partida en un archivo de texto.
    """
    try:
        ahora = datetime.now()
        marca_tiempo = ahora.strftime("%Y-%m-%d %H:%M:%S")

        with open(nombre_archivo, "a", encoding="utf-8") as archivo:
            archivo.write(f"Fecha y hora: {marca_tiempo}\n")
            archivo.write("Resultado de la partida:\n")
            archivo.write(f"Jugador: {configuracion.jugador_rondas} rondas ganadas\n")
            archivo.write(f"Enemigo: {configuracion.enemigo_rondas} rondas ganadas\n")
            archivo.write(f"Resultado Final: {configuracion.resultado_final}\n") 
            archivo.write("-----------\n")
    except IOError as e:
        print(f"No se pudo guardar el resultado: {e}")