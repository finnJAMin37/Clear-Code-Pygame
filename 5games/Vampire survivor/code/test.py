import pygame
from math import cos, sin

pygame.init()

WINDOW_WIDTH, WINDOW_HEIGHT = 1280, 720
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Wizard RPG")
clock = pygame.time.Clock()

# game state
running = True

class Player(pygame.sprite.Sprite):
    def __init__(self, groups):
        super().__init__(groups)
        self.originial_image = pygame.Surface((100,100), pygame.SRCALPHA)
        self.image = self.originial_image
        self.rect = self.image.get_frect(center = (200, 600))
        self.image.fill("red")
        self.angle: float = 90
        self.rotation_speed: int = 100
        self.angle_dir: int = 0

        self.move_speed: int = 200
    def update(self, dt):
        keys = pygame.key.get_pressed()
        self.angle_dir = int(keys[pygame.K_LEFT] - keys[pygame.K_RIGHT])
        self.angle += self.angle_dir*self.rotation_speed*dt
        if keys[pygame.K_UP]:
            self.rect.x += cos(self.angle * 3.14/180) * self.move_speed * dt
            self.rect.y -= sin(self.angle * 3.14/180) * self.move_speed * dt
            # print(f'angle: {self.angle} \n dx: {sin(self.angle * 3.14/180) * 100 * dt} \n dy: {sin(self.angle * 3.14/180) * 100 * dt}')
        if keys[pygame.K_DOWN]:
            self.rect.x -= cos(self.angle * 3.14/180) * self.move_speed * dt
            self.rect.y += sin(self.angle * 3.14/180) * self.move_speed * dt
        
        self.image = pygame.transform.rotozoom(self.originial_image, self.angle, 1)
        self.rect = self.image.get_frect(center = self.rect.center)

# imports

# groups
all_sprites = pygame.sprite.Group()
player = Player(all_sprites)

floor = pygame.Surface((WINDOW_WIDTH, 70))
floor_rect = floor.get_rect(bottomleft = (0,WINDOW_HEIGHT))
floor.fill("green4")

while running:
    dt = clock.tick(60) / 1000
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    all_sprites.update(dt)

    # bg
    display_surface.fill('green2')
    display_surface.blit(floor, (0,WINDOW_HEIGHT-70))

    # draw game
    all_sprites.draw(display_surface)

    pygame.display.update()

pygame.quit()
