import pygame
import configuracion
import funciones
import tablero

pygame.init()
pygame.display.set_caption("Gwent")
funciones.nueva_ronda()

jugando = True
while jugando:
    tablero.pantalla.fill(configuracion.NEGRO)

    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            jugando = False

        if evento.type == pygame.MOUSEBUTTONDOWN:
            if configuracion.fin_del_juego:
                x, y = evento.pos
                if 400 <= x <= 600 and 400 <= y <= 450:
                    funciones.nueva_ronda()
                if 700 <= x <= 900 and 400 <= y <= 450:
                    jugando = False
            elif configuracion.ronda_terminada:
                if configuracion.esperando_clic:
                    funciones.nueva_ronda()
                configuracion.esperando_clic = False
            else:
                x, y = evento.pos
                if y > 500:
                    indice = x // 150
                    if indice < len(configuracion.mano_jugador):
                        funciones.jugar_carta(indice)
                        configuracion.turno += 1
                        if configuracion.turno >= configuracion.turnos_maximos:
                            configuracion.ronda_terminada = True

    if configuracion.fin_del_juego:
        configuracion.mostrar_pantalla_final()
    else:
        configuracion.dibujar()
        configuracion.mostrar_info()
        configuracion.mostrar_resultado_ronda()
        funciones.revisar_final()

    pygame.display.update()

pygame.quit()