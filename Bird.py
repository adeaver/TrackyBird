import pygame
from math import cos, pi
import Rectangle

jumping_steps = 20

class Bird():
    """ Represents the player in the game (the Tracky Bird) """
    def __init__(self,screenx, screeny):
        """ Initialize a Tracky bird at the specified position
            pos_x, pos_y """
        self.pos_x = screenx/2
        self.pos_y = screeny/2
        self.death_height = int(screeny * (7.0/8.0))
        self.width = 30 # replace with width of sprite
        self.height = 30 # replace with height of sprite
        self.v_x = 0
        self.v_y = 0
        self.jumping = 0
        # TODO: don't depend on relative path
        #self.image = pygame.image.load('images/bird_wing_up.png')
        #self.image.set_colorkey((255,255,255))

    def get_drawables(self):
        """ get the drawables that makeup the Flappy Bird Player """
        return [DrawableSurface(self.image, self.image.get_rect().move(self.pos_x, self.pos_y))]

    def draw(self, surface):
        pygame.draw.circle(surface, pygame.Color(0,100,0), (int(self.pos_x), int(self.pos_y)), 30)

    def update(self, delta_t):
        """ update the flappy bird's position """
        if self.jumping > 5:
            self.v_y = -2000 * cos((self.jumping/jumping_steps)*2*pi)
            self.jumping -=1
        elif self.jumping > 0:
            self.v_y += 20
            self.jumping -= 1
        else:
            # self.v_y = delta_t*400 # this is gravity in pixels / s^2
            self.v_y = 200

        self.pos_x += self.v_x*delta_t
        self.pos_y += self.v_y*delta_t

    def check_loss(self):
        return (self.pos_y > self.death_height - 30)

    def collision(self, rectangles):
        bird_rect = self.get_rect()
        for rect in rectangles:
            if rect.contains(bird_rect):
                return True
            elif (rect.get_left() <= self.pos_x and rect.get_right() >= self.pos_x and self.pos_y <= 0):
                return True
        return False

    def get_rect(self):
        return Rectangle.Rectangle(self.pos_x, self.pos_y, self.width, self.height)

    def flap(self):
        """ cause the bird to accelerate upwards (negative y direction) """
        # self.v_y = -200
        self.jumping = jumping_steps
