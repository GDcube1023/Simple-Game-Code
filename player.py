import pygame
from pygame.sprite import Sprite
import os

class Player(Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.animation_types = os.listdir("assets")
        self.all_images = {}
        for animation in self.animation_types:
            self.all_images[animation] =[]
            for image in os.listdir(f"assets/{animation}"):
                img = pygame.image.load(f"assets/{animation}/{image}")
                img = pygame.transform.scale_by(img, 0.4)
                self.all_images[animation].append(img)
        self.current_animation = "Idle"
        self.current_frame = 0
        self.image = self.all_images[self.current_animation][self.current_frame]
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.last_animation_time = pygame.time.get_ticks()
        self.animation_state = "Idle"
        self.direction = -1
        self.flip = False
        self.y_vel = 0

    def update(self, screen):
        pygame.draw.line(screen, "red", (0, 500), (1000, 500), 1)
        pygame.draw.rect(screen, "blue", self.rect, 2)
        screen.blit(
            pygame.transform.flip(self.image, self.flip, False)
            , self.rect) 
        self.image = self.all_images[self.current_animation][self.current_frame]
        current_time = pygame.time.get_ticks()
        if pygame.time.get_ticks() - self.last_animation_time > 100:
            self.last_animation_time = current_time
            self.current_frame += 1
        if self.current_frame >= len(self.all_images[self.current_animation]):
            self.current_frame = 0

        dx = 0
        dy = 0
        keys = pygame.key.get_pressed()

        # Key Functions
        if keys[pygame.K_a] and not keys[pygame.K_LSHIFT]:
            self.animation_state = "Run"
            self.flip = True
            dx -= 10

        if keys[pygame.K_d] and not keys[pygame.K_LSHIFT]:
            self.animation_state = "Run"
            self.flip = False
            dx += 10

        if keys[pygame.K_a] and keys[pygame.K_LSHIFT]:
            self.animation_state = "Walk"
            self.flip = True
            dx -= 5

        if keys[pygame.K_d] and keys[pygame.K_LSHIFT]:
            self.animation_state = "Walk"
            self.flip = False
            dx += 5
        
        if not keys[pygame.K_a] and not keys[pygame.K_d]:
            self.animation_state = "Idle"

        if keys[pygame.K_w] or keys[pygame.K_SPACE]:
            self.in_air = True
            self.animation_state = "Jump"
            self.y_vel = -10
        
        if self.rect.bottom >= 500:
            self.in_air = False
            self.y_vel = 0
            dy = 500 - self.rect.bottom

        dy += self.y_vel
        self.y_vel += 1
        self.rect.x += dx
        self.rect.y += dy
    
    def change_animation(self, animation_name):
        if self.current_animation != animation_name:
            self.current_animation = animation_name
            self.current_frame = 0
            self.last_animation_time = pygame.time.get_ticks()