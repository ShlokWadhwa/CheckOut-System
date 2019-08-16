# Shlok Wadhwa, Project, CIS345 T/Th 10:30-11:45

# file to create logo using turtle
import turtle

# setting up turtle
turtle.setup(700, 500)
window = turtle.Screen()
window.reset()
window.bgcolor('teal')

# setting up the 2 boxes
pen = turtle.Turtle()
pen.speed(0)
pen.up()
pen.setposition(-300, 0)
pen.down()
pen.forward(200)
pen.setheading(90)
pen.forward(200)
pen.setheading(180)
pen.forward(200)
pen.setheading(270)
pen.forward(200)
pen.up()

pen.setposition(0, 0)
pen.setheading(90)
pen.down()
pen.forward(200)
pen.setheading(0)
pen.forward(200)
pen.setheading(270)
pen.forward(200)
pen.setheading(180)
pen.forward(200)

# writing the 'K'
pen.pencolor('white')
pen.up()
pen.setposition(-250, 175)
pen.setheading(270)
pen.down()
pen.forward(150)
pen.up()
pen.setheading(90)
pen.forward(75)
pen.right(45)
pen.down()
pen.forward(100)
pen.up()
pen.backward(100)
pen.right(90)
pen.down()
pen.forward(100)

# Writing the S
pen.up()
pen.setposition(50, 175)
pen.down()
pen.setheading(0)
pen.forward(75)
pen.up()
pen.backward(75)
pen.setheading(270)
pen.down()
pen.forward(75)
pen.setheading(0)
pen.forward(75)
pen.setheading(270)
pen.forward(75)
pen.setheading(180)
pen.forward(75)
pen.up()

pen.goto(-50, -50)


pen.up()
# creating a star
pen.setposition(-25, 100)
pen.down()
for i in range(5):
    pen.forward(50)
    pen.right(144)

pen.up()
pen.setposition(-400, -400)


turtle.done()
