import pygame
from player import Player
pygame.init()

# constants
my_player = Player(100, 200)
WIDTH = 1000
HEIGHT = 600
FPS = 60
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Simple Game")
clock = pygame.time.Clock()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    if my_player.animation_state == "Idle":
        my_player.change_animation("Idle")
    if my_player.animation_state == "Walk":
        my_player.change_animation("Walk")
    if my_player.animation_state == "Run":
        my_player.change_animation("Run")

    screen.fill((WHITE))
    my_player.update(screen)
    pygame.display.update()
    clock.tick(FPS)