import pygame
import configuracion
import funciones

pantalla = pygame.display.set_mode((configuracion.ANCHO, configuracion.ALTO))

def texto(msg, x, y, color=configuracion.BLANCO):
    img = configuracion.fuente.render(msg, True, color)
    pantalla.blit(img, (x, y))

def dibujar():
    pantalla.blit(configuracion.fondo, (0, 0))

    texto("CAMPO ENEMIGO", 20, 140)
    texto("TU CAMPO", 20, 390)
    texto("TU MANO", 20, 540)
    pygame.draw.line(pantalla, configuracion.GRIS, (0, 180), (1280, 180))
    pygame.draw.line(pantalla, configuracion.GRIS, (0, 380), (1280, 380))
    pygame.draw.line(pantalla, configuracion.GRIS, (0, 530), (1280, 530))

    if configuracion.campo_enemigo:
        nombre = configuracion.campo_enemigo[-1][0]
        texto(f"El enemigo jugó: {nombre}", 20, 100)

    for i in range(5):
        x = i * 150 + 20
        y = 200
        if i < len(configuracion.campo_enemigo):
            carta = configuracion.campo_enemigo[i]
            if carta:
                nombre, fuerza, *_ = carta
                imagen = configuracion.imagenes_cartas.get(nombre)
                if imagen:
                    pantalla.blit(imagen, (x, y))
                    texto(f"{fuerza}", x + 90, y + 5)
                else:
                    pygame.draw.rect(pantalla, configuracion.ROJO, (x, y, 120, 80), border_radius=8)
                    texto(f"{nombre} ({fuerza})", x + 5, y + 25)
        else:
            pygame.draw.rect(pantalla, configuracion.GRIS, (x, y, 120, 80), 1, border_radius=8)

    for i in range(5):
        x = i * 150 + 20
        y = 450
        if i < len(configuracion.campo_jugador):
            carta = configuracion.campo_jugador[i]
            if carta:
                nombre, fuerza, *_ = carta
                imagen = configuracion.imagenes_cartas.get(nombre)
                if imagen:
                    pantalla.blit(imagen, (x, y))
                    texto(f"{fuerza}", x + 90, y + 5)
                else:
                    pygame.draw.rect(pantalla, configuracion.VERDE, (x, y, 120, 80), border_radius=8)
                    texto(f"{nombre} ({fuerza})", x + 5, y + 25)
        else:
            pygame.draw.rect(pantalla, configuracion.GRIS, (x, y, 120, 80), 1, border_radius=8)

    for i in range(len(configuracion.mano_jugador)):
        carta = configuracion.mano_jugador[i]
        x = i * 150 + 20
        y = 600
        ancho, alto = 120, 80
        if carta is not None:
            nombre, fuerza, *_ = carta
            imagen = configuracion.imagenes_cartas.get(nombre)
            if imagen:
                pantalla.blit(imagen, (x, y))
                pygame.draw.rect(pantalla, configuracion.AZUL, (x, y, ancho, alto), 2, border_radius=8)
                texto(f"{fuerza}", x + 90, y + 5)
            else:
                pygame.draw.rect(pantalla, configuracion.AZUL, (x, y, ancho, alto), border_radius=8)
                texto(f"{nombre} ({fuerza})", x + 5, y + 25)
        else:
            pygame.draw.rect(pantalla, (60, 60, 60), (x, y, ancho, alto), border_radius=8)
            texto("Jugado", x + 20, y + 30, color=configuracion.GRIS)

    pygame.draw.rect(pantalla, configuracion.AZUL, (850, 470, 200, 80), 2, border_radius=6)
    if configuracion.efectos_jugador:
        texto("Efectos:", 860, 480)
        for i, efecto in enumerate(configuracion.efectos_jugador):
            texto(f"- {efecto['nombre']}", 860, 500 + i * 20)
    else:
        texto("Sin efecto", 860, 480)

    pygame.draw.rect(pantalla, configuracion.ROJO, (850, 220, 200, 80), 2, border_radius=6)
    if configuracion.efectos_enemigo:
        texto("Efectos:", 860, 230)
        for i, efecto in enumerate(configuracion.efectos_enemigo):
            texto(f"- {efecto['nombre']}", 860, 250 + i * 20)
    else:
        texto("Sin efecto", 860, 230)

def mostrar_info():
    texto(f"Fuerza Enemiga: {funciones.fuerza(configuracion.campo_enemigo)}", 20, 170)
    texto(f"Tu Fuerza: {funciones.fuerza(configuracion.campo_jugador)}", 20, 400)
    texto(f"Cartas: {sum(1 for c in configuracion.mano_jugador if c)}", 1050, 640)
    texto(f"Rondas: {configuracion.jugador_rondas}-{configuracion.enemigo_rondas}", 1050, 20)

def mostrar_resultado_ronda():
    if configuracion.ronda_terminada and configuracion.esperando_clic:
        fj = funciones.fuerza(configuracion.campo_jugador)
        fe = funciones.fuerza(configuracion.campo_enemigo)
        if fj > fe:
            texto("¡Ganaste la ronda!", 550, 300)
            if not configuracion.fin_del_juego:
                configuracion.jugador_rondas += 1
        elif fj < fe:
            texto("Perdiste la ronda", 550, 300)
            if not configuracion.fin_del_juego:
                configuracion.enemigo_rondas += 1
        else:
            texto("Empate", 550, 300)
        texto("Haz clic para continuar", 530, 350)

def mostrar_pantalla_final():
    pantalla.fill(configuracion.NEGRO)
    texto(configuracion.resultado_final, 550, 250)
    pygame.draw.rect(pantalla, configuracion.GRIS, (400, 400, 200, 50))
    pygame.draw.rect(pantalla, configuracion.GRIS, (700, 400, 200, 50))
    texto("Reintentar", 440, 415)
    texto("Salir", 760, 415)