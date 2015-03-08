import pygame
from math import cos, pi
import Rectangle

jumping_steps = 20

class Bird():
    """ Represents the player in the game (the Tracky Bird) """
    def __init__(self,screenx, screeny):
        """ Initialize a Tracky bird at the specified position
            pos_x, pos_y """
        self.image = pygame.image.load("./images/bird.gif")
        self.image = pygame.transform.scale(self.image, (50, 50))
        self.pos_x = screenx/2
        self.pos_y = screeny/2
        self.death_height = int(screeny * (7.0/8.0))
        self.width = 50 # replace with width of sprite
        self.height = 50 # replace with height of sprite
        self.v_x = 0
        self.v_y = 0
        self.accel = 9.8
        self.jumper = 0
        # TODO: don't depend on relative path
        #self.image = pygame.image.load('images/bird_wing_up.png')
        #self.image.set_colorkey((255,255,255))

    def get_drawables(self):
        """ get the drawables that makeup the Flappy Bird Player """
        return [DrawableSurface(self.image, self.image.get_rect().move(self.pos_x, self.pos_y))]

    def draw(self, surface):
        surface.blit(self.image, (self.pos_x, self.pos_y))

    def reset(self, screenx, screeny):
        self.pos_x = screenx/2
        self.pos_y = screeny/2
        self.width = 50 # replace with width of sprite
        self.height = 50 # replace with height of sprite
        self.v_x = 0
        self.v_y = 0
        self.accel = 9.8
        self.jumper = 0

    def update(self, delta_t):
        """ update the flappy bird's position """
        accel = 30
        self.v_y += accel
        if self.jumper:
            self.v_y = -70*self.jumper
            self.jumper -= 1


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
        if(self.pos_y > 40):
            self.jumper = 10
