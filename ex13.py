import turtle
turtle.shape('turtle')

def l(n):
	for x in range (360):
		turtle.forward(n/100)
		turtle.left(1)


def d(n):
	for x in range (180):
		turtle.forward(n/100)
		turtle.left(1)

turtle.color("green")
turtle.begin_fill()		
l(100)
turtle.end_fill()

turtle.penup()
turtle.goto(30, 80)
turtle.pendown()
turtle.color("black")
turtle.begin_fill()		
l(10)
turtle.end_fill()

turtle.penup()
turtle.goto(-30, 80)
turtle.pendown()
turtle.color("black")
turtle.begin_fill()		
l(10)
turtle.end_fill()

turtle.penup()
turtle.goto(0, 70)
turtle.pendown()
turtle.right(90)
turtle.width(5)
turtle.forward(20)


turtle.penup()
turtle.goto(-30, 40)
turtle.pendown()
turtle.color("red")
turtle.width(5)
d(50)
