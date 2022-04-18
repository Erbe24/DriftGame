import pygame, time, math, random
from cgi import test
from tkinter import Y
import pygame, random
from sys import exit
pygame.init()

GRASS = pygame.image.load("vscodeproj/img/grass.jpg")
GRASS = pygame.transform.scale(GRASS, (900,900))
TRACK = pygame.image.load("vscodeproj/img/track.png")

TRACK_BORDER = pygame.image.load("vscodeproj/img/track-border.png")
FINISH = pygame.image.load("vscodeproj/img/finish.png")


# player car
RED_CAR = pygame.image.load("vscodeproj/img/red-car.png")
RED_CAR = pygame.transform.scale(RED_CAR, (20,40))
CAR_dir = pygame.transform.rotate(RED_CAR,0)
RED_CAR_x = 40
RED_CAR_y = 424
RED_CAR_rect = RED_CAR.get_rect(center = (RED_CAR_x,RED_CAR_y))#pygame.Rect() #left, top, width, height
RED_CAR_vel = 5

WIDTH, HEIGHT = TRACK.get_width(), TRACK.get_height()
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
# grass = pygame.display.set_mode((gWIDTH,gHEIGHT))
pygame.display.set_caption("Drift Game!")

FPS = 60

run = True
clock = pygame.time.Clock()

# angle = 0

# def is_90(angle):
#     if angle == 90:
#         pass


# def CAR_pos(CAR_image,CAR_rect):
#     WIN.blit(CAR_image,CAR_rect)



while run:
    clock.tick(FPS)

    WIN.blit(GRASS, (0, 0))
    WIN.blit(TRACK, (0, 0))
    # WIN.blit(RED_CAR,RED_CAR_rect)
    
    # pygame.draw.rect(RED_CAR,, RED_CAR_rect,10)
    
    # WIN.blit(RED_CAR,(RED_CAR_x,RED_CAR_y)) #starting pos of cars

   
    

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
         pygame.quit()
         exit()
        if event.type == pygame.MOUSEBUTTONDOWN: #click anywhere program closes
         print("--PROGRAM TERMINATED--")
         exit()
    
        # if event.type == pygame.MOUSEMOTION: #for finding positions its good
        #     print(event.pos) 

    # CAR_image = pygame.transform.rotate(RED_CAR, angle)
    userInput = pygame.key.get_pressed()

    if userInput [pygame.K_w]:
        RED_CAR_rect.y -= RED_CAR_vel
        CAR_dir = pygame.transform.rotate(RED_CAR,0)
        if userInput [pygame.K_SPACE]:
            RED_CAR_rect.y -= RED_CAR_vel +3

    if userInput [pygame.K_s]:
        RED_CAR_rect.y += RED_CAR_vel
        CAR_dir = pygame.transform.rotate(RED_CAR,180)
        if userInput [pygame.K_SPACE]:
            RED_CAR_rect.y += RED_CAR_vel +3
            

    if userInput [pygame.K_d]:
        RED_CAR_rect.x += RED_CAR_vel
        CAR_dir = pygame.transform.rotate(RED_CAR, -90)
        if userInput [pygame.K_d and pygame.K_w]:
            CAR_dir = pygame.transform.rotate(RED_CAR, -50)
        if userInput [pygame.K_SPACE]:
            RED_CAR_rect.x += RED_CAR_vel +3

    if userInput [pygame.K_a]:
        RED_CAR_rect.x -= RED_CAR_vel
        CAR_dir = pygame.transform.rotate(RED_CAR, 90)
        if userInput [pygame.K_a and pygame.K_w]:
            CAR_dir = pygame.transform.rotate(RED_CAR, 50)
        if userInput [pygame.K_SPACE]:
            RED_CAR_rect.x -= RED_CAR_vel +3
        
    WIN.blit(CAR_dir,RED_CAR_rect)
    # playerInput(userInput) # userinput to move car
    # # CAR_pos(RED_CAR,RED_CAR_rect)
    
    

    

    pygame.time.delay(1) # bigger number slower update
    pygame.display.update()

pygame.quit()