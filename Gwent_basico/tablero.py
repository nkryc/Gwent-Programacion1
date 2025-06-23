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
        pygame.draw.rect(pantalla, configuracion.AZUL, (x, 500, 120, 80))
        nombre, fuerza, *_ = configuracion.mano_jugador[i]
        texto(f"{nombre}({fuerza})", x + 5, 530)

    for i in range(5):
        x = i * 150 + 20
        y = 350
        if i < len(configuracion.campo_jugador):
            nombre, fuerza, *_ = configuracion.campo_jugador[i]
            pygame.draw.rect(pantalla, configuracion.VERDE, (x, y, 120, 80))
            texto(f"{nombre}({fuerza})", x + 5, y + 25)
        else:
            pygame.draw.rect(pantalla, configuracion.GRIS, (x, y, 120, 80), 1)

    for i in range(5):
        x = i * 150 + 20
        y = 150
        if i < len(configuracion.campo_enemigo):
            nombre, fuerza, *_ = configuracion.campo_enemigo[i]
            pygame.draw.rect(pantalla, configuracion.ROJO, (x, y, 120, 80))
            texto(f"{nombre}({fuerza})", x + 5, y + 25)
        else:
            pygame.draw.rect(pantalla, configuracion.GRIS, (x, y, 120, 80), 1)

def mostrar_info():
    texto(f"Tu Fuerza: {funciones.fuerza(configuracion.campo_jugador)}", 20, 300)
    texto(f"Fuerza Enemiga: {funciones.fuerza(configuracion.campo_enemigo)}", 20, 100)
    texto(f"Rondas: {configuracion.jugador_rondas}-{configuracion.enemigo_rondas}", 550, 20)

def mostrar_resultado_ronda():
    if configuracion.ronda_terminada:
        fj = funciones.fuerza(configuracion.campo_jugador)
        fe = funciones.fuerza(configuracion.campo_enemigo)

        if fj > fe:
            texto("¡Victoria!", 500, 250)
            configuracion.jugador_rondas += 1
        elif fj < fe:
            texto("Derrota", 500, 250)
            configuracion.enemigo_rondas += 1
        else:
            texto("Empate", 500, 250)

        configuracion.esperando_clic = True
        texto("Clic para continuar...", 500, 300)

def mostrar_pantalla_final():
    pantalla.fill(configuracion.NEGRO)
    texto(configuracion.resultado_final, 520, 250)

    pygame.draw.rect(pantalla, configuracion.GRIS, (400, 400, 200, 50))
    pygame.draw.rect(pantalla, configuracion.GRIS, (700, 400, 200, 50))
    texto("Reintentar", 440, 415)
    texto("Salir",760,415)
