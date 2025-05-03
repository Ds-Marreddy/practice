import pygame
import random

# Init
pygame.init()

# Settings
TILE_SIZE = 100
GRID_SIZE = 3
MARGIN = 5
WIDTH = HEIGHT = TILE_SIZE * GRID_SIZE + MARGIN * (GRID_SIZE + 1)
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Sliding Puzzle")

FONT = pygame.font.SysFont(None, 60)
WHITE = (255, 255, 255)
GRAY = (180, 180, 180)
BLACK = (0, 0, 0)

# Initialize tiles
tiles = list(range(1, GRID_SIZE**2)) + [0]
random.shuffle(tiles)

# Convert to 2D grid
def to_grid(lst):
    return [lst[i:i+GRID_SIZE] for i in range(0, len(lst), GRID_SIZE)]

grid = to_grid(tiles)

# Find empty tile (0)
def find_empty():
    for y in range(GRID_SIZE):
        for x in range(GRID_SIZE):
            if grid[y][x] == 0:
                return x, y

# Draw tiles
def draw_grid():
    screen.fill(WHITE)
    for y in range(GRID_SIZE):
        for x in range(GRID_SIZE):
            value = grid[y][x]
            rect = pygame.Rect(
                x * TILE_SIZE + MARGIN * (x + 1),
                y * TILE_SIZE + MARGIN * (y + 1),
                TILE_SIZE,
                TILE_SIZE,
                )
            if value == 0:
                pygame.draw.rect(screen, WHITE, rect)
            else:
                pygame.draw.rect(screen, GRAY, rect)
                text = FONT.render(str(value), True, BLACK)
                text_rect = text.get_rect(center=rect.center)
                screen.blit(text, text_rect)

# Check win
def is_solved():
    expected = list(range(1, GRID_SIZE**2)) + [0]
    return sum(grid, []) == expected

# Swap tiles
def swap(x1, y1, x2, y2):
    grid[y1][x1], grid[y2][x2] = grid[y2][x2], grid[y1][x1]

# Game loop
running = True
while running:
    draw_grid()
    if is_solved():
        msg = FONT.render("Solved!", True, (0, 200, 0))
        screen.blit(msg, (WIDTH // 2 - msg.get_width() // 2, 10))
    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mx, my = event.pos
            x = mx // (TILE_SIZE + MARGIN)
            y = my // (TILE_SIZE + MARGIN)
            ex, ey = find_empty()

            if (abs(ex - x) == 1 and ey == y) or (abs(ey - y) == 1 and ex == x):
                swap(x, y, ex, ey)

pygame.quit()
