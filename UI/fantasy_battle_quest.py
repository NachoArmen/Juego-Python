##Inicio de Fantasy Battle Quest
import pygame

WIDTH = 1200
HEIGHT = 700
pygame.init()
pygame.display.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Fantasy Battle Quest")
clock = pygame.time.Clock()


def draw_text(surface, text, size, x, y):
    font = pygame.font.SysFont("serif", size)
    text_surface = font.render(text, True, (255, 255, 255))
    text_rect = text_surface.get_rect()
    text_rect.midtop = (x, y)
    surface.blit(text_surface, text_rect)

background= (0,0,0)
def show_go_screen():
    screen.blit(background, [0, 0])
    draw_text(screen, "SHOOTER", 65, WIDTH // 2, HEIGHT // 4)
    draw_text(screen, "Instruciones van aquí", 27, WIDTH // 2, HEIGHT // 2)
    draw_text(screen, "Press Key", 20, WIDTH // 2, HEIGHT * 3 / 4)
    pygame.display.flip()
    waiting = True
    while waiting:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYUP:
                waiting = False







