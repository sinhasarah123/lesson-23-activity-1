import pygame

# Initialize Pygame
pygame.init()

# Window parameters
WINDOW_WIDTH = 500
WINDOW_HEIGHT = 500
WINDOW_CAPTION = "my first game screen"
BACKGROUND_COLOR = (58, 58, 58)

# Image parameters
IMAGE_SIZE = 300
IMAGE_SIZE_TUPLE = (IMAGE_SIZE, IMAGE_SIZE)

# Create the game window
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption(WINDOW_CAPTION)

# Create a placeholder surface (replace with actual image loading)
image_surface = pygame.Surface(IMAGE_SIZE_TUPLE)
image_surface.fill((200, 200, 200))  # Light gray placeholder

# Calculate center position
center_x = (WINDOW_WIDTH - IMAGE_SIZE) // 2
center_y = (WINDOW_HEIGHT - IMAGE_SIZE) // 2
image_rect = image_surface.get_rect(topleft=(center_x, center_y))

# Game loop
running = True
clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # Fill background
    screen.fill(BACKGROUND_COLOR)
    
    # Draw image
    screen.blit(image_surface, image_rect)
    
    # Update display
    pygame.display.flip()
    clock.tick(60)

pygame.quit()