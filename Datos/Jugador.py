

import pygame, assets

WIDTH = 1200
HEIGHT = 700
BLACK = 0,0,0

pygame.init()
pygame.display.init()
screen = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Fantasy Battle Quest")
clock= pygame.time.Clock()

class Jugador(pygame.sprite.Sprite):


    def __init__(self):
        super().__init__()
        self.id= 1 #ID, va para BDD
        self.nivel = 1
        self.nombre = ""
        self.tipo = ""#Tipo, creaer clase para los tipos de pjs
        self.vida = 100
        self.arma = ""#Arma, crear clase para las armas
        self.equipo = ""#Equipo, crear clase para los Equipos
        self.image = pygame.image.load("../assets/player.png").convert()
        self.rect = self.image.get_rect()
        self.rect.centerx = WIDTH // 2
        self.rect.bottom = HEIGHT - 10
        self.speed_x = 0
        self.speed_y = 0

    def update(self):
        self.speed_x = 0
        self.speed_y = 0
        keystate = pygame.key.get_pressed()
        if keystate[pygame.K_LEFT]:
            self.speed_x = -5
        if keystate[pygame.K_RIGHT]:
            self.speed_x = 5
        if keystate[pygame.K_UP]:
            self.speed_y = -5
        if keystate[pygame.K_DOWN]:
            self.speed_y = 5
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y
        if self.rect.right > WIDTH:
            self.rect.right = WIDTH
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.top > HEIGHT:
            self.rect.top = HEIGHT
        if self.rect.bottom < 0:
            self.rect.bottom = 0




    def presentar(self,nombre,tipo,arma):
        print(f"Hola aventurero, me llamo {nombre} , mi clase es {tipo} y uso {arma}.")
        return

all_sprites = pygame.sprite.Group()


player = Jugador()
all_sprites.add(player)

running = True
while running:
    # Keep loop running at the right speed
    clock.tick(60)
    # Process input (events)
    for event in pygame.event.get():
        # check for closing window
        if event.type == pygame.QUIT:
            running = False

    # Update
    all_sprites.update()

    # Draw / Render
    screen.fill(BLACK)
    all_sprites.draw(screen)
    # *after* drawing everything, flip the display.
    pygame.display.flip()

pygame.quit()