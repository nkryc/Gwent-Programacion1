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
resultado_guardado = False

jugador_rondas = 0
enemigo_rondas = 0

mano_jugador = []
mano_enemigo = []
campo_jugador = []
campo_enemigo = []

efectos_jugador = []
efectos_enemigo = []
imagenes_cartas = {}

def asignar_efecto(nombre, campo_objetivo):
    def efecto(campo):
        return [(n, max(f - 1, 0), ef) for n, f, *ef in campo]
    if campo_objetivo is campo_jugador:
        efectos_jugador.append({"nombre": nombre, "funcion": efecto})
    else:
        efectos_enemigo.append({"nombre": nombre, "funcion": efecto})

todas_cartas = [
    ("Soldado", 5, lambda jugador, enemigo: None, "Gwent_basico/img/Soldado.jpg"),
    ("Cazador", 3, lambda jugador, enemigo: asignar_efecto("Sangrado", enemigo), "Gwent_basico/img/Cazador.jpg"),
    ("Caballero", 6, lambda jugador, enemigo: None, "Gwent_basico/img/Caballero.jpg"),
    ("Mago", 7, lambda jugador, enemigo: asignar_efecto("Refuerzo", jugador), "Gwent_basico/img/Mago.jpg"),
    ("Espía", 2, lambda jugador, enemigo: None, "Gwent_basico/img/Espia.jpg"),
    ("Bestia", 8, lambda jugador, enemigo: None, "Gwent_basico/img/Bestia.jpg"),
    ("Hechicera", 5, lambda jugador, enemigo: asignar_efecto("Maleficio", enemigo),"Gwent_basico/img/Hechicera.jpg"),
    ("Catapulta", 8, lambda jugador, enemigo: None, "Gwent_basico/img/Catapulta.jpg"),
    ("Arpía", 2, lambda jugador, enemigo: None, "Gwent_basico/img/Arpia.jpg"),
    ("Asesino", 6, lambda jugador, enemigo: None, "Gwent_basico/img/Asesino.jpg"),
    ("Balista", 7, lambda jugador, enemigo: None, "Gwent_basico/img/Balista.jpg"),
    ("Bárbaro", 5, lambda jugador, enemigo: None, "Gwent_basico/img/Barbaro.jpg"),
    ("Basilisco", 6, lambda jugador, enemigo: None, "Gwent_basico/img/Basilisco.jpg"),
    ("Bruja", 9, lambda jugador, enemigo: None, "Gwent_basico/img/Bruja.jpg"),
    ("Brujo", 10, lambda jugador, enemigo: None, "Gwent_basico/img/Brujo.jpg"),
    ("Caballeria", 5, lambda jugador, enemigo: None, "Gwent_basico/img/Caballeria.jpg"),
    ("Demonio", 10, lambda jugador, enemigo: None, "Gwent_basico/img/Demonio.jpg"),
    ("Diplomatico", 3, lambda jugador, enemigo: None, "Gwent_basico/img/Diplomatico.jpg"),
    ("Dragon", 8, lambda jugador, enemigo: None, "Gwent_basico/img/Dragon.jpg"),
    ("Elfo", 5, lambda jugador, enemigo: None, "Gwent_basico/img/Elfo.jpg"),
    ("Enano", 4, lambda jugador, enemigo: None, "Gwent_basico/img/Enano.jpg"),
    ("Espíritu", 8, lambda jugador, enemigo: None, "Gwent_basico/img/Espiritu.jpg"),
    ("Gigante", 8, lambda jugador, enemigo: None, "Gwent_basico/img/Gigante.jpg"),
    ("Golem", 6, lambda jugador, enemigo: None, "Gwent_basico/img/Golem.jpg"),
    ("Grifo", 7, lambda jugador, enemigo: None, "Gwent_basico/img/Grifo.jpg"),
    ("Guardián", 8, lambda jugador, enemigo: None, "Gwent_basico/img/Guardian.jpg"),
    ("Insecto", 4, lambda jugador, enemigo: None, "Gwent_basico/img/Insecto.jpg"),
    ("Mercenario", 5, lambda jugador, enemigo: None, "Gwent_basico/img/Mercenario.jpg"),
    ("Sabio", 9, lambda jugador, enemigo: None, "Gwent_basico/img/Sabio.jpg"),
    ("Vampíro", 8, lambda jugador, enemigo: None, "Gwent_basico/img/Vampiro.jpg")
]

def cargar_imagenes():
    for carta in todas_cartas:
        nombre = carta[0]
        ruta = carta[3] if len(carta) > 3 else None
        if ruta and os.path.exists(ruta):
            imagen = pygame.image.load(ruta)
            imagenes_cartas[nombre] = pygame.transform.scale(imagen, (120, 100))

try:
    fondo_original = pygame.image.load("Gwent_basico/img/fondo.jpg")
    fondo = pygame.transform.scale(fondo_original, (ANCHO, ALTO))
except Exception as e:
    print(f"No se pudo cargar el fondo: {e}")
    fondo = pygame.Surface((ANCHO, ALTO))
    fondo.fill(GRIS)