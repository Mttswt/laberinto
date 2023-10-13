import pygame
import sys
from lectortxt import level

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 640, 480
CELL_SIZE = 32
WHITE = (255, 255, 255)
PLAYER_COLOR = (0, 0, 255)

# Create the game window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Lab Game')

# Find the player's initial position and the target position
for row, line in enumerate(level):
    if 'x' in line:
        player_x = line.index('x')
        player_y = row
    if 'w' in line:
        target_x = line.index('w')
        target_y = row

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    for row, line in enumerate(level):
        for col, char in enumerate(line):
            if char == '1':
                pygame.draw.rect(screen, (0, 0, 0), pygame.Rect(col * CELL_SIZE, row * CELL_SIZE, CELL_SIZE, CELL_SIZE))
            elif char == '0':
                pygame.draw.rect(screen, WHITE, pygame.Rect(col * CELL_SIZE, row * CELL_SIZE, CELL_SIZE, CELL_SIZE))
    
    # Draw the target ('w')
    pygame.draw.rect(screen, (0, 255, 0), pygame.Rect(target_x * CELL_SIZE, target_y * CELL_SIZE, CELL_SIZE, CELL_SIZE))

    # Draw the player ('x')
    pygame.draw.rect(screen, PLAYER_COLOR, pygame.Rect(player_x * CELL_SIZE, player_y * CELL_SIZE, CELL_SIZE, CELL_SIZE))

    pygame.display.flip()
pygame.quit()
sys.exit()