#Import the Turtle module
import turtle

#Setup the screen for our painting
screen = turtle.Screen()
screen.setup(800, 700)

#Create a circle "fucntion"
circle = turtle.Turtle()
circle.shape('circle')
circle.color('red')
circle.speed('fastest')
circle.up()

#Create a square "function"
square = turtle.Turtle()
square.shape('square')
square.color('green')
square.speed('fastest')
square.up()

#Function to draw the star
#We will represent the star as a circle to save space
#and for a better design
def draw_star():
    circle.goto(0, 280)
    circle.stamp()

#Function to print squares
def print_sq(x, y):
    square.goto(x, - y + 280)
    square.stamp()
    square.goto(-x, - y + 280)
    square.stamp()

#Function to print a circle
def print_cl(color, x, y):
    circle.color(color)
    circle.goto(-x, -y + 280)
    circle.stamp()
    circle.goto(x, -y + 280)
    circle.stamp()

def draw_tree():
    k = 0
    for i in range(1, 17):
        y = 30 * i
        for j in range(i - k):
            x = 30 * j
            print_sq(x, y)
        
        if i % 4 == 0:
            x = 30 * (j + 1)
            print_cl('red', x, y)
            k += 2

        if i % 4 == 3:
            x = 30 * (j + 1)
            print_cl('yellow', x, y)

def draw_trunc():
    square.color('brown')
    for i in range(17, 20):
        y = 30 * i
        for j in range(3):
            x = 30 * j
            print_sq(x, y)

draw_star()
draw_tree()
draw_trunc()

turtle.done()
