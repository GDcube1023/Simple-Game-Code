from pygame.sprite import Sprite
from pathlib import Path
import pygame
import os
from playsound import playsound

SCRIPT_DIR = Path(__file__).parent
SHOOT = SCRIPT_DIR / 'shoot.mp3'

class Player(Sprite):
    def __init__(self, x,y):
        super().__init__()
        self.animation_types = os.listdir("player_sprites")
        self.all_images = {}
        for animation in self.animation_types:
            self.all_images[animation] = []
            for image in os.listdir(f"player_sprites/{animation}"):
                img = pygame.image.load(f"player_sprites/{animation}/{image}")
                img = pygame.transform.scale_by(img, 0.8)
                self.all_images[animation].append(img)
        self.current_animation = "idle"
        self.current_frame = 0
        self.image = self.all_images[self.current_animation][self.current_frame]
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.last_animation_time = pygame.time.get_ticks()
        self.animation_state = "idle"
        self.direction = 1
        self.flip = False
        self.in_air = False
        self.y_vel = 0
        self.attack = False
        self.jump_attack = False
        self.attack_time = pygame.time.get_ticks()

    def update(self, screen):
        pygame.draw.line(screen, "red", (0,500), (1000,500), 1)
        pygame.draw.rect(screen, "blue", self.rect, 2)
        screen.blit(pygame.transform.flip(self.image, self.flip, False), self.rect)
        self.image = self.all_images[self.current_animation][self.current_frame]
        current_time = pygame.time.get_ticks()
        if current_time - self.last_animation_time > 100:
            self.current_frame += 1
            self.last_animation_time = pygame.time.get_ticks()
        if self.current_frame >= len(self.all_images[self.current_animation]):
            self.current_frame = 0
        
        dx = 0
        dy = 0
        keys = pygame.key.get_pressed()
        if self.in_air:
            self.animation_state = "jump"
        else:
            if not keys[pygame.K_a] and not keys[pygame.K_d]:
                self.animation_state  = "idle"

            if keys[pygame.K_a] and keys[pygame.K_LSHIFT]:
                dx -= 3
                self.animation_state = "walk"
                self.flip = True

            elif keys[pygame.K_a]:
                dx -= 10
                self.animation_state = "run"
                self.flip = True

            if keys[pygame.K_d]  and keys[pygame.K_LSHIFT]:
                dx += 3
                self.animation_state = "walk"
                self.flip = False

            elif keys[pygame.K_d]:
                dx += 10
                self.animation_state = "run"
                self.flip = False

        if keys[pygame.K_SPACE] and self.in_air == False or keys[pygame.K_w] and self.in_air == False:
            self.in_air = True
            self.animation_state = "jump"
            self.y_vel = -10
        dy += self.y_vel
        self.y_vel += 1

        if keys[pygame.K_UP]:
            self.animation_state = "shoot"

        self.rect.x += dx
        self.rect.y += dy

        if self.rect.bottom + dy >= 610:
            self.in_air = False
            self.y_vel = 0
            dy = 610 - self.rect.bottom

    def change_animation(self, animation_name):
        if self.current_animation != animation_name:
            self.current_animation = animation_name
            self.current_frame = 0
            self.last_animation_time = pygame.time.get_ticks()
        