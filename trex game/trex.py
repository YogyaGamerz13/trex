import pygame
import random

# Initialize pygame
pygame.init()

# Set up the game window
WIDTH, HEIGHT = 800, 400
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("T-Rex Game")

# Load images
dino_img = pygame.image.load("dino.jpg")
cactus_img = pygame.image.load("cactus.jpg")

# Set up game variables
dino_x = 50
dino_y = HEIGHT - dino_img.get_height() - 50
dino_vel = 10

cactus_x = WIDTH + 20
cactus_y = HEIGHT - cactus_img.get_height() - 50
cactus_vel = 5

score = 0
font = pygame.font.Font(None, 36)

clock = pygame.time.Clock()

running = True
while running:
    clock.tick(30)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # Update game logic
    keys = pygame.key.get_pressed()
    if keys[pygame.K_SPACE]:
        dino_y -= dino_vel
    
    cactus_x -= cactus_vel
    if cactus_x < -cactus_img.get_width():
        cactus_x = WIDTH
        score += 1
    
    # Check for collision
    dino_rect = pygame.Rect(dino_x, dino_y, dino_img.get_width(), dino_img.get_height())
    cactus_rect = pygame.Rect(cactus_x, cactus_y, cactus_img.get_width(), cactus_img.get_height())
    if dino_rect.colliderect(cactus_rect):
        running = False
    
    # Draw elements
    win.fill((255, 255, 255))
    win.blit(dino_img, (dino_x, dino_y))
    win.blit(cactus_img, (cactus_x, cactus_y))
    
    score_text = font.render("Score: " + str(score), True, (0, 0, 0))
    win.blit(score_text, (10, 10))
    
    pygame.display.flip()

pygame.quit()