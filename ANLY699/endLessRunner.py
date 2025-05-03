import pygame
import random

# Initialize
pygame.init()

# Screen setup
WIDTH, HEIGHT = 800, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Endless Runner")
clock = pygame.time.Clock()
FONT = pygame.font.SysFont(None, 40)

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Player
player = pygame.Rect(100, HEIGHT - 100, 50, 50)
player_y_velocity = 0
gravity = 0.5
jump_power = -12
is_jumping = False

# Ground
ground_y = HEIGHT - 50

# Obstacles
obstacle_width =30
obstacle_height = 40
obstacle_speed = 5
obstacles = []

# Score
score = 0

# Game loop
running = True
while running:
    screen.fill(WHITE)
    pygame.draw.rect(screen, BLACK, (0, ground_y, WIDTH, 50))  # ground

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Jump
    keys = pygame.key.get_pressed()
    if keys[pygame.K_SPACE] and not is_jumping:
        player_y_velocity = jump_power
        is_jumping = True

    # Apply gravity
    player_y_velocity += gravity
    player.y += player_y_velocity

    # Floor collision
    if player.y >= ground_y - player.height:
        player.y = ground_y - player.height
        is_jumping = False

    # Obstacle logic
    if random.randint(0, 60) == 0:  # random spawn
        obstacle = pygame.Rect(WIDTH, ground_y - obstacle_height, obstacle_width, obstacle_height)
        obstacles.append(obstacle)

    for obstacle in list(obstacles):
        obstacle.x -= obstacle_speed
        pygame.draw.rect(screen, (200, 0, 0), obstacle)
        if obstacle.colliderect(player):
            running = False  # Game over
        if obstacle.x < -obstacle_width:
            obstacles.remove(obstacle)
            score += 1

    # Draw player
    pygame.draw.rect(screen, (0, 128, 255), player)

    # Display score
    score_text = FONT.render(f"Score: {score}", True, BLACK)
    screen.blit(score_text, (10, 10))

    pygame.display.update()
    clock.tick(60)

pygame.quit()
