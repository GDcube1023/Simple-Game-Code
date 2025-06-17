import pygame

class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y, direction):
        super().__init__()
        self.image = pygame.Surface((10, 4))
        self.image.fill((255, 0, 0))
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.speed = 15 * direction

    def update(self):
        self.rect.x += self.speed
        
        if self.rect.right < 0 or self.rect.left > 1000:
            self.kill()
        
        keys = pygame.key.get_pressed()
        
        if keys[pygame.K_a]:
            direction = -1

        if keys[pygame.K_d]:
            direction = 1