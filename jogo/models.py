import turtle as t
from turtle import TurtleScreen
from enum import Enum

# === Definições utilizadas ===


# Create Border
class ScreenBorder:
    size: float

    def __init__(self, screen: TurtleScreen):
        self.size = min(screen.window_width(), screen.window_height()) * 0.8
        self.__pen = t.Turtle()
        self.__pen.speed(0)
        self.__pen.penup()
        self.__pen.setposition(-self.size / 2, -self.size / 2)
        self.__pen.pendown()
        self.__pen.pensize(3)
        for side in range(4):
            self.__pen.forward(self.size)
            self.__pen.left(90)
        self.__pen.hideturtle()


class PaddleDirection(Enum):
    RIGHT = 1
    LEFT = 2


class Paddle:
    __min_x: int
    __max_x: int
    __dx: int = 20

    def __init__(self, start_x, start_y, min_x, max_x):
        self.__min_x = min_x
        self.__max_x = max_x
        self.__pen = t.Turtle()
        self.__pen.speed(0)
        self.__pen.shape("square")
        self.__pen.color("black")
        self.__pen.shapesize(stretch_wid=1, stretch_len=6)
        self.__pen.penup()
        self.__pen.goto(start_x, start_y)

    def x(self):
        return self.__pen.xcor()

    def y(self):
        return self.__pen.ycor()

    def move(self, direction: PaddleDirection):
        if direction == PaddleDirection.RIGHT:
            positions = self.__dx
        elif direction == PaddleDirection.LEFT:
            positions = -self.__dx

        def undo():
            self.__pen.setx(self.__pen.xcor() - positions)

        self.__pen.setx(self.__pen.xcor() + positions)
        if self.__pen.xcor() < self.__min_x:
            undo()
        if self.__pen.xcor() > self.__max_x:
            undo()

    def paddle_right(self):
        self.move(PaddleDirection.RIGHT)

    def paddle_left(self):
        self.move(PaddleDirection.LEFT)


class Ball:
    """
    Ball of circle shape
    """

    def __init__(self):
        # TODO ball size
        self.__pen = t.Turtle()
        self.__pen.speed(3)
        self.__pen.shape("circle")
        self.__pen.color("blue")
        self.__pen.penup()
        self.__pen.goto(0, 0)
        # TODO E se eu quiser que a bola caminhasse em uma direcao diferente?
        self.dx = 5  # direita
        self.dy = -5 # baixo

    def x(self):
        return self.__pen.xcor()

    def y(self):
        return self.__pen.ycor()

    def move(self):
        self.__pen.setx(self.__pen.xcor() + self.dx)
        self.__pen.sety(self.__pen.ycor() + self.dy)



