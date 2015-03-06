import sys, pygame, time
import classes
from movement_detect import *

tracker = Movement_Track()

pygame.init()
pygame.font.init()
pygame.mixer.init()

#pygame.mixer.music.load("boat.wav")
#pygame.mixer.music.play(-1)

font = pygame.font.SysFont("ubuntumono",100)

screen = pygame.display.set_mode([860, 640])
pygame.display.set_caption('TrackyBird')

screenx, screeny = screen.get_size()

background = pygame.Surface(screen.get_size())
background = background.convert()
background.fill((0, 191, 255))

grass_height = int(screeny/7.0)

grass = pygame.Surface((screenx, grass_height))
grass.fill((124, 252, 0))

grassy = int(screeny * (7.0/8.0))

background.blit(grass, (0, grassy))
screen.blit(background, (0, 0))
counter = 0
update = time.time()
pipe = PipeObstacle.PipeObstacle(screenx, screeny)
pipe2 = PipeObstacle.PipeObstacle(screenx, screeny)
bird = Bird.Bird(screenx, screeny)

lost = False
track = True

while True:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            # if event.key == pygame.K_SPACE:
            #     bird.flap()
            #     print "Flap!"
            if event.key == pygame.K_q:
                sys.exit()
        elif event.type == pygame.QUIT:
            sys.exit()

    if tracker.Movement():
        bird.flap()
        track = False
        counter = -1
        print "Flap!"

    if(track == False):
        counter += 1
        if(counter == 10):
            track = True


    delta_t = time.time() - update
    update = time.time()

    background.fill((0, 191, 255))
    background.blit(grass, (0, grassy))
    screen.blit(background, (0, 0))

    rects = pipe.rect() + pipe2.rect()

    pipe.draw(background)
    pipe.update(delta_t)
    pipe2.draw(background)
    pipe2.update(delta_t)
    bird.draw(background)
    bird.update(delta_t)

    if(bird.check_loss() or bird.collision(rects)):
        lost = True

    if(lost):
        msg = font.render('You Lost!', 0, pygame.Color(000,000,000))
        background.blit(msg, (0,48))
        lost = False

    screen.blit(background, (0, 0))
    pygame.display.update()
