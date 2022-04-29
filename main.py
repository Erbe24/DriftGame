from contextlib import redirect_stderr
import pygame, time, math, random
from cgi import test
from tkinter import Y
import pygame, random
from sys import exit
pygame.init()

"""
Images
taken from https://github.com/techwithtim/Pygame-Car-Racer/tree/main/tutorial1-code

You will have to setup the directory for the images (pygame.image.load())
"""
GRASS = pygame.image.load("vscodeproj/img/grass.jpg")# NOTE: setup the directory for imgs
GRASS = pygame.transform.scale(GRASS, (900,900))
TRACK = pygame.image.load("vscodeproj/img/track.png")# NOTE: setup the directory for imgs

TRACK_BORDER = pygame.image.load("vscodeproj/img/track-border.png")# NOTE: setup the directory for imgs
FINISH = pygame.image.load("vscodeproj/img/finish.png")# NOTE: setup the directory for imgs
EXPLOSION = pygame.image.load("vscodeproj/img/explosion.png")# NOTE: setup the directory for imgs
EXPLOSION = pygame.transform.scale(EXPLOSION, (40, 40))


# player car taken from https://github.com/techwithtim/Pygame-Car-Racer/tree/main/tutorial1-code
RED_CAR = pygame.image.load("vscodeproj/img/red-car.png") # NOTE: setup the directory for imgs
RED_CAR = pygame.transform.scale(RED_CAR, (20,40))
CAR_dir = pygame.transform.rotate(RED_CAR,0)
"""
car position
"""
RED_CAR_x = 40 
RED_CAR_y = 424
RED_CAR_rect = RED_CAR.get_rect(center = (RED_CAR_x,RED_CAR_y))#pygame.Rect() #left, top, width, height
RED_CAR_vel = 4 # car velocity

"""
Creates the track's border so that the car doesn't just go through the barriers.
"""
wall_rect_1 = pygame.Rect(0, 0, 30, 900)
wall_rect_2 = pygame.Rect(105, 124, 50, 645)
wall_rect_3 = pygame.Rect(235, 0, 35, 414)
wall_rect_4 = pygame.Rect(350, 124, 430, 125)
wall_rect_5 = pygame.Rect(350, 349, 55, 420)
wall_rect_6 = pygame.Rect(155, 499, 195, 270)
wall_rect_7 = pygame.Rect(30, 0, 830, 44)
wall_rect_8 = pygame.Rect(860, 0, 40, 900)
wall_rect_9 = pygame.Rect(485, 329, 375, 35)
wall_rect_10 = pygame.Rect(405, 444, 300, 45)
wall_rect_11 = pygame.Rect(705, 444, 75, 325)
wall_rect_12 = pygame.Rect(490, 574, 135, 275)
wall_rect_13 = pygame.Rect(30, 849, 830, 51)

WIDTH, HEIGHT = TRACK.get_width(), TRACK.get_height()
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
# grass = pygame.display.set_mode((gWIDTH,gHEIGHT))
pygame.display.set_caption("Drift Game!")

FPS = 60

run = True
clock = pygame.time.Clock()




while run:
    clock.tick(FPS)

    WIN.blit(GRASS, (0, 0)) # makes images visible in window, and position of image
    WIN.blit(TRACK, (0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
         pygame.quit()
         exit()
        if event.type == pygame.MOUSEBUTTONDOWN: #click anywhere program to kill the program
         print("--PROGRAM TERMINATED--")
         exit()
    
        # if event.type == pygame.MOUSEMOTION: #for finding positions its good
        #     print(event.pos) 

    # CAR_image = pygame.transform.rotate(RED_CAR, angle)
    """
    User inputs: (standard wasd movement)
    """
    userInput = pygame.key.get_pressed()

    if userInput [pygame.K_w]:
        RED_CAR_rect.y -= RED_CAR_vel # depending on input, RED_CAR_vel will subtract or add from x or y
        CAR_dir = pygame.transform.rotate(RED_CAR,0) # rotation
        if userInput [pygame.K_LSHIFT]: # boost
            RED_CAR_rect.y -= RED_CAR_vel +3 # depending on input, RED_CAR_vel will subtract or add from x or y

    if userInput [pygame.K_s]:
        RED_CAR_rect.y += RED_CAR_vel
        CAR_dir = pygame.transform.rotate(RED_CAR,180)
        if userInput [pygame.K_LSHIFT]:
            RED_CAR_rect.y += RED_CAR_vel +3
            

    if userInput [pygame.K_d]:
        RED_CAR_rect.x += RED_CAR_vel
        CAR_dir = pygame.transform.rotate(RED_CAR, -90)
        if userInput [pygame.K_d and pygame.K_w]:
            CAR_dir = pygame.transform.rotate(RED_CAR, -50)
        elif userInput [pygame.K_d and pygame.K_s]:
            CAR_dir = pygame.transform.rotate(RED_CAR, -140)
        if userInput [pygame.K_LSHIFT]:
            RED_CAR_rect.x += RED_CAR_vel +3

    if userInput [pygame.K_a]:
        RED_CAR_rect.x -= RED_CAR_vel
        CAR_dir = pygame.transform.rotate(RED_CAR, 90)
        if userInput [pygame.K_a and pygame.K_w]:
            CAR_dir = pygame.transform.rotate(RED_CAR, 50)
        elif userInput [pygame.K_a and pygame.K_s]:
            CAR_dir = pygame.transform.rotate(RED_CAR, 140)
        if userInput [pygame.K_LSHIFT]:
            RED_CAR_rect.x -= RED_CAR_vel +3
        
    WIN.blit(CAR_dir,RED_CAR_rect) 
    
    """
    Resets red car to starting position if collision occurs
    """
    if RED_CAR_rect.colliderect(wall_rect_1) or RED_CAR_rect.colliderect(wall_rect_2) or RED_CAR_rect.colliderect(wall_rect_3) or RED_CAR_rect.colliderect(wall_rect_4) or RED_CAR_rect.colliderect(wall_rect_5) or RED_CAR_rect.colliderect(wall_rect_6) or RED_CAR_rect.colliderect(wall_rect_7) or RED_CAR_rect.colliderect(wall_rect_8) or RED_CAR_rect.colliderect(wall_rect_9) or RED_CAR_rect.colliderect(wall_rect_10) or RED_CAR_rect.colliderect(wall_rect_11) or RED_CAR_rect.colliderect(wall_rect_12) or RED_CAR_rect.colliderect(wall_rect_13):
        WIN.blit(EXPLOSION, RED_CAR_rect)
        RED_CAR_rect.x = RED_CAR_x
        RED_CAR_rect.y = RED_CAR_y
    

    

    pygame.time.delay(1) # bigger number slower update
    pygame.display.update()

pygame.quit()
