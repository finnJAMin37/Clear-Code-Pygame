import pygame

class Game:
    def __init__(self):
        # initialize
        pygame.init()

        # display
        WINDOW_WIDTH, WINDOW_HEIGHT = 1280, 720
        self.display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        pygame.display.set_caption('3d test')

        # game loop
        self.clock = pygame.time.Clock()
        self.running = True

        # groups
        self.all_points = pygame.sprite.Group()

        # sprites | z = 1
        self.point1 = Point(self.all_points, undo_translate((1, 1)))
        self.point2 = Point(self.all_points, undo_translate((-1, 1)))
        self.point3 = Point(self.all_points, undo_translate((1, -1)))
        self.point4 = Point(self.all_points, undo_translate((-1, -1)))

        # z = 2

        self.point5 = Point(self.all_points, undo_translate((1, 1)), 1.001)
        self.point6 = Point(self.all_points, undo_translate((-1, 1)), 1.001)
        self.point7 = Point(self.all_points, undo_translate((1, -1)), 1.001)
        self.point8 = Point(self.all_points, undo_translate((-1, -1)), 1.001)

    def run(self):
        while self.running:
            dt = self.clock.tick(60) / 1000

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
            
            # points
            self.all_points.update(dt)

            # draw
            self.display_surface.fill((0,0,0))

            # draw points
            self.all_points.draw(self.display_surface)

            pygame.display.flip()

        pygame.quit()

class Point(pygame.sprite.Sprite):
    def __init__(self, groups, pos, z = 1, color=(250,50,50)):
        super().__init__(groups)
        self.image = pygame.Surface((40, 40))
        self.rect = self.image.get_frect(center = pos)
        self.image.fill(color)
        self.pos = pos
        self.z = z

    def update(self, dt):
        self.z += 0.001 * dt
        self.pos = translate(self.pos)
        self.pos = ((self.pos[0]) / self.z, (self.pos[1]) / self.z)
        self.pos = undo_translate(self.pos)
        self.rect.center = self.pos
    
def translate(pos) -> tuple:
    x = ((pos[0]/(1280/2)) - 1)
    y = ((pos[1]/(720/2)) - 1) * -1
    return (x,y)

def undo_translate(pos) -> tuple:
    x = (pos[0]+1) * (1280/2)
    y = (2-(pos[1]+1)) * (720/2)
    return(x,y)

game = Game()
game.run()