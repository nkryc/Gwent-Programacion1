import pygame
import configuracion
import funciones
import tablero

pygame.init()
pygame.display.set_caption("Gwent")

pantalla = pygame.display.set_mode((configuracion.ANCHO, configuracion.ALTO))
configuracion.fondo = pygame.transform.scale(configuracion.fondo_original, pantalla.get_size())

configuracion.cargar_imagenes()

def salir():
    pygame.quit()
    exit()

def mostrar_menu():
    while True:
        pantalla.fill(configuracion.NEGRO)
        titulo = configuracion.fuente.render("Gwent", True, configuracion.BLANCO)
        instrucciones = configuracion.fuente.render("Presiona ESPACIO para jugar o ESC para salir", True, configuracion.BLANCO)

        pantalla.blit(titulo, (configuracion.ANCHO // 2 - titulo.get_width() // 2, 200))
        pantalla.blit(instrucciones, (configuracion.ANCHO // 2 - instrucciones.get_width() // 2, 300))
        pygame.display.update()

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                salir()
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_SPACE:
                    return
                if evento.key == pygame.K_ESCAPE:
                    salir()

def procesar_eventos():
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            return False

        if evento.type == pygame.MOUSEBUTTONDOWN:
            x, y = evento.pos

            if configuracion.fin_del_juego:
                if 400 <= x <= 600 and 400 <= y <= 450:
                    funciones.nueva_ronda(reiniciar_todo=True)
                if 700 <= x <= 900 and 400 <= y <= 450:
                    return False

            elif configuracion.ronda_terminada:
                if configuracion.esperando_clic:
                    funciones.nueva_ronda()
                configuracion.esperando_clic = False

            elif y > 500:
                indice = x // 150
                if indice < len(configuracion.mano_jugador) and configuracion.mano_jugador[indice] is not None:
                    funciones.jugar_carta(indice)
                    configuracion.turno += 1

    return True

def main():
    mostrar_menu()
    funciones.nueva_ronda()
    jugando = True

    while jugando:
        tablero.pantalla.fill(configuracion.NEGRO)
        jugando = procesar_eventos()

        if configuracion.turno >= configuracion.turnos_maximos:
            configuracion.ronda_terminada = True
            configuracion.esperando_clic = True

        if configuracion.fin_del_juego:
            tablero.mostrar_pantalla_final()
        else:
            tablero.dibujar()
            tablero.mostrar_info()
            tablero.mostrar_resultado_ronda()
            funciones.revisar_final()

        pygame.display.update()

    salir()

main()