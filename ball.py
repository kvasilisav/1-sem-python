import math
import random
from random import choice
from random import randint
import time 


import pygame


FPS = 30

RED = 0xFF0000
BLUE = 0x0000FF
YELLOW = 0xFFC91F
GREEN = 0x00FF00
MAGENTA = 0xFF03B8
CYAN = 0x00FFCC
BLACK = (0, 0, 0)
WHITE = 0xFFFFFF
GREY = 0x7D7D7D
GAME_COLORS = [RED, BLUE, YELLOW, GREEN, MAGENTA, CYAN]

WIDTH = 800
HEIGHT = 600

class Ball:
	def __init__(self, screen):
		self.screen = screen
		self.color = choice(GAME_COLORS)
		self.x = random.randint(20, 780)
		self.y = random.randint(50, 550)
		self.r = random.randint(20, 100)
		self.vx = randint(-10, 10)
		self.vy = randint(-10, 10)
		self.points = 0
		self.live = 1
		self.g=1

	def move(self):
		if self.x + self.vx > screen.get_width() - 50 and self.vx > 0:
			self.vx = -self.vx
		if self.x + self.vx < 50 and self.vx < 0:
			self.vx = -self.vx
		if self.y + self.vy < 50 and self.vy > 0:
			self.vy = - self.vy
		if self.y + self.vy > screen.get_height() - 50 and self.vy < 0:
			self.vy = - self.vy
		self.x = self.x + self.vx
		self.y = self.y - self.vy
		self.vy = self.vy - self.g

	def draw(self):
		pygame.draw.circle(screen, self.color, (self.x, self.y), self.r)
		

class Rectangle:
	def __init__(self, screen):
		self.screen = screen
		self.color = choice(GAME_COLORS)
		self.x = random.randint(20, 780)
		self.y = random.randint(50, 550)
		self.vx = randint(-20, 20)
		self.vy = randint(-20, 20)
		self.points = 0
		self.live = 1

	def move(self):
		g = 1.5
		k = 1
		time = 1
		for t in range(time):
			self.vy +=g
			if (self.x<=20+1 or self.x>=WIDTH - 20 -1):
				self.vx = -k*self.vx
				self.vy *= k
				self.x += self.vx
				self.y = self.y + self.vy + g/2
			elif (self.y<=80+2 or self.y>=HEIGHT - 80 -2):
				self.vy = -k*self.vy
				self.vx *= k
				self.x += self.vx
				self.y = self.y + self.vy + g/2
			else:
				self.x += self.vx
				self.y = self.y + self.vy + g/2
	def draw(self):
		pygame.draw.rect(screen, self.color, (self.x, self.y, 20, 80))
		
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
print('привет! добро пожаловать на игру. напишите число игроков')
player = int(input())
out = open('result.txt' ,'w')
name = [] # list of players' name
k = 0
for k in range (player):
	score=0
	balls = []
	rectangles = []
	balls_am = 0
	number_of_balls = 10
	number_of_rectangles = 8
	print ('Как вас зовут?')
	name.append(input())
	
	clock = pygame.time.Clock()
	
	for n in range(number_of_balls):
		balls.append(Ball(screen))

	for n in range(number_of_rectangles):
		rectangles.append(Rectangle(screen))

	t = 600

	notfinished = True

	while  notfinished:
		t += -1
		if t == 0:
			notfinished =False
		screen.fill(WHITE)
		for r in rectangles:
			if r.live != 0:
				r.draw()
				r.move()
		for b in balls:
			if b.live != 0:
				b.draw()
				b.move()
		pygame.display.update()
		clock.tick(FPS)
		for event in pygame.event.get():
			if event.type == pygame.MOUSEBUTTONDOWN:
				for b in balls: 
					x1, y1 = event.pos
					if (b.x- x1)**2 + (b.y - y1)**2 <= b.r**2:
						score += 1
						b.live = 0 
						
				for r in rectangles:
					x3, y3 = event.pos
					if  x3  < r.x + 20 and x3 > r.x and y3 < r.y + 80  and y3 > r.y:
						score += 5
						r.live = 0
						
	print ('Результаты', name[k],' Мячики:',score,' Палочки :',scorer, file = out)

out.close()
pygame.quit()
