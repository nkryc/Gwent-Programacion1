import pygame

ANCHO, ALTO = 1280, 720
BLANCO = (255, 255, 255)
NEGRO = (0, 0, 0)
AZUL = (50, 100, 255)
ROJO = (255, 50, 50)
VERDE = (50, 255, 50)
GRIS = (100, 100, 100)

pygame.font.init()
fuente = pygame.font.SysFont(None, 36)

turno = 0
turnos_maximos = 8
ronda_terminada = False
esperando_clic = False
fin_del_juego = False
resultado_final = ""

jugador_rondas = 0
enemigo_rondas = 0

mano_jugador = []
mano_enemigo = []
campo_jugador = []
campo_enemigo = []


todas_cartas = [
    ("Soldado", 5), ("Arquero", 3), ("Caballero", 6), ("Mago", 7), ("Asesino", 4),
    ("Bestia", 8), ("Hechicero", 5), ("Catapulta", 9), ("Espía", 2), ("Guardia", 6),
    ("Ladrón", 4), ("Cazador", 3), ("Bruja", 7), ("Monje", 3), ("Bárbaro", 6)
]
fondo_original = pygame.image.load("Imagenes/fondo.jpg")
fondo = pygame.transform.scale(fondo_original, (ANCHO, ALTO))