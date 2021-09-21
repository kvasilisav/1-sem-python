import turtle
turtle.shape('turtle')

def d(n):
	for x in range (180):
		turtle.forward(n/100)
		turtle.left(1)
turtle.right(90)
for i in range (10):
	d(50)
	d(10)	
	
