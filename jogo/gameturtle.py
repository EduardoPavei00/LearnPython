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
        self.ball = Ball(0, 0, +3, +4)

        # Keyboard bindings
        self.sc.listen()
        self.sc.onkeypress(self.paddle.paddle_right, "Right")
        self.sc.onkeypress(self.paddle.paddle_left, "Left")

    def detect_ball_in_border(self):
        if self.ball.x() > (self.border.size/2) or self.ball.x() < (-self.border.size/2):
            self.ball.dx *= -1

        if self.ball.y() > (self.border.size/2):
            self.ball.dy *= -1

        elif self.ball.y() < -(self.border.size/2):
            self.ball.reset()
            self.ball.dy *= -1
            self.lives -= 1

    def detect_ball_in_paddle(self):
        pad_x_min = self.paddle.x() - (self.paddle.width/2)
        pad_x_max = self.paddle.x() + (self.paddle.width/2)
        pad_y = self.paddle.y() + self.paddle.height
        ball_x = self.ball.x()
        ball_y = self.ball.y() # + ? (raio, diametro, zero)...
        
        if pad_x_min <= ball_x <= pad_x_max and ball_y <= pad_y:
            self.ball.dy *= -1


    def update(self):
        self.sc.update()
        self.ball.move()
        self.detect_ball_in_border()
        self.detect_ball_in_paddle()

    def start(self):
        self.active = True
