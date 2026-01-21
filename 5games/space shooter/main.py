import pygame
from os.path import join
from random import randint

class Player(pygame.sprite.Sprite):
    def __init__(self, groups):
        super().__init__(groups)
        self.image = pygame.image.load(join("images","player.png")).convert_alpha()
        self.rect = self.image.get_frect(center = (WINDOW_WIDTH/2, WINDOW_HEIGHT/2))
        self.dir = pygame.math.Vector2(0, 0)
        self.speed: int = 300
    def update(self, dt):
        keys = pygame.key.get_pressed()
        self.dir.x = int(keys[pygame.K_RIGHT] - keys[pygame.K_LEFT])
        self.dir.y = int(keys[pygame.K_DOWN] - keys[pygame.K_UP])
        keys = pygame.key.get_just_pressed()
        if int(keys[pygame.K_SPACE]):
            print("fire laser!") 
        self.dir = self.dir.normalize() if self.dir else self.dir
        self.rect.center += self.dir * 300 * dt

class Star(pygame.sprite.Sprite):
    def __init__(self, groups, surf):
        super().__init__(groups)
        self.image = surf
        self.rect = self.image.get_frect(center = (randint(0,WINDOW_WIDTH),randint(0, WINDOW_HEIGHT)))



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
#star_path = join("images", "star.png")
#star_surf = pygame.image.load(star_path).convert_alpha()
#star_positions = [(randint(0,WINDOW_WIDTH),randint(0, WINDOW_HEIGHT)) for i in range(20)]

# player importing image
# player_surf = pygame.image.load(join("images","player.png")).convert_alpha()
# player_rect = player_surf.get_rect(center = (WINDOW_WIDTH/2, WINDOW_HEIGHT/2))
player_dir = pygame.math.Vector2(0, 0)
# player_speed = 400



all_sprites = pygame.sprite.Group()
star_surf = pygame.image.load(join("images", "star.png")).convert_alpha()
for i in range(20):
    Star(all_sprites, star_surf)
player = Player(all_sprites)

while running:
    dt = clock.tick(60) / 1000
    # event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # keys = pygame.key.get_pressed()
    # player_dir.x = int(keys[pygame.K_RIGHT] - keys[pygame.K_LEFT])
    # player_dir.y = int(keys[pygame.K_DOWN] - keys[pygame.K_UP])
    # keys = pygame.key.get_just_pressed()
    # if int(keys[pygame.K_SPACE]):
    #     print("fire laser!") 

    all_sprites.update(dt)

    # draw the game
    display_surface.fill('darkgrey')
    
    # for pos in star_positions:
    #     display_surface.blit(star_surf,(pos))

    all_sprites.draw(display_surface)

    pygame.display.update()

pygame.quit()