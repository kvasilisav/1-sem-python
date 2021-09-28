import pygame
from pygame.draw import *
import math as m


pygame.init()

FPS=30
screen = pygame.display.set_mode((400, 400))

#trava
rect(screen, (92,206,113), (30, 230, 350, 120))
#nebo
rect(screen, (153, 194, 225), (30, 40, 350, 190))
#cloud
circle(screen, (255,255,255), (250, 100), 20)
circle(screen, (255,255,255), (280, 100), 20)
circle(screen, (255,255,255), (255, 80), 20)
circle(screen, (255,255,255), (275, 70), 20)
circle(screen, (255,255,255), (290, 75), 20)
circle(screen, (255,255,255), (310, 90), 20)
#sun
circle(screen, (253, 232, 103), (90, 90), 30)
#domik
rect(screen, (136, 63, 27), (110, 190, 190, 120))
rect(screen, (0,0,0), (110, 190, 190, 120), 2)
polygon(screen,(210, 76, 93), [(110, 190), (300, 190), (205, 130)])
polygon(screen,(0,0,0), [(110, 190), (300, 190), (205, 130)], 1) 
rect(screen, (136, 155, 201), (175, 225, 60, 45))
rect(screen, (0,0,0), (175, 225, 60, 45),3)
#tree
rect(screen, (160,142,106), (337, 185, 8, 60))
circle(screen, (136, 165, 107), (325, 185), 15)
circle(screen, (136, 165, 107), (329, 170), 15)
circle(screen, (136, 145, 107), (359, 165), 15)
circle(screen, (136, 155, 107), (330, 180), 15)
circle(screen, (136, 155, 107), (350, 180), 15)
circle(screen, (136, 155, 107), (340, 160), 15)
circle(screen, (136, 155, 107), (345, 190), 15)
circle(screen, (136, 155, 107), (340, 170), 15)
circle(screen, (136, 165, 107), (355, 185), 15)

pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True


pygame.quit()  
