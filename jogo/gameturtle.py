# Import required library
from jogo.models import Paddle, ScreenBorder, Ball, PaddleDirection
import turtle as t

class PaddleGame():
    sc = t.Screen()
    active: bool
    # TODO maybe game has an end?
    lives = 3

    def __init__(self):
        self.sc.title("Pong game")
        self.sc.bgcolor("white")
        self.sc.setup(width=1000, height=600)

        # Create Border
        self.border = ScreenBorder(self.sc)

        # Create Paddle
        self.paddle = Paddle(0, -200, -self.border.size/2, self.border.size/2)

        # Create Ball
        self.ball = Ball()

        # Keyboard bindings
        self.sc.listen()
        self.sc.onkeypress(self.paddle.paddle_right, "Right")
        self.sc.onkeypress(self.paddle.paddle_left, "Left")


    def detect_ball_collision(self):
        if self.ball.x() > (self.border.size/2) or self.ball.x() < (-self.border.size/2):
            self.ball.dx *= -1

        if self.ball.y() > (self.border.size/2) or self.ball.y() < -(self.border.size/2):
            self.ball.dy *= -1

        # TODO paddle colision

    def update(self):
        self.sc.update()
        self.ball.move()
        self.detect_ball_collision()

    def start(self):
        self.active = True
