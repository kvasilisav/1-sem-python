import turtle

turtle.shape('circle')

turtle.speed(1000)
turtle.width(5)
turtle.penup()
turtle.goto(500, -200)
turtle.pendown()
turtle.goto(-200, -200)
turtle.width(1)
turtle.speed(1)

x=-200
y=-200
vx=10
vy=70
g=10
b=0.001
dt=0.1

while x<=400 and vx >= 0:
	while y >= -200:
		turtle.goto(x, y)
		ay=b*(vy)**2
		ax=b*(vx)**2
		if vy >= 0:
			a=g+ay
		elif vy <= 0:
			a=g-ay	
		vy -= a * dt
		y += vy*dt - a*dt**2/2
		ax=b*(vx)**2
		vx -= ax*dt
		x += vx*dt
	y=-200
	vy=-vy
	
