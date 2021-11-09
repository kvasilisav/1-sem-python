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
		self.x = 40
		self.y = 450
		self.r = 10
		self.vx = 0
		self.vy = 0
		self.color = BLACK
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
		
	def hittestt(self, obj):
			if ((self.x - obj.x) ** 2 + (self.y - obj.y) ** 2) < (obj.r+10)**2:
				return True
			else:
				return False
		
	def hittestr(self, obj):
		if (obj.x - self.x) <= (10) and (obj.y + 80) > self.y and obj.x < self.y :
			return True
		else:
			return False


class Gun:
	def __init__(self, screen):
		self.screen = screen
		self.f2_power = 10
		self.f2_on = 0
		self.an = 0
		self.color = GREY
		self.x = 20
		self.y = 450

	def fire2_start(self, event):
		self.f2_on = 1

	def fire2_end(self, event):
		global balls, bullet
		bullet += 1
		new_ball = Ball(self.screen)
		new_ball.r += 5
		if event.pos[0]-new_ball.x == 0:
			self.an = 0.785
		else:
			self.an = math.atan2((event.pos[1]-new_ball.y), (event.pos[0]-new_ball.x))
		new_ball.vx = self.f2_power * math.cos(self.an)
		new_ball.vy = - self.f2_power * math.sin(self.an)
		balls.append(new_ball)
		self.f2_on = 0
		self.f2_power = 10

	def targetting(self, event):
		if event:
			if event.pos[0] - 20== 0:
				self.an = 0.785
			else:
				self.an = math.atan2((event.pos[1] - 450), (event.pos[0] - 20))
		if self.f2_on:
			self.color = RED
		else:
			self.color = GREY
			
			

	def draw(self):
		pygame.draw.polygon(screen, BLACK, ((self.x, self.y), (self.x + math.sin(self.an)*7, self.y - math.cos(self.an)*7), (self.x + math.cos(self.an)*self.f2_power + math.sin(self.an)*7, self.y + math.sin(self.an)*self.f2_power- math.cos(self.an)*7),(self.x + math.cos(self.an)*self.f2_power, self.y + math.sin(self.an)*self.f2_power)))

	def power_up(self):
		if self.f2_on:
			if self.f2_power < 100:
				self.f2_power += 1
			self.color = RED
		else:
			self.color = GREY

class Target(Ball):
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
		
	def new_target(self):
		self.x = random.randint(600, 780)
		self.y = random.randint(300, 550)
		self.r = random.randint(2, 50)
		self.live = 1

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
		
		
class Tank(Gun):
	def __init__(self, screen):
		self.screen = screen
		self.f2_power = 10
		self.f2_on = 0
		self.an = 1
		self.color = GREY
		self.x = 20
		self.y = 450
		self.points = 0
		

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
print('привет! добро пожаловать на игру. напишите число игроков')
player = int(input())
out = open('result.txt' ,'w')
name = [] # list of players' name
k = 0
for k in range (player):
	bullet = 0
	score=0
	scorer=0
	balls = []
	targ = []
	rectangles = []
	balls_am = 0
	number_of_targets = 6
	number_of_rectangles = 4
	
	print ('Как вас зовут?')
	name.append(input())
	
	clock = pygame.time.Clock()
	gun = Gun(screen)

	for n in range(number_of_targets):
		targ.append(Target(screen))

	for n in range(number_of_rectangles):
		rectangles.append(Rectangle(screen))

	t = 600
	all_died = False

	notfinished = True


	while  notfinished:
		t += -1
		if t == 0:
			notfinished =False
		all_died = True
		screen.fill(WHITE)
		gun.draw()
		for target in targ:
			if target.live != 0:
				target.draw()
				target.move()
				all_died = False
		for r in rectangles:
			if r.live != 0:
				r.draw()
				r.move()
				all_died=False
		for b in balls:
			b.draw()
		if(t > 0):
			MYFONT = pygame.font.SysFont('cmmi10', 30)
			textsurface = MYFONT.render( 'Мячики: ' + str(score) + ', палочки' + str(scorer), False, GREEN)
			screen.blit(textsurface, (100, 10))
		pygame.display.update()
		if all_died:
			balls_am = len(balls)
			balls = []
			gun.points += 10
			for i in range(len(targ)):
				targ[i] = Target(screen)
		pygame.display.update()
		clock.tick(FPS)
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				notfinished = False
			elif event.type == pygame.MOUSEBUTTONDOWN:
				gun.fire2_start(event)
			elif event.type == pygame.MOUSEBUTTONUP:
				gun.fire2_end(event)
			elif event.type == pygame.MOUSEMOTION:
				gun.targetting(event)

		for b in balls:
			b.move()
			for target in targ:
				if b.hittestt(target) and target.live:
					target.live = 0
					b.x=10
					b.y=10
					b.vx=0
					b.vy=0
					b.g=0
					score += 1
					targ.append(Target(screen))
					balls_am = len(balls)
			for r in rectangles:
				if b.hittestr(r) and r.live:
					r.live=0
					scorer += 1
					rectangles.append(Rectangle(screen))
					balls_am=len(balls)
		gun.power_up()
	print ('Результаты', name[k],' Мячики:',score,' Палочки :',scorer, file = out)

out.close()
pygame.quit()
