import pygame
from pygame.draw import *
import math as m


pygame.init()

FPS=30
screen = pygame.display.set_mode((900, 400))

#trava
rect(screen, (92,206,113), (30, 230, 800, 120))
#nebo
rect(screen, (153, 194, 225), (30, 40, 800, 190))

#cloud1
circle(screen, (255,255,255), (250, 100), 20)
circle(screen, (255,255,255), (280, 100), 20)
circle(screen, (255,255,255), (255, 80), 20)
circle(screen, (255,255,255), (275, 70), 20)
circle(screen, (255,255,255), (290, 75), 20)
circle(screen, (255,255,255), (310, 90), 20)
#cloud2
circle(screen, (255,255,255), (450, 130), 20)
circle(screen, (255,255,255), (480, 130), 20)
circle(screen, (255,255,255), (455, 110), 20)
circle(screen, (255,255,255), (475, 100), 20)
circle(screen, (255,255,255), (490, 105), 20)
circle(screen, (255,255,255), (510, 120), 20)
#cloud3
circle(screen, (255,255,255), (630, 110), 25)
circle(screen, (255,255,255), (660, 110), 25)
circle(screen, (255,255,255), (635, 90), 25)
circle(screen, (255,255,255), (655, 80), 25)
circle(screen, (255,255,255), (670, 85), 25)
circle(screen, (255,255,255), (690, 100), 25)

#sun
circle(screen, (253, 232, 103), (90, 90), 30)

#domik1
rect(screen, (136, 63, 27), (110, 190, 190, 120))
rect(screen, (0,0,0), (110, 190, 190, 120), 2)
polygon(screen,(210, 76, 93), [(110, 190), (300, 190), (205, 130)])
polygon(screen,(0,0,0), [(110, 190), (300, 190), (205, 130)], 1) 
rect(screen, (136, 155, 201), (175, 225, 60, 45))
rect(screen, (0,0,0), (175, 225, 60, 45),3)
#domik2
rect(screen, (136, 63, 27), (510, 210, 160, 100))
rect(screen, (0,0,0), (510, 210, 160, 100), 1) 
polygon(screen, (210, 76, 93), [(510,210), (670, 210), (590, 160)])
polygon(screen,(0,0,0),[(510,210), (670, 210), (590, 160)],2)
rect(screen, (136, 155, 201), (565, 240, 50, 40))
rect(screen, (0,0,0), (565, 240, 50, 40), 1)
 
#tree1
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
#tree2
rect(screen, (160,142,106), (737, 165, 15, 110))
circle(screen, (136, 165, 107), (725, 165), 30)
circle(screen, (136, 165, 107), (729, 150), 30)
circle(screen, (136, 145, 107), (759, 145), 30)
circle(screen, (136, 155, 107), (730, 160), 30)
circle(screen, (136, 155, 107), (750, 160), 30)
circle(screen, (136, 155, 107), (740, 140), 30)
circle(screen, (136, 155, 107), (745, 170), 30)
circle(screen, (136, 155, 107), (740, 150), 30)
circle(screen, (136, 165, 107), (755, 165), 30)

pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True


pygame.quit()  
