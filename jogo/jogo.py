import turtle
import random

# wn = Window
wn = turtle.Screen()
wn.bgcolor('black')
wn.title('Freetown')

class Line(turtle.Turtle):

    def __init__(self):
        turtle.Turtle.__init__(self)
        self.penup()
        self.hideturtle()
        self.speed(0)
        self.color('red')
        self.pensize(5)

    def draw_line(self):
        self.penup()
        self.goto(-200, -200)
        self.pendown()
        self.goto(-200,200)

class Player(turtle.Turtle):


    def __init__(self):
        turtle.Turtle.__init__(self)
        self.score = 0
        self.penup()
        self.speed(0)
        self.shape('triangle')
        self.color('green')
        self.speed = 1

    def move(self):
        self.forward(self.speed)
    def turnleft(self):
        self.left(30)
    def turnright(self):
        self.right(30)
    def increasespeed(self):
        self.speed +=1
    def decreasespeed(self):
        self.speed -=1


def isCollision2(t1, t2):
    if abs (t1.xcor () - t2.xcor ()) < 20 :
        a = t1.ycor ()
        b = t2.ycor ()
        if a < b and a > b - 400 :
            return True
    else:
        return False

#Class instance
player = Player()
line = Line()

#Draw the line
line.draw_line()

#Keyboard bindings
turtle.listen()
turtle.onkey(player.turnleft, 'a')
turtle.onkey(player.turnright, 'd')
turtle.onkey(player.increasespeed, 'w')
turtle.onkey(player.decreasespeed,'s')

while True:
    player.move()
    if isCollision2(player,line):
        player.setheading(360 - (player.heading () + 180))