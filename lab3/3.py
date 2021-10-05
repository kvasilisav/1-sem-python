import pygame
from pygame.draw import *
import math as m


pygame.init()

FPS=30
screen = pygame.display.set_mode((900, 400))

def draw_trava(surface, color):
	rect(surface, color, (30, 230, 800, 120))
	
def draw_nebo(surface, color):
	rect(surface, color, (30, 40, 800, 190))

def draw_cloud(surface, x, y, color):
	circle(surface, color, (x, y), 20)
	circle(surface, color, (x+30, y), 20)
	circle(surface, color, (x+5, y-20), 20)
	circle(surface, color, (x+25, y-30), 20)
	circle(surface, color, (x+40, y-25), 20)
	circle(surface, color, (x+60, y-10), 20)
	
def draw_domik(surface, x, y, k, color1, color2, color3, color4):
	rect(surface, color1, (x, y, 190*k, 120*k))
	rect(surface, color2, (x, y, 190*k, 120*k), 2)
	polygon(surface ,color3, [(x, y), (x+190*k, y), (x+95*k, y-60*k)])
	polygon(surface, color2, [(x, y), (x+190*k, y), (x+95*k, y-60*k)], 1) 
	rect(surface, color4, (x+65*k, y+35*k, 60*k, 45*k))
	rect(surface, color2, (x+65*k, y+35*k, 60*k, 45*k),3)
	
def draw_sun (surface, x, y, color):
	circle(screen, color, (x, y), 30)

def draw_derevo (surface, x, y, k, color1, color2, color3):
	rect(surface, color1, (x+12, y, 8*k, 60*k))
	circle(surface, color2, (x, y), 15*k)
	circle(surface, color2, (x+4, y-15), 15*k)
	circle(surface, color2, (x+34, y-20), 15*k)
	circle(surface, color3, (x+5, y), 15*k)
	circle(surface, color3, (x+25, y), 15*k)
	circle(surface, color3, (x+15, y-25), 15*k)
	circle(surface, color3, (x+20, y+5), 15*k)
	circle(surface, color3, (x+15, y-15), 15*k)
	circle(surface, color2, (x+30, y), 15*k)
	
#fon
draw_trava(screen, (92,206,113))
draw_nebo(screen, (153,194,225))

#oblachka	
draw_cloud(screen, 250, 100, (255,255,255))
draw_cloud(screen, 450, 130, (255,255,255))
draw_cloud(screen, 630, 110, (255,255,255))
	
	
#domiki
draw_domik(screen, 110, 190, 1, (136,63,27), (0,0,0), (210,76,93),(136,155,201))
draw_domik(screen, 510, 220, 0.85, (136,63,27), (0,0,0), (210,76,93),(136,155,201))

#sun
draw_sun(screen, 90, 90, (253,232,103))
  
#derevia
draw_derevo(screen, 325, 185, 1, (160,142,106), (136,165,107), (136,155,107))
draw_derevo(screen, 725, 165, 2, (160,142,106), (136,165,107), (136,155,107))

pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True


pygame.quit()  
