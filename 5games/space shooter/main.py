import pygame
from os.path import join
from random import randint, uniform

class Player(pygame.sprite.Sprite):
    def __init__(self, groups):
        super().__init__(groups)
        self.image = pygame.image.load(join("images","player.png")).convert_alpha()
        self.rect = self.image.get_frect(center = (WINDOW_WIDTH/2, WINDOW_HEIGHT/2))
        self.dir = pygame.math.Vector2(0, 0)
        self.speed: int = 300

        # cooldown
        self.can_shoot = True
        self.laser_shoot_time = 0
        self.cooldown_duration = 400

    def laser_timer(self):
        if not self.can_shoot:
            current_time = pygame.time.get_ticks()
            if current_time - self.laser_shoot_time >= self.cooldown_duration:
                self.can_shoot = True
    def update(self, dt):
        keys = pygame.key.get_pressed()
        self.dir.x = int(keys[pygame.K_RIGHT] - keys[pygame.K_LEFT])
        self.dir.y = int(keys[pygame.K_DOWN] - keys[pygame.K_UP])
        keys = pygame.key.get_just_pressed()
        if int(keys[pygame.K_SPACE]) and self.can_shoot:
            Laser(laser_surf, self.rect.midtop, (all_sprites, laser_sprites))
            self.can_shoot = False
            self.laser_shoot_time = pygame.time.get_ticks()
        self.dir = self.dir.normalize() if self.dir else self.dir
        self.rect.center += self.dir * 300 * dt
        self.laser_timer()

class Star(pygame.sprite.Sprite):
    def __init__(self, groups, surf):
        super().__init__(groups)
        self.image = surf
        self.rect = self.image.get_frect(center = (randint(0,WINDOW_WIDTH),randint(0, WINDOW_HEIGHT)))

class Laser(pygame.sprite.Sprite):
    def __init__(self, surf, pos, groups):
        super().__init__(groups)
        self.image = surf
        self.rect = self.image.get_frect(midbottom = pos)

    def update(self, dt):
        self.rect.centery -=400 * dt
        if self.rect.bottom < 0:
            self.kill()

class Meteor(pygame.sprite.Sprite):
    def __init__(self, surf, groups):
        super().__init__(groups)
        self.image = surf
        self.rect = self.image.get_frect(midbottom = (randint(0,WINDOW_WIDTH), 0))
        self.direction = pygame.Vector2(uniform(-0.5,0.5), 1)
        self.meteor_speed = randint(200, 300)
        self.star_time = pygame.time.get_ticks()
        self.life_time = 1000
    def update(self, dt):
        self.rect.center += self.direction * self.meteor_speed * dt
        # if pygame.time.get_ticks() - self.star_time > self.life_time:
        #     self.kill()
        if self.rect.top > WINDOW_HEIGHT:
             self.kill()

def collisions():
    global running

    collided_sprites = pygame.sprite.spritecollide(player, meteor_sprites, True)
    if collided_sprites:
        print("player hit", collided_sprites[0])
        running = False
    for laser in laser_sprites:
        collided_sprites = pygame.sprite.spritecollide(laser, meteor_sprites, True)
        if collided_sprites:
            laser.kill()

def display_score():
    current_time = pygame.time.get_ticks()
    text_surf = font.render(str(current_time // 200), True, (240, 240, 240))
    text_rect = text_surf.get_frect(midbottom = (WINDOW_WIDTH/2,WINDOW_HEIGHT - 50))
    display_surface.blit(text_surf, text_rect)
    
    pygame.draw.rect(display_surface, 'grey', text_rect.move(0,-2).inflate(15,10), 5, 10)

# general setup
pygame.init()
WINDOW_WIDTH, WINDOW_HEIGHT = 1280, 720
display_surface = pygame.display.set_mode((WINDOW_WIDTH,WINDOW_HEIGHT))
pygame.display.set_caption("Space Shooter")
running = True
clock = pygame.time.Clock()

# import
meteor_surf = pygame.image.load(join("images","meteor.png")).convert_alpha()
laser_surf = pygame.image.load(join("images", "laser.png")).convert_alpha()
star_surf = pygame.image.load(join("images", "star.png")).convert_alpha()
font = pygame.font.Font(None, 50)

# sprites
all_sprites = pygame.sprite.Group()
meteor_sprites = pygame.sprite.Group()
laser_sprites = pygame.sprite.Group()
for i in range(20):
    Star(all_sprites, star_surf)
player = Player(all_sprites)

# custom events -> meteor event
meteor_event = pygame.event.custom_type()
pygame.time.set_timer(meteor_event, 2000)

while running:
    dt = clock.tick(60) / 1000
    # event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == meteor_event:
            Meteor(meteor_surf, (all_sprites, meteor_sprites))

    all_sprites.update(dt)
    # collisions
    collisions()

    # draw the game
    display_surface.fill('#3a2e3f')
    display_score()
    all_sprites.draw(display_surface)

    pygame.display.update()

pygame.quit()