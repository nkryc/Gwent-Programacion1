import pygame
import os 

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
ronda_evaluada = False
resultado_final = ""

jugador_rondas = 0
enemigo_rondas = 0

mano_jugador = []
mano_enemigo = []
campo_jugador = []
campo_enemigo = []

efectos_jugador = []
efectos_enemigo = []
imagenes_cartas = {}

def asignar_efecto_jugador(nombre, funcion):
    efectos_jugador.append({"nombre": nombre, "funcion": funcion})

def asignar_efecto_enemigo(nombre, funcion):
   efectos_enemigo.append({"nombre": nombre, "funcion": funcion})

todas_cartas = [
    ("Soldado", 5, lambda j, e: None),
    ("Arquero", 3, lambda j, e: asignar_efecto_enemigo("Sangrado", lambda campo: [(n, max(f - 1, 0), ef) for n, f, *ef in campo])),
    ("Caballero", 6, lambda j, e: None),
    ("Mago", 7, lambda j, e: asignar_efecto_jugador("Refuerzo", lambda campo: [(n, f + 2, ef) for n, f, *ef in campo])),
    ("Espía", 2, lambda j, e: None),
    ("Bestia", 8, lambda j, e: None),
    ("Hechicero", 5, lambda j, e: asignar_efecto_enemigo("Maleficio", lambda campo: [(n, max(f - 2, 0), ef) for n, f, *ef in campo])),
    ("Catapulta", 8, lambda j, e: None, "img/catapulta.jpg")
]

def cargar_imagenes():
    for carta in todas_cartas:
        nombre = carta[0]
        ruta = carta[3] if len(carta) > 3 else None
        if ruta and os.path.exists(ruta):
            imagen = pygame.image.load(ruta)
            imagenes_cartas[nombre] = pygame.transform.scale(imagen, (120, 80))

fondo_original = pygame.Surface((ANCHO, ALTO))
fondo_original.fill((30, 30, 30))
fondo = pygame.transform.scale(fondo_original, (ANCHO, ALTO))