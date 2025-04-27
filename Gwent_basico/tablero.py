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
