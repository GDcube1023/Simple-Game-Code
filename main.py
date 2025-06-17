import pygame
import os
from player2 import Player
from bullet import Bullet
pygame.init()

bullets = pygame.sprite.Group()

WIDTH, HEIGHT = 1280, 720
FPS = 60
WHITE = (255, 255, 255)

screen = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Simple 2D Shooting Game")
clock = pygame.time.Clock()

my_player = Player(300, 200)
my_bullet = Bullet(300, 200, 1)
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    
        my_player.change_animation(my_player.animation_state)
    
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                bullet = Bullet(my_player.rect.centerx, my_player.rect.centery, my_player.direction)
                bullets.add(bullet)

    screen.fill(WHITE)
    bullets.update()
    bullets.draw(screen)
    my_player.update(screen)
    pygame.display.update()
    clock.tick(FPS)