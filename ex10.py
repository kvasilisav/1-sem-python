import turtle
turtle.shape('turtle')

def l(n):
	for x in range (360):
		turtle.forward(n/100)
		turtle.left(1)
def r(n):
	for x in range (360):
		turtle.forward(n/100)
		turtle.right(1)
		
for x in range (3):
	l(50)
	r(50)
	turtle.left(60)
