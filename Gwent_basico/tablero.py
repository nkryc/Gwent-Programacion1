import pygame
import configuracion
import funciones

pantalla = pygame.display.set_mode((configuracion.ANCHO, configuracion.ALTO))
ronda_mostrada = False  

def texto(msg, x, y, color=configuracion.BLANCO):
    img = configuracion.fuente.render(msg, True, color)
    pantalla.blit(img, (x, y))

def dibujar():
    pantalla.blit(configuracion.fondo, (0, 0))

    texto("CAMPO ENEMIGO", 20, 170)
    texto("TU CAMPO", 20, 420)
    texto("TU MANO", 20, 570)

    for i in range(5):
        x = i * 150 + 20
        y = 200
        if i < len(configuracion.campo_enemigo):
            nombre, fuerza, *_ = configuracion.campo_enemigo[i]
            pygame.draw.rect(pantalla, configuracion.ROJO, (x, y, 120, 80), border_radius=8)
            texto(f"{nombre} ({fuerza})", x + 5, y + 25)
        else:
            pygame.draw.rect(pantalla, (80, 80, 80), (x, y, 120, 80), 1, border_radius=8)

    pygame.draw.rect(pantalla, configuracion.ROJO, (850, 220, 200, 80), 2, border_radius=6)
    if configuracion.efectos_enemigo:
        texto("Efectos:", 860, 230)
        for i, efecto in enumerate(configuracion.efectos_enemigo):
            texto(f"- {efecto['nombre']}", 860, 250 + i * 20)
    else:
        texto("Sin efecto", 860, 230)
        
    for i in range(5):
        x = i * 150 + 20
        y = 450
        if i < len(configuracion.campo_jugador):
            nombre, fuerza, *_ = configuracion.campo_jugador[i]
            pygame.draw.rect(pantalla, configuracion.VERDE, (x, y, 120, 80), border_radius=8)
            texto(f"{nombre} ({fuerza})", x + 5, y + 25)
        else:
            pygame.draw.rect(pantalla, (80, 80, 80), (x, y, 120, 80), 1, border_radius=8)

    pygame.draw.rect(pantalla, configuracion.AZUL, (850, 470, 200, 80), 2, border_radius=6)
    if configuracion.efectos_jugador:
        texto("Efectos:", 860, 480)
        for i, efecto in enumerate(configuracion.efectos_jugador):
            texto(f"- {efecto['nombre']}", 860, 500 + i * 20)
    else:
        texto("Sin efecto", 860, 480)

    for i in range(len(configuracion.mano_jugador)):
        x = i * 150 + 20
        y = 600
        pygame.draw.rect(pantalla, configuracion.AZUL, (x, y, 120, 80), border_radius=8)
        nombre, fuerza, *_ = configuracion.mano_jugador[i]
        texto(f"{nombre} ({fuerza})", x + 5, y + 25)

def mostrar_info():
    texto(f"Tu Fuerza: {funciones.fuerza(configuracion.campo_jugador)}", 1050, 400)
    texto(f"Fuerza Enemiga: {funciones.fuerza(configuracion.campo_enemigo)}", 1050, 170)
    texto(f"Rondas ganadas: {configuracion.jugador_rondas}-{configuracion.enemigo_rondas}", 1050, 20)
    texto(f"Cartas restantes: {len(configuracion.mano_jugador)}", 1050, 600)

def mostrar_resultado_ronda():
    global ronda_mostrada

    if configuracion.ronda_terminada and not ronda_mostrada:
        fj = funciones.fuerza(configuracion.campo_jugador)
        fe = funciones.fuerza(configuracion.campo_enemigo)

        if fj > fe:
            texto("¡Victoria!", 550, 300)
            configuracion.jugador_rondas += 1
        elif fj < fe:
            texto("Derrota", 550, 300)
            configuracion.enemigo_rondas += 1
        else:
            texto("Empate", 550, 300)

        ronda_mostrada = True
        texto("Haz clic para continuar...", 530, 350)

    elif not configuracion.ronda_terminada:
        ronda_mostrada = False

def mostrar_pantalla_final():
    pantalla.fill(configuracion.NEGRO)
    texto(configuracion.resultado_final, 550, 250)

    pygame.draw.rect(pantalla, configuracion.GRIS, (400, 400, 200, 50))
    pygame.draw.rect(pantalla, configuracion.GRIS, (700, 400, 200, 50))
    texto("Reintentar", 440, 415)
    texto("Salir", 760, 415)