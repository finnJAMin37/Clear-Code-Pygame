import pygame
from os.path import join
from random import randint

# general setup
pygame.init()
WINDOW_WIDTH, WINDOW_HEIGHT = 1280, 720
display_surface = pygame.display.set_mode((WINDOW_WIDTH,WINDOW_HEIGHT))
pygame.display.set_caption("Space Shooter")
running = True
clock = pygame.time.Clock()

# meteor
meteor_path = join("images","meteor.png")
meteor_surf = pygame.image.load(meteor_path).convert_alpha()
meteor_rect = meteor_surf.get_rect(center = (WINDOW_WIDTH/2, WINDOW_HEIGHT/2))

# laser
laser_path = join("images", "laser.png")
laser_surf = pygame.image.load(laser_path).convert_alpha()
laser_rect = laser_surf.get_rect(bottomleft = (20, WINDOW_HEIGHT-20))

# importing star image
star_path = join("images", "star.png")
star_surf = pygame.image.load(star_path).convert_alpha()
star_positions = [(randint(0,WINDOW_WIDTH),randint(0, WINDOW_HEIGHT)) for i in range(20)]

# player importing image
player_path = join("images","player.png")
player_surf = pygame.image.load(player_path).convert_alpha()
player_rect = player_surf.get_rect(center = (WINDOW_WIDTH/2, WINDOW_HEIGHT/2))
player_dir = pygame.math.Vector2(-1, -1)
player_speed = 400

while running:
    dt = clock.tick(60) / 1000
    # event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # draw the game
    display_surface.fill('darkgrey')
    for pos in star_positions:
        display_surface.blit(star_surf,(pos))
    display_surface.blit(meteor_surf, meteor_rect)
    display_surface.blit(laser_surf, laser_rect)

    # player movement
    if player_rect.top < 0 or player_rect.bottom > WINDOW_HEIGHT:
        player_dir[1] *= -1
        if player_rect.left < 0 or player_rect.right > WINDOW_WIDTH:
            pygame.display.set_caption("CORNER!!")
            player_dir[0] *= -1
    elif player_rect.left < 0 or player_rect.right > WINDOW_WIDTH:
        player_dir[0] *= -1
    player_rect.center += player_dir * player_speed * dt

    display_surface.blit(player_surf, player_rect)
    
    pygame.display.update()

pygame.quit()