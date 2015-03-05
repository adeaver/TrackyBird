import pygame, random
import Rectangle

class PipeObstacle():

    counter = 0

    def __init__(self, screenx, screeny):
        PipeObstacle.counter += 1
        self.count = PipeObstacle.counter
        print self.count
        self.screenx = screenx
        self.screeny = screeny
        self.posx = screenx+40 + (self.screenx/2 * (self.count-1))
        self.width = 30
        self.posy = random.randrange(screeny-300, int(screeny * (7.0/8.0)))
        self.height = screeny-self.posy

    def draw(self, screen):
        pygame.draw.rect(screen, pygame.Color(255,0,0), (self.posx, self.posy, self.width, self.height))
        pygame.draw.rect(screen, pygame.Color(255, 0, 0), (self.posx, 0, self.width, self.posy-200))

    def update(self, delta_t):
        self.posx -= (200 * delta_t)

        if(self.posx < -1 * self.width):
            self.posx = self.screenx
            self.posy = random.randrange(self.screeny-300, int(self.screeny * (7.0/8.0)))
            self.height = self.screeny-self.posy

    def get_x(self):
        print self.posx

    def rect(self):
        return [Rectangle.Rectangle(self.posx, self.posy, self.width, self.height), Rectangle.Rectangle(self.posx, 0, self.width, self.posy-200)]
