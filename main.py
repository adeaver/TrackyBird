import sys, pygame, time
import classes
from movement_detect import *

tracker = Movement_Track()

pygame.init()
pygame.font.init()
pygame.mixer.init()

#pygame.mixer.music.load("boat.wav")
#pygame.mixer.music.play(-1)

score = 0

font = pygame.font.Font("./fonts/04B_19__.TTF",100)

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
pipe = classes.PipeObstacle(screenx, screeny)
pipe2 = classes.PipeObstacle(screenx, screeny)
bird = classes.Bird(screenx, screeny)

lost = False
play = False
exit = False
track = True

distance = 0;

title_image = pygame.image.load('./images/trackylogo.gif')
by_image = pygame.image.load('./images/bylogo.gif')

while play != True:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                play = True
                pipe.reset()
                pipe2.reset()

    delta_t = time.time() - update
    update = time.time()

    background.fill((0, 191, 255))
    background.blit(grass, (0, grassy))

    pipe.draw(background)
    pipe.update(delta_t)
    pipe2.draw(background)
    pipe2.update(delta_t)

    background.blit(title_image, (screenx/2-201, 10))
    background.blit(by_image, (screenx/2-342, screeny-100))

    screen.blit(background, (0, 0))
    pygame.display.update()

while True:
    while lost != True:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                     bird.flap()
                if event.key == pygame.K_q:
                    sys.exit()
            elif event.type == pygame.QUIT:
                sys.exit()

        if tracker.Movement():
            bird.flap()
            track = False
            counter = -1
        #Prevents bird from flapping again for 10 frames after a flap
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

        distance += delta_t * 200

        if(distance > screenx/2 + 60):
            score+=1
            distance = 0

        score_msg = font.render(str(score), 0, pygame.Color(000,000,000))
        background.blit(score_msg, (screenx/2, 48))

        if(lost):
            msg = font.render('You Lost!', 0, pygame.Color(000,000,000))
            background.blit(msg, (screenx/3,screeny-100))

        screen.blit(background, (0, 0))
        pygame.display.update()

    while True: 
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    lost = False
                    print "Restart Pressed"
                    break
                elif event.key == pygame.K_q:
                    sys.exit()

        if(lost == False):
            break

    if(lost == False):
        pipe.reset()
        pipe2.reset()
        score = 0
        distance = 0
        bird.reset(screenx, screeny)
        pygame.display.update()
