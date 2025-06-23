import pygame
import configuracion
import funciones

pantalla = pygame.display.set_mode((configuracion.ANCHO, configuracion.ALTO))

def texto(msg, x, y, color=configuracion.BLANCO):
    img = configuracion.fuente.render(msg, True, color)
    pantalla.blit(img, (x, y))

def dibujar():
    pantalla.blit(configuracion.fondo, (0, 0))

    for i in range(len(configuracion.mano_jugador)):
        x = i * 150 + 20
        pygame.draw.rect(pantalla, configuracion.AZUL, (x, 600, 120, 80), border_radius=8)
        nombre, fuerza, *_ = configuracion.mano_jugador[i]
        texto(f"{nombre} ({fuerza})", x + 5, 625)

    for i in range(5):
        x = i * 150 + 20
        y = 450
        if i < len(configuracion.campo_jugador):
            nombre, fuerza, *_ = configuracion.campo_jugador[i]
            pygame.draw.rect(pantalla, configuracion.VERDE, (x, y, 120, 80), border_radius=8)
            texto(f"{nombre} ({fuerza})", x + 5, y + 25)
        else:
            pygame.draw.rect(pantalla, configuracion.GRIS, (x, y, 120, 80), 1, border_radius=8)

    pygame.draw.rect(pantalla, configuracion.AZUL, (850, 470, 200, 40), 2, border_radius=6)
    if configuracion.efecto_jugador:
        nombre, _ = configuracion.efecto_jugador
        texto(f"Efecto: {nombre}", 860, 480)
    else:
        texto("Sin efecto", 860, 480)

    for i in range(5):
        x = i * 150 + 20
        y = 200
        if i < len(configuracion.campo_enemigo):
            nombre, fuerza, *_ = configuracion.campo_enemigo[i]
            pygame.draw.rect(pantalla, configuracion.ROJO, (x, y, 120, 80), border_radius=8)
            texto(f"{nombre} ({fuerza})", x + 5, y + 25)
        else:
            pygame.draw.rect(pantalla, configuracion.GRIS, (x, y, 120, 80), 1, border_radius=8)

    pygame.draw.rect(pantalla, configuracion.ROJO, (850, 220, 200, 40), 2, border_radius=6)
    if configuracion.efecto_enemigo:
        nombre, _ = configuracion.efecto_enemigo
        texto(f"Efecto: {nombre}", 860, 230)
    else:
        texto("Sin efecto", 860, 230)

def mostrar_info():
    texto(f"Tu Fuerza: {funciones.fuerza(configuracion.campo_jugador)}", 20, 400)
    texto(f"Fuerza Enemiga: {funciones.fuerza(configuracion.campo_enemigo)}", 20, 170)
    texto(f"Rondas: {configuracion.jugador_rondas}-{configuracion.enemigo_rondas}", 1050, 20)

def mostrar_resultado_ronda():
    if configuracion.ronda_terminada:
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

        configuracion.esperando_clic = True
        texto("Haz clic para continuar...", 530, 350)

def mostrar_pantalla_final():
    pantalla.fill(configuracion.NEGRO)
    texto(configuracion.resultado_final, 550, 250)

    pygame.draw.rect(pantalla, configuracion.GRIS, (400, 400, 200, 50))
    pygame.draw.rect(pantalla, configuracion.GRIS, (700, 400, 200, 50))
    texto("Reintentar", 440, 415)
    texto("Salir", 760, 415)