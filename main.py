import pygame
import random
import sys

# Inicialización
pygame.init()
WIDTH, HEIGHT = 800, 600
WHITE = (255, 255, 255)
GRAY = (200, 200, 200)
GREEN = (0, 150, 0)
BLACK = (0, 0, 0)
FONT = pygame.font.SysFont("arial", 20)
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Gwent Básico")


# ==== CLASES ====

class Carta:
    def __init__(self, nombre, valor):
        self.nombre = nombre
        self.valor = valor


class Jugador:
    def __init__(self, es_cpu=False):
        self.mano = self.generar_mano()
        self.cartas_en_juego = []
        self.es_cpu = es_cpu

    def generar_mano(self):
        nombres = ["Espadachín", "Arquero", "Mago", "Lancero", "Asesino"]
        return [Carta(random.choice(nombres), random.randint(1, 10)) for _ in range(5)]

    def jugar_carta(self, indice):
        if 0 <= indice < len(self.mano):
            carta = self.mano.pop(indice)
            self.cartas_en_juego.append(carta)

    def puntaje_total(self):
        return sum(c.valor for c in self.cartas_en_juego)


class Juego:
    def __init__(self):
        self.jugador = Jugador()
        self.cpu = Jugador(es_cpu=True)
        self.turno_jugador = True  # alternancia de turnos
        self.running = True

    def detectar_slot_click(self, x, y):
        fila_y = HEIGHT - 170
        if fila_y <= y <= fila_y + 150:
            for i in range(5):
                slot_x = 20 + i * 120
                if slot_x <= x <= slot_x + 100:
                    return i
        return None

    def turno_cpu(self):
        if self.cpu.mano:
            carta = self.cpu.mano.pop(0)
            self.cpu.cartas_en_juego.append(carta)

    def manejar_click(self, pos):
        if self.turno_jugador:
            indice = self.detectar_slot_click(*pos)
            if indice is not None and indice < len(self.jugador.mano):
                self.jugador.jugar_carta(indice)
                self.turno_jugador = False
                pygame.time.delay(500)
                self.turno_cpu()
                self.turno_jugador = True

    def dibujar(self):
        screen.fill(WHITE)
        self.dibujar_fila(self.cpu.cartas_en_juego, 50)
        self.dibujar_fila(self.jugador.cartas_en_juego, HEIGHT - 200)
        self.dibujar_slots_mano(self.jugador.mano)

        puntos_jugador = self.jugador.puntaje_total()
        puntos_cpu = self.cpu.puntaje_total()

        texto_pj = FONT.render(f"Jugador: {puntos_jugador}", True, BLACK)
        texto_cpu = FONT.render(f"CPU: {puntos_cpu}", True, BLACK)
        screen.blit(texto_pj, (20, HEIGHT // 2 + 40))
        screen.blit(texto_cpu, (20, HEIGHT // 2 - 60))

        pygame.display.flip()

    def dibujar_fila(self, cartas, y):
        for i, carta in enumerate(cartas):
            x = 20 + i * 120
            pygame.draw.rect(screen, GREEN, (x, y, 100, 150))
            nombre = FONT.render(carta.nombre, True, WHITE)
            valor = FONT.render(str(carta.valor), True, WHITE)
            screen.blit(nombre, (x + 10, y + 10))
            screen.blit(valor, (x + 35, y + 100))

    def dibujar_slots_mano(self, mano):
        y = HEIGHT - 170
        for i in range(5):
            x = 20 + i * 120
            pygame.draw.rect(screen, GRAY, (x, y, 100, 150), 2)
            if i < len(mano):
                carta = mano[i]
                nombre = FONT.render(carta.nombre, True, BLACK)
                valor = FONT.render(str(carta.valor), True, BLACK)
                screen.blit(nombre, (x + 10, y + 10))
                screen.blit(valor, (x + 35, y + 100))


# ==== LOOP PRINCIPAL ====

juego = Juego()

while juego.running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            juego.running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            juego.manejar_click(pygame.mouse.get_pos())

    juego.dibujar()

pygame.quit()
sys.exit()