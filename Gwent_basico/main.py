import pygame
import configuracion
import funciones
import tablero

pygame.init()
pygame.display.set_caption("Gwent")

pantalla = pygame.display.set_mode((configuracion.ANCHO, configuracion.ALTO))
configuracion.fondo = pygame.transform.scale(configuracion.fondo, pantalla.get_size())

configuracion.cargar_imagenes()

def salir():
    pygame.quit()
    exit()

def mostrar_menu():
    """
    Muestra el menu principal del juego en pantalla y espera la interaccion del usuario.
    El menú presenta el título del juego y las instrucciones para comenzar o salir.
    - Presiona la tecla ESPACIO para iniciar el juego.
    - Presiona la tecla ESC para salir del juego.
    """
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
    """
    Procesa los eventos de la ventana principal del juego utilizando pygame.
    - Detecta el cierre de la ventana y retorna False para finalizar el juego.
    - Gestiona los clics del mouse:
        - Si el juego ha terminado, permite reiniciar la ronda o salir segun la zona clickeada.
        - Si la ronda ha terminado y se espera un clic, inicia una nueva ronda.
        - Si el clic ocurre en la zona de la mano del jugador, permite jugar una carta y avanza el turno.
    True si el juego debe continuar, False si debe finalizar.
    """
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
    """
    Funcion principal del juego Gwent.
    Esta función inicializa el menu, comienza una nueva ronda y gestiona el bucle principal del juego.
    Durante la ejecucion, procesa los eventos del usuario, actualiza el estado del tablero y controla el flujo de la partida,
    incluyendo la finalizacion de rondas y del juego.
    Guarda el resultado al finalizar la partida.
    """
    mostrar_menu()
    funciones.nueva_ronda()
    jugando = True
    configuracion.resultado_guardado = False

    while jugando:
        tablero.pantalla.fill(configuracion.NEGRO)
        jugando = procesar_eventos()

        if configuracion.turno >= configuracion.turnos_maximos and not configuracion.ronda_terminada:
            funciones.finalizar_ronda()
            configuracion.ronda_terminada = True
            configuracion.esperando_clic = True

        if configuracion.fin_del_juego:
            tablero.mostrar_pantalla_final()
            if not configuracion.resultado_guardado:
                try:
                    funciones.guardar_resultado()
                    configuracion.resultado_guardado = True
                except Exception as e:
                    print(f"Error al guardar el resultado: {e}")
        else:
            tablero.dibujar()
            tablero.mostrar_info()
            tablero.mostrar_resultado_ronda()

        pygame.display.update()

    salir()

main()