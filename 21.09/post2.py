import turtle
import math as m

turtle.shape('turtle')

with open('sh.txt', 'r') as f:
	lines=f.readlines()
nums = []
for line in lines:
	nums.append(eval(line.rstrip()))

l=(1, 4, 1, 7, 0, 0) #вот сюда вводить индекс

for num in l:
	for i in nums[num]:
		if i[0]==1:
			turtle.pendown()
		else:
			turtle.penup()
		turtle.left(i[1])
		turtle.forward(i[2])
	turtle.penup()
	turtle.forward(60)

