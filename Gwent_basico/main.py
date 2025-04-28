import pygame
import configuracion
import funciones
import tablero

pygame.init()
pygame.display.set_caption("Gwent")

pantalla = pygame.display.set_mode((configuracion.ANCHO, configuracion.ALTO))
configuracion.fondo = pygame.transform.scale(configuracion.fondo_original, pantalla.get_size())

menu = True
while menu:
    pantalla.fill(configuracion.NEGRO)
    texto_titulo = configuracion.fuente.render("Gwent", True, configuracion.BLANCO)
    texto_instrucciones = configuracion.fuente.render("Presiona ESPACIO para jugar o ESC para salir", True, configuracion.BLANCO)

    pantalla.blit(texto_titulo, (configuracion.ANCHO // 2 - texto_titulo.get_width() // 2, 200))
    pantalla.blit(texto_instrucciones, (configuracion.ANCHO // 2 - texto_instrucciones.get_width() // 2, 300))

    pygame.display.update()

    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            exit()
        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_SPACE:
                menu = False
            if evento.key == pygame.K_ESCAPE:
                pygame.quit()
                exit()
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
                    funciones.nueva_ronda(reiniciar_todo=True)
               
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
        tablero.mostrar_pantalla_final()  
    else:
        tablero.dibujar()  
        tablero.mostrar_info()  
        tablero.mostrar_resultado_ronda()  
        funciones.revisar_final()  

    pygame.display.update()  

pygame.quit()