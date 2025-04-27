import pygame
import configuracion

pantalla = pygame.display.set_mode((configuracion.ANCHO, configuracion.ALTO))

def texto(msg, x, y, color=configuracion.BLANCO):
    img = configuracion.fuente.render(msg, True, color)
    pantalla.blit(img, (x, y))

def dibujar():
    for i in range(len(configuracion.mano_jugador)):
        pygame.draw.rect(pantalla, configuracion.AZUL, (i * 150 + 20, 500, 120, 80))
        nombre, fuerza = configuracion.mano_jugador[i]
        texto(f"{nombre}({fuerza})", i * 150 + 25, 530)

    for i in range(len(configuracion.campo_jugador)):
        pygame.draw.rect(pantalla, configuracion.VERDE, (i * 150 + 20, 350, 120, 80))
        nombre, fuerza = configuracion.campo_jugador[i]
        texto(f"{nombre}({fuerza})", i * 150 + 25, 380)

    for i in range(len(configuracion.campo_enemigo)):
        pygame.draw.rect(pantalla, configuracion.ROJO, (i * 150 + 20, 150, 120, 80))
        nombre, fuerza = configuracion.campo_enemigo[i]
        texto(f"{nombre}({fuerza})", i * 150 + 25, 180)
