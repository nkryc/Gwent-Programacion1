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
turnos_maximos = 5
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

efecto_jugador = None 
efecto_enemigo = None

def asignar_efecto_jugador(nombre, funcion):
    global efecto_jugador
    efecto_jugador = (nombre, funcion)

def asignar_efecto_enemigo(nombre, funcion):
    global efecto_enemigo
    efecto_enemigo = (nombre, funcion)

todas_cartas = [
    ("Soldado", 5, lambda j, e: None),
    ("Arquero", 3, lambda j, e: asignar_efecto_enemigo("Sangrado", lambda campo: [(n, max(f - 1, 0), ef) for n, f, *ef in campo])),
    ("Caballero", 6, lambda j, e: None),
    ("Mago", 7, lambda j, e: asignar_efecto_jugador("Refuerzo", lambda campo: [(n, f + 2, ef) for n, f, *ef in campo])),
    ("Espía", 2, lambda j, e: None),
    ("Bestia", 8, lambda j, e: None),
    ("Hechicero", 5, lambda j, e: asignar_efecto_enemigo("Maleficio", lambda campo: [(n, max(f - 2, 0), ef) for n, f, *ef in campo])),
    ("Catapulta", 9, lambda j, e: None)
]

fondo_original = pygame.Surface((ANCHO, ALTO))
fondo_original.fill((30, 30, 30))
fondo = pygame.transform.scale(fondo_original, (ANCHO, ALTO))