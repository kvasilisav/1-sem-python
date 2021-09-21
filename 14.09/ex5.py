import turtle

turtle.shape('turtle')
turtle.forward(20)
turtle.left(90)
turtle.forward(20)
turtle.left(90)
turtle.forward(20)
turtle.left(90)
turtle.forward(20)
for x in range(1,9):
	turtle.penup()
	turtle.forward(20)
	turtle.pendown()
	turtle.left(90)
	turtle.forward(20+20*x)
	turtle.left(90)
	turtle.forward(20+20*2*x)
	turtle.left(90)
	turtle.forward(20+20*2*x)
	turtle.left(90)
	turtle.forward(20+20*2*x)
	turtle.left(90)
	turtle.forward(20*x)
	turtle.right(90)
	
	

