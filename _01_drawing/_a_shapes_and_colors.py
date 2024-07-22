import turtle


window = turtle.Screen()
window.bgcolor('white')

# This code makes a new Turtle. Pick a new name for the turtle
deniz = turtle.Turtle()

# Make your turtle's shape 'turtle', .shape('turtle')
deniz.shape('turtle')
# Set your turtle's speed using .speed(2)
deniz.speed(10)
# Set your turtle's color using .color('green') and .pencolor('blue')
deniz.color('grey')
deniz.pencolor('blue')
# Move your turtle forward using .forward(100)
deniz.forward(150)
# TEST    Did your turtle move forward?
# yes my turtle moved forward
# Move your turtle left or right using .left(90) or .right(90)
deniz.left(90)
# Now put the forward and left/right code into a for loop to repeat 4 times.
# TEST    Did your turtle draw a square?
deniz.forward(150)
deniz.left(90)
deniz.forward(150)
deniz.left(90)


# Move your turtle to a new place on the screen using .goto(x, y)
# x=0 and y=0 is the center of the screen
deniz.goto(-100, -100)
deniz.begin_fill()
# Have your turtle draw a circle using .circle(radius, steps=30)
deniz.circle(20, steps=30)
# TEST    Did your turtle draw a circle?
deniz.end_fill()
# Add color to your shape by adding .begin_fill() before drawing the circle
# and .end_fill() below

# Draw 3 more shapes with different fill colors!
deniz.goto(100, 100)
deniz.begin_fill()
for i in range (3):
    deniz.forward(150)
    deniz.left(60)
deniz.end_fill()

deniz.goto(100, -100)
deniz.begin_fill()
deniz.circle(100, steps=100)
deniz.end_fill()

# ===================== DO NOT EDIT THE CODE BELOW ============================
turtle.done()
