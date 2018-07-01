import turtle

painter = turtle.Turtle()
painter.pensize(20)

for _ in range(3):
	painter.forward(100)
	painter.left(90)
	painter.forward(100)
	painter.left(90)
	painter.forward(100)
	painter.left(90)
	painter.forward(100)

	painter.right(90)
	painter.forward(100)
	painter.right(90)
	painter.forward(100)
	painter.right(90)
	painter.forward(100)
	painter.right(90)
	painter.forward(100)

turtle.done()