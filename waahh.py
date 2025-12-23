import pygame
import sys

# Initialize Pygame
pygame.init()

# Screen dimensions
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Sprite Color Change Event")

# Colors
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)

# Custom event
COLOR_CHANGE_EVENT = pygame.USEREVENT + 1

class Sprite(pygame.sprite.Sprite):
    def __init__(self, x, y, color):
        super().__init__()
        self.image = pygame.Surface((50, 50))
        self.image.fill(color)
        self.rect = self.image.get_rect(topleft=(x, y))
        self.color = color
        self.colors = [RED, BLUE, GREEN]
    
    def change_color(self):
        self.color = self.colors[(self.colors.index(self.color) + 1) % len(self.colors)]
        self.image.fill(self.color)

# Create sprite group
all_sprites = pygame.sprite.Group()

# Add two sprites
sprite1 = Sprite(100, 100, RED)
sprite2 = Sprite(300, 100, BLUE)
all_sprites.add(sprite1, sprite2)

# Set up timer for color change event
pygame.time.set_timer(COLOR_CHANGE_EVENT, 1000)

# Main loop
clock = pygame.time.Clock()
running = True

while running:
    clock.tick(60)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == COLOR_CHANGE_EVENT:
            sprite1.change_color()
            sprite2.change_color()
    
    screen.fill(WHITE)
    all_sprites.draw(screen)
    pygame.display.flip()

pygame.quit()
sys.exit()