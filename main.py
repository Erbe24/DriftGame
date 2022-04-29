import pygame, time, math, random
from cgi import test
from tkinter import Y
import pygame, random
from sys import exit
from pygame import mixer
pygame.init()

"""
Images
taken from https://github.com/techwithtim/Pygame-Car-Racer/tree/main/tutorial1-code
You will have to setup the directory for the images (pygame.image.load())
"""

GRASS = pygame.image.load("imgs\\grass.jpg")
GRASS = pygame.transform.scale(GRASS, (900,900))
TRACK = pygame.image.load("imgs\\track.png")

TRACK_BORDER = pygame.image.load("imgs\\track-border.png")
FINISH = pygame.image.load("imgs\\finish.png")
EXPLOSION = pygame.image.load("imgs\\explosion.png")
EXPLOSION = pygame.transform.scale(EXPLOSION, (40, 40))

#Background Music
mixer.music.load("Sounds\\Background-Song.wav")
mixer.music.play(-1) #-1 loops the sound

# player car taken from https://github.com/techwithtim/Pygame-Car-Racer/tree/main/tutorial1-code
RED_CAR = pygame.image.load("imgs\\red-car.png")
RED_CAR = pygame.transform.scale(RED_CAR, (20,40))
CAR_dir = pygame.transform.rotate(RED_CAR,0)

#Car position
RED_CAR_x = 40
RED_CAR_y = 424
RED_CAR_rect = RED_CAR.get_rect(center = (RED_CAR_x,RED_CAR_y))#pygame.Rect() #left, top, width, height
RED_CAR_vel = 5

#Borders for the track 
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
pygame.display.set_caption("Drift Game!")

FPS = 60

run = True
clock = pygame.time.Clock()


while run:
    clock.tick(FPS)

    WIN.blit(GRASS, (0, 0))  # makes images visible in window, and position of image
    WIN.blit(TRACK, (0, 0))
   



    for event in pygame.event.get():
        if event.type == pygame.QUIT:
         pygame.quit()
         exit()
        if event.type == pygame.MOUSEBUTTONDOWN: #click anywhere program closes
         print("--PROGRAM TERMINATED--")
         exit()
    
      
    userInput = pygame.key.get_pressed()

    #create mixer channels in order to overlap sounds
    channel1 = pygame.mixer.Channel(0)


    if userInput [pygame.K_w]:
        RED_CAR_rect.y -= RED_CAR_vel # depending on input, RED_CAR_vel will subtract or add from x or y
        CAR_dir = pygame.transform.rotate(RED_CAR,0) # rotation
        if userInput [pygame.K_LSHIFT]: # boost
            RED_CAR_rect.y -= RED_CAR_vel +3 # depending on input, RED_CAR_vel will subtract or add from x or y
        #Makes sound of car accelerating
        Acceleration_Sound = mixer.Sound("Sounds\\Acceleration.wav")
        pygame.mixer.Sound.play(Acceleration_Sound)
 
    if userInput [pygame.K_s]:
        RED_CAR_rect.y += RED_CAR_vel
        CAR_dir = pygame.transform.rotate(RED_CAR,180)
        if userInput [pygame.K_LSHIFT]:
            RED_CAR_rect.y += RED_CAR_vel +3
        
        Acceleration_Sound = mixer.Sound("Sounds\\Acceleration.wav")
        pygame.mixer.Sound.play(Acceleration_Sound)
            

    if userInput [pygame.K_d]:
        RED_CAR_rect.x += RED_CAR_vel
        CAR_dir = pygame.transform.rotate(RED_CAR, -90)
        if userInput [pygame.K_d and pygame.K_w]:
            CAR_dir = pygame.transform.rotate(RED_CAR, -50)
        elif userInput [pygame.K_d and pygame.K_s]:
            CAR_dir = pygame.transform.rotate(RED_CAR, -140)
        if userInput [pygame.K_LSHIFT]:
            RED_CAR_rect.x += RED_CAR_vel +3

        Acceleration_Sound = mixer.Sound("Sounds\\Acceleration.wav")
        pygame.mixer.Sound.play(Acceleration_Sound)

    if userInput [pygame.K_a]:
        RED_CAR_rect.x -= RED_CAR_vel
        CAR_dir = pygame.transform.rotate(RED_CAR, 90)
        if userInput [pygame.K_a and pygame.K_w]:
            CAR_dir = pygame.transform.rotate(RED_CAR, 50)
        elif userInput [pygame.K_a and pygame.K_s]:
            CAR_dir = pygame.transform.rotate(RED_CAR, 140)
        if userInput [pygame.K_LSHIFT]:
            RED_CAR_rect.x -= RED_CAR_vel +3
        
        Acceleration_Sound = mixer.Sound("Sounds\\Acceleration.wav")
        pygame.mixer.Sound.play(Acceleration_Sound)


    WIN.blit(CAR_dir,RED_CAR_rect)
    # playerInput(userInput) # userinput to move car
    # # CAR_pos(RED_CAR,RED_CAR_rect)
    
    #Wrecks car if it collides with track border
    if RED_CAR_rect.colliderect(wall_rect_1) or RED_CAR_rect.colliderect(wall_rect_2) or RED_CAR_rect.colliderect(wall_rect_3) or RED_CAR_rect.colliderect(wall_rect_4) or RED_CAR_rect.colliderect(wall_rect_5) or RED_CAR_rect.colliderect(wall_rect_6) or RED_CAR_rect.colliderect(wall_rect_7) or RED_CAR_rect.colliderect(wall_rect_8) or RED_CAR_rect.colliderect(wall_rect_9) or RED_CAR_rect.colliderect(wall_rect_10) or RED_CAR_rect.colliderect(wall_rect_11) or RED_CAR_rect.colliderect(wall_rect_12) or RED_CAR_rect.colliderect(wall_rect_13):
        WIN.blit(EXPLOSION, RED_CAR_rect)
        RED_CAR_rect.x = RED_CAR_x
        RED_CAR_rect.y = RED_CAR_y


        Explosion_Sound = mixer.Sound("Sounds\\Crash.wav")
        channel1.play(Explosion_Sound) #Calls a channel to overlap acceleration sound
    

    pygame.time.delay(1) # bigger number slower update
    pygame.display.update()

pygame.quit()
