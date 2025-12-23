import pygame

# Initialize Pygame
pygame.init()

# Set window size
WIDTH, HEIGHT = 640, 480
screen = pygame.display.set_mode((WIDTH, HEIGHT))

# Set window caption
pygame.display.set_caption("My first game screen")

# Colors
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)

# Create font for text
font = pygame.font.Font(None, 36)
text = font.render("Welcome to Pygame!", True, BLACK)

# Rectangle parameters
rect_width, rect_height = 200, 100
rect_x = (WIDTH - rect_width) // 2
rect_y = (HEIGHT - rect_height) // 2
rectangle = pygame.Rect(rect_x, rect_y, rect_width, rect_height)

# Main game loop
running = True
clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # Fill background with white
    screen.fill(WHITE)
    
    # Draw rectangle
    pygame.draw.rect(screen, BLUE, rectangle)
    
    # Draw text at center
    text_rect = text.get_rect(center=(WIDTH // 2, HEIGHT // 2 - 60))
    screen.blit(text, text_rect)
    
    # Update display
    pygame.display.flip()
    clock.tick(60)

pygame.quit()