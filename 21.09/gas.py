from random import randint
import turtle


number_of_turtles = 30
steps_of_time_number = 100

turtle.penup()
turtle.speed(1000)
turtle.goto(-200, -200)
turtle.width(5)
turtle.pendown()
turtle.goto(-200, 200)
turtle.goto(200, 200)
turtle.goto(200, -200)
turtle.goto(-200, -200)
turtle.hideturtle()


pool = [turtle.Turtle(shape='circle') for i in range(number_of_turtles)]
for unit in pool:
    unit.penup()
    unit.speed(randint(190, 210))
    unit.goto(randint(-199, 199), randint(-199, 199))
    unit.left(randint(1, 360))


for i in range(steps_of_time_number):
	for unit in pool:
		unit.forward(2)
		x = unit.xcor()
		y = unit.ycor()
		angle = unit.heading()
		if y>=190 or y<=-190:
			unit.setheading(360-angle)
		if x>=190 or x<=-190:
			unit.setheading(520 - angle)
