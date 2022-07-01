# Import required library
import turtle as t

# Create screen
sc = t.Screen()
sc.title("Pong game")
sc.bgcolor("white")
sc.setup(width=1000, height=600)


# Create Border
mypen = t.Turtle()
mypen.speed(0)
mypen.penup()
mypen.setposition(-400,-400)
mypen.pendown()
mypen.pensize(3)
for side in range(4):
    mypen.forward(800)
    mypen.left(90)
mypen.hideturtle()



# Left paddle
t.speed(0)
t.shape("square")
t.color("black")
t.shapesize(stretch_wid=1, stretch_len=6)
t.penup()
t.goto(0, -200)

# Ball of circle shape
hit_ball = t.Turtle()
hit_ball.speed(40)
hit_ball.shape("circle")
hit_ball.color("blue")
hit_ball.penup()
hit_ball.goto(0, 0)
hit_ball.dx = 5
hit_ball.dy = -10



# Functions to move paddle

def paddle_right():
    x = t.xcor()
    x += 20
    t.setx(x)


def paddle_left():
    x = t.xcor()
    x -= 20
    t.setx(x)


# Keyboard bindings
sc.listen()
sc.onkeypress(paddle_right, "Right")
sc.onkeypress(paddle_left, "Left")

while True:
    sc.update()

    hit_ball.setx(hit_ball.xcor() + hit_ball.dx)
    hit_ball.sety(hit_ball.ycor() + hit_ball.dy)

    if hit_ball.xcor() > 400 or hit_ball.xcor() < -400:
        hit_ball.dx *= -1

    if hit_ball.ycor() > 400 or hit_ball.ycor() < -400:
        hit_ball.dy *= -1





    # Paddle ball collision
