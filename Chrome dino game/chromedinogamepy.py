import pygame
import random
import sys

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 300
GROUND_HEIGHT = 50
FPS = 60
SPEED = 5
GRAVITY = 1

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Create the game window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Dino Run Game")

# Load images
dino_img = pygame.image.load("dino.png")
cactus_img = pygame.image.load("cactus.png")
bg_img = pygame.image.load("background.png")

# Scale the images
dino_img = pygame.transform.scale(dino_img, (50, 50))
cactus_img = pygame.transform.scale(cactus_img, (30, 50))
bg_img = pygame.transform.scale(bg_img, (WIDTH, HEIGHT))

# Set up initial game state
dino_x, dino_y = 50, HEIGHT - GROUND_HEIGHT - 50
cactus_x, cactus_y = WIDTH, HEIGHT - GROUND_HEIGHT - 50
dino_vel_y = 0
is_jumping = False
score = 0

# Fonts
font = pygame.font.Font(None, 36)

def reset_game():
    global dino_x, dino_y, dino_vel_y, is_jumping, cactus_x, score
    dino_x, dino_y = 50, HEIGHT - GROUND_HEIGHT - 50
    dino_vel_y = 0
    is_jumping = False
    cactus_x = WIDTH
    score = 0

def draw_text(text, x, y):
    text_surface = font.render(text, True, BLACK)
    screen.blit(text_surface, (x, y))

# Game loop
clock = pygame.time.Clock()

running = True
game_over = False
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN and not is_jumping and not game_over:
            if event.key == pygame.K_SPACE:
                dino_vel_y = -15
                is_jumping = True

        if event.type == pygame.KEYDOWN and game_over:
            if event.key == pygame.K_RETURN:
                game_over = False
                reset_game()

    if not game_over:
        # Update game objects
        dino_vel_y += GRAVITY
        dino_y += dino_vel_y

        if dino_y >= HEIGHT - GROUND_HEIGHT - 50:
            dino_y = HEIGHT - GROUND_HEIGHT - 50
            is_jumping = False

        cactus_x -= SPEED
        if cactus_x < -30:
            cactus_x = WIDTH
            cactus_y = HEIGHT - GROUND_HEIGHT - 50
            score += 1

        # Check for collisions
        dino_rect = pygame.Rect(dino_x, dino_y, 50, 50)
        cactus_rect = pygame.Rect(cactus_x, cactus_y, 30, 50)

        if dino_rect.colliderect(cactus_rect):
            game_over = True

        # Draw everything
        screen.blit(bg_img, (0, 0))
        pygame.draw.rect(screen, (200, 200, 200), (0, HEIGHT - GROUND_HEIGHT, WIDTH, GROUND_HEIGHT))
        screen.blit(dino_img, (dino_x, dino_y))
        screen.blit(cactus_img, (cactus_x, cactus_y))

        # Display score
        draw_text(f"Score: {score}", 10, 10)

    else:
        # Display game over message
        draw_text("Game Over", WIDTH // 2 - 70, HEIGHT // 2 - 30)
        draw_text("Press Enter to Play Again", WIDTH // 2 - 150, HEIGHT // 2 + 20)

    pygame.display.flip()

    clock.tick(FPS)

pygame.quit()
sys.exit()
