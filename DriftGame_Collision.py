import pygame
import time
import math
import random
from cgi import test
from tkinter import Y
import pygame
import random
from sys import exit
pygame.init()

GRASS = pygame.image.load("imgs\\grass.jpg")
GRASS = pygame.transform.scale(GRASS, (900, 900))
TRACK = pygame.image.load("imgs\\track.png")

TRACK_BORDER = pygame.image.load("imgs\\track_border_2.jpg")
FINISH = pygame.image.load("imgs\\finish.png")
EXPLOSION = pygame.image.load("imgs\\explosion.png")
EXPLOSION = pygame.transform.scale(EXPLOSION, (40, 40))

RED_CAR = pygame.image.load("imgs\\red-car.png")
RED_CAR = pygame.transform.scale(RED_CAR, (20, 40))
RED_CAR_x = 40
RED_CAR_y = 424
# pygame.Rect() #left, top, width, height
RED_CAR_rect = RED_CAR.get_rect(center=(RED_CAR_x, RED_CAR_y))
RED_CAR_vel = 5

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

    WIN.blit(GRASS, (0, 0))
    WIN.blit(TRACK, (0, 0))

    # pygame.draw.rect(RED_CAR,, RED_CAR_rect,10)

    # WIN.blit(RED_CAR,(RED_CAR_x,RED_CAR_y)) #starting pos of cars

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            print("--PROGRAM TERMINATED--")
            exit()

        # if event.type == pygame.MOUSEMOTION: #for finding positions its good
        #     print(event.pos)

    userInput = pygame.key.get_pressed()
    if userInput[pygame.K_w]:
        RED_CAR_rect.y -= RED_CAR_vel
        if userInput[pygame.K_SPACE]:
            RED_CAR_rect.y -= RED_CAR_vel + 3

    if userInput[pygame.K_s]:
        RED_CAR_rect.y += RED_CAR_vel
        if userInput[pygame.K_SPACE]:
            RED_CAR_rect.y += RED_CAR_vel + 3

    if userInput[pygame.K_d]:
        RED_CAR_rect.x += RED_CAR_vel
        if userInput[pygame.K_SPACE]:
            RED_CAR_rect.x += RED_CAR_vel + 3
    if userInput[pygame.K_a]:
        RED_CAR_rect.x -= RED_CAR_vel
        if userInput[pygame.K_SPACE]:
            RED_CAR_rect.x -= RED_CAR_vel + 3

    WIN.blit(RED_CAR, RED_CAR_rect)

    if RED_CAR_rect.colliderect(wall_rect_1) or RED_CAR_rect.colliderect(wall_rect_2) or RED_CAR_rect.colliderect(wall_rect_3) or RED_CAR_rect.colliderect(wall_rect_4) or RED_CAR_rect.colliderect(wall_rect_5) or RED_CAR_rect.colliderect(wall_rect_6) or RED_CAR_rect.colliderect(wall_rect_7) or RED_CAR_rect.colliderect(wall_rect_8) or RED_CAR_rect.colliderect(wall_rect_9) or RED_CAR_rect.colliderect(wall_rect_10) or RED_CAR_rect.colliderect(wall_rect_11) or RED_CAR_rect.colliderect(wall_rect_12) or RED_CAR_rect.colliderect(wall_rect_13):
        WIN.blit(EXPLOSION, RED_CAR_rect)
        RED_CAR_rect.x = RED_CAR_x
        RED_CAR_rect.y = RED_CAR_y
    
    pygame.time.delay(10)
    pygame.display.update()

pygame.quit()
