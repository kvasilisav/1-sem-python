import pygame
from pygame.draw import *


pygame.init()

FPS=30
screen = pygame.display.set_mode((400, 400))
screen.fill((255,255,255))

#fizionomiya
circle(screen, (253, 232, 103), (200,200), 150)
#eyes
circle(screen, (223, 109, 75), (140, 125), 30)
circle(screen, (223, 109, 75), (260, 125), 20)
circle(screen, (0,0,0), (140, 125), 10)
circle(screen, (0,0,0), (260, 125), 6.67)
#mouth
rect(screen, (0,0,0), (130, 270, 140, 30))
#brovi(ya ne iz anglii)
polygon(screen, (0,0,0), [(60, 40), (60, 80), (185, 100), (185, 80)])
polygon(screen, (0,0,0), [(320, 30), (320, 80), (215, 100), (215, 80)])

pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True


pygame.quit()          
