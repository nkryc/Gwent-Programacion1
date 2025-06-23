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
    ("Soldado", 5, lambda j, e: None),  # sin efecto
    ("Arquero", 3, lambda j, e: e.append(("Herida", -2, lambda j,e: None))),  # daña al enemigo
    ("Caballero", 6, lambda j, e: None),
    ("Mago", 7, lambda j, e: j.append(("Refuerzo", 2, lambda j,e: None))),    # refuerza aliado
    ("Espía", 2, lambda j, e: j.append(("Información", 1, lambda j,e: None))),
    ("Bestia", 8, lambda j, e: None),
    ("Hechicero", 5, lambda j, e: e.append(("Debil", -1, lambda j,e: None))),
    ("Catapulta", 9, lambda j, e: None),
]

fondo_original = pygame.Surface((ANCHO, ALTO))
fondo_original.fill((30, 30, 30))