import turtle
import math

turtle.shape('turtle')

def be(n, R):
	turtle.left(180-90*(n-2)/n)
	for i in range(n):
		turtle.forward(R*2*math.sin(math.pi/n))
		turtle.left(180-180*(n-2)/n)
		
for x in range(3, 11):
	be(x, (x-1)*20)
	turtle.right(180-90*(x-2)/x)
	turtle.penup()
	turtle.forward(20)
	turtle.pendown()
