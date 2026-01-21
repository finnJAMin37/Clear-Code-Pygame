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
player_dir = pygame.math.Vector2(0, 0)
player_speed = 400

while running:
    dt = clock.tick(60) / 1000
    # event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    #    if event.type == pygame.KEYDOWN and event.key == pygame.K_1:
    #        print(1)
    #    if event.type == pygame.MOUSEMOTION:
    #        player_rect.center = event.pos
    # print(pygame.mouse.get_pressed())
    
    keys = pygame.key.get_just_pressed()
    player_dir.x = int(keys[pygame.K_RIGHT] - keys[pygame.K_LEFT])
    player_dir.y = int(keys[pygame.K_DOWN] - keys[pygame.K_UP])
    if int(keys[pygame.K_SPACE]):
        print("fire laser!") 


    # draw the game
    display_surface.fill('darkgrey')
    for pos in star_positions:
        display_surface.blit(star_surf,(pos))
    display_surface.blit(meteor_surf, meteor_rect)
    display_surface.blit(laser_surf, laser_rect)

    #
    player_dir = player_dir.normalize() if player_dir else player_dir
    player_rect.center += player_dir * player_speed * dt

    display_surface.blit(player_surf, player_rect)

    print(player_dir.magnitude())
    
    pygame.display.update()

pygame.quit()