import pygame
import random
from math import cos, pi

class Bird():
    """ Represents the player in the game (the Tracky Bird) """
    def __init__(self,screenx, screeny):
        """ Initialize a Tracky bird at the specified position
            pos_x, pos_y """
        self.up = pygame.image.load("./images/bird_up.png")
        self.up = pygame.transform.scale(self.up, (50,50))

        self.up_up = pygame.image.load("./images/bird_up.png")
        self.up_up = pygame.transform.scale(self.up_up, (50,50))    
        
        self.normal = pygame.image.load("./images/bird_wing_down.png")
        self.normal = pygame.transform.scale(self.normal, (50, 50))

        self.deg10 = pygame.image.load("./images/bird_10_degrees.png")
        self.deg10 = pygame.transform.scale(self.deg10, (50, 50))

        self.deg20 = pygame.image.load("./images/bird_20_degrees.png")
        self.deg20 = pygame.transform.scale(self.deg20, (50, 50))


        self.deg30 = pygame.image.load("./images/bird_30_degrees.png")
        self.deg30 = pygame.transform.scale(self.deg30, (50, 50))

        self.deg60 = pygame.image.load("./images/bird_60_degrees.png")
        self.deg60 = pygame.transform.scale(self.deg60, (50, 50))

        self.deg90 = pygame.image.load("./images/bird_90_degrees.png")
        self.deg90 = pygame.transform.scale(self.deg90, (50, 50))
    
        self.images = { 0:self.up, 1:self.up_up, 2:self.normal, 3:self.deg10, 4:self.deg20,
                        5:self.deg30, 6:self.deg60, 7:self.deg90}

        self.image = self.images[2]

        self.pos_x = screenx/2
        self.pos_y = screeny/2
        self.death_height = int(screeny * (7.0/8.0))
        self.width = 50  # replace with width of sprite
        self.height = 50 # replace with height of sprite
        self.v_x = 0
        self.v_y = 0
        self.jumping = 0

    def get_drawables(self):
        """ get the drawables that makeup the Flappy Bird Player """
        return [DrawableSurface(self.image,
                self.image.get_rect().move(self.pos_x, self.pos_y))]

    def draw(self, surface):
        surface.blit(self.image, (self.pos_x, self.pos_y))

    def reset(self, screenx, screeny):
        self.pos_x = screenx/2
        self.pos_y = screeny/2
        self.width = 50  # replace with width of sprite
        self.height = 50 # replace with height of sprite
        self.v_x = 0
        self.v_y = 0
        self.accel = 9.8
        self.jumper = 0

    def update(self, delta_t):
        """ update the flappy bird's position """
        if self.jumping:
            self.v_y = -350
            self.jumping = False            
        else:
            self.v_y += 30 #falling acceleration

        self.pos_x += self.v_x*delta_t
        self.pos_y += self.v_y*delta_t
        
        if self.v_y < 0 and self.image is self.images[1]: 
            self.image = self.images[0]
        elif self.v_y < 0 and self.image is self.images[0]: 
            self.image = self.images[1]
        elif self.v_y < 50: self.image = self.images[2]
        elif self.v_y < 100: self.image = self.images[3]
        elif self.v_y < 150: self.image = self.images[4]    
        elif self.v_y < 200: self.image = self.images[5]
        elif self.v_y < 300: self.image = self.images[6]
        elif self.v_y < 500: self.image = self.images[7]

    def check_loss(self):
        return (self.pos_y > self.death_height - 30)

    def collision(self, rectangles):
        bird_rect = self.get_rect()
        for rect in rectangles:
            if rect.contains(bird_rect):
                return True
            elif (rect.left <= self.pos_x \
                  and rect.right >= self.pos_x \
                  and self.pos_y <= 0):
                return True
        return False

    def get_rect(self):
        return Rectangle(self.pos_x, self.pos_y, self.width, self.height)

    def flap(self):
        """ cause the bird to accelerate upwards (negative y direction) """
        # self.v_y = -200
        if(self.pos_y > 40):
            self.jumping = True

class PipeObstacle():

    counter = 0

    def __init__(self, screenx, screeny):
        PipeObstacle.counter += 1
        self.gap = 200
        self.count = PipeObstacle.counter
        self.screenx = screenx
        self.screeny = screeny
        self.posx = screenx + 300 + (((self.screenx)/2+60) * (self.count-1))
        self.width = 120
        self.posy = random.randrange(screeny-300, int(screeny * (7.0/8.0)))
        self.height = screeny-self.posy
        self.image = pygame.image.load('./images/pipe_body.png')
        self.image = pygame.transform.scale(self.image,
                          (self.width, self.height))
        self.top = pygame.transform.scale(self.image, (self.width + 50, 30))
        
        self.reflection = pygame.transform.scale(self.image,
                          (self.width, self.posy-self.gap))


    def draw(self, screen):
        screen.blit(self.image, (self.posx, self.posy))
        screen.blit(self.reflection, (self.posx, 0))
        screen.blit(self.top, (self.posx - 25, self.posy))
        screen.blit(self.top, (self.posx - 25, self.posy - self.gap))
    
    def reset(self):
        self.posx = self.screenx + 300 + (((self.screenx)/2+60) * (self.count-1))
        self.width = 120
        self.posy = random.randrange(self.screeny-300, int(self.screeny * (7.0/8.0)))
        self.height = self.screeny-self.posy
        self.image = pygame.transform.scale(self.image, (self.width, self.height))
        self.reflection = pygame.transform.scale(self.image, (self.width, self.posy-self.gap))

    def update(self, delta_t):
        self.posx -= (200 * delta_t)

        if(self.posx < -1 * self.width):
            self.posx = self.screenx
            self.posy = random.randrange(self.screeny-300, int(self.screeny * (7.0/8.0)))
            self.height = self.screeny-self.posy
            self.image = pygame.transform.scale(self.image, (self.width, self.height))
            self.reflection = pygame.transform.scale(self.image, (self.width, self.posy-self.gap))

    def rect(self):
        return [Rectangle(self.posx, self.posy, self.width, self.height),
                Rectangle(self.posx, 0, self.width, self.posy-200)]

class Rectangle():

    def __init__(self, left, top, width, height):
        self.top = top
        self.left = left
        self.width = width
        self.height = height
        self.right = left+width
        self.bottom = top + height

    def contains(self, rect):
        if(rect.right >= self.left and rect.left <= self.left+self.width):
            if(rect.top <= self.top+self.height and rect.bottom >= self.top):
                return True

        return False
