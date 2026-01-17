import pygame
from os.path import join
from random import randint

# general setup
pygame.init()
WINDOW_WIDTH, WINDOW_HEIGHT = 1280, 720
display_surface = pygame.display.set_mode((WINDOW_WIDTH,WINDOW_HEIGHT))
pygame.display.set_caption("Space Shooter")
running = True

# surface
ground_surf = pygame.Surface((WINDOW_WIDTH, WINDOW_HEIGHT/4))

# importing star image
star_path = join("images", "star.png")
star_surf = pygame.image.load(star_path).convert_alpha()
star_positions = [(randint(0,WINDOW_WIDTH),randint(0, WINDOW_HEIGHT)) for i in range(20)]

# importing image
x, y = 100, 200
player_path = join("images","player.png")
player_surf = pygame.image.load(player_path).convert_alpha()

while running:
    # event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # draw the game
    x += .1
    display_surface.fill('darkgrey')
    display_surface.blit(ground_surf, (0, WINDOW_HEIGHT-(WINDOW_HEIGHT/4)))
    for pos in star_positions:
        display_surface.blit(star_surf,(pos))
    display_surface.blit(player_surf, (x, y))
    
    pygame.display.update()

pygame.quit()