from settings import *
from player import *
from sprites import *
from random import randint

class Game:
    def __init__(self):
        # setup
        pygame.init()
        self.display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        pygame.display.set_caption(WINDOW_CAPTION)
        self.clock = pygame.time.Clock()
        self.running = True

        # groups
        self.all_sprites = pygame.sprite.Group()
        self.collision_sprites = pygame.sprite.Group()

        # sprites
        self.player = Player((200, 200), self.all_sprites, self.collision_sprites)
        for i in range(6):
            pos = (randint(0, WINDOW_WIDTH), randint(0, WINDOW_HEIGHT))
            size = (randint(50, 200), randint(50, 200))
            CollisionSprite(pos, size, (self.all_sprites, self.collision_sprites))

    def run(self):
        while self.running:
            # dt
            dt = self.clock.tick(60) / 1000
            # event loop
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
            # update
            self.player.update(dt)

            # draw
            self.display_surface.fill((0,100,20))
            self.all_sprites.draw(self.display_surface)
            pygame.display.update()
        pygame.quit()

if __name__ == '__main__':
    game = Game()
    game.run()