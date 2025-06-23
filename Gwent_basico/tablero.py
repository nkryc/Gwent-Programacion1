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
    texto("TU CAMPO", 20, 370)
    texto("TU MANO", 20, 540)
    
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
                    texto(f"{nombre} ({fuerza})", x + 8, y + 30)
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
                    texto(f"{nombre} ({fuerza})", x + 8, y + 30)
        else:
            pygame.draw.rect(pantalla, configuracion.GRIS, (x, y, 120, 80), 1, border_radius=8)

    for i, carta in enumerate(configuracion.mano_jugador):
        x = i * 150 + 20
        y = 600
        ancho, alto = 120, 80
        if carta:
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

    mostrar_efectos(850, 220, configuracion.efectos_enemigo, configuracion.ROJO)
    mostrar_efectos(850, 470, configuracion.efectos_jugador, configuracion.AZUL)

def mostrar_efectos(x, y, efectos, color_borde):
    alto = 80 + max(0, (len(efectos) - 1) * 20)
    ancho = 200
    fondo = pygame.Surface((ancho, alto), pygame.SRCALPHA)
    fondo.fill((30, 30, 30, 180))
    pantalla.blit(fondo, (x, y))
    pygame.draw.rect(pantalla, color_borde, (x, y, ancho, alto), 2, border_radius=6)

    texto("Efectos:", x + 10, y + 10)
    if efectos:
        for i, efecto in enumerate(efectos):
            texto(f"- {efecto['nombre']}", x + 10, y + 30 + i * 20)
    else:
        texto("Sin efecto", x + 10, y + 30)

def mostrar_info():
    texto(f"Fuerza Enemiga: {funciones.fuerza(configuracion.campo_enemigo)}", 20, 170)
    texto(f"Tu Fuerza: {funciones.fuerza(configuracion.campo_jugador)}", 20, 400)
    texto(f"Cartas en mano: {sum(1 for c in configuracion.mano_jugador if c)}", 1050, 640)
    texto(f"Rondas ganadas: {configuracion.jugador_rondas}", 1050, 20)
    texto(f"Rondas perdidas: {configuracion.enemigo_rondas}", 1050, 50)

def mostrar_resultado_ronda():
    if configuracion.ronda_terminada and configuracion.esperando_clic:
        fj = funciones.fuerza(configuracion.campo_jugador)
        fe = funciones.fuerza(configuracion.campo_enemigo)
        if fj > fe:
            texto("¡Ganaste la ronda!", 520, 300)
        elif fj < fe:
            texto("Perdiste la ronda", 520, 300)
        else:
            texto("Empate", 550, 300)
        texto("Haz clic para continuar", 500, 350)

def mostrar_pantalla_final():
    pantalla.fill(configuracion.NEGRO)
    texto(configuracion.resultado_final, 550, 250)
    pygame.draw.rect(pantalla, configuracion.GRIS, (400, 400, 200, 50), border_radius=10)
    pygame.draw.rect(pantalla, configuracion.GRIS, (700, 400, 200, 50), border_radius=10)
    texto("Reintentar", 440, 415)
    texto("Salir", 760, 415)
