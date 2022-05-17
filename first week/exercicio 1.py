import random
import turtle as t
from unittest import result

t.pensize(2)
t.speed(1)

def bolsa():
    x = 0
    for _ in range(200):
        y = random.randint(-200, 200)
        if y >= 0:
            t.color("green")
            t.goto(x, y)
        else:
            t.color("red")
            t.goto(x, y)
        x = x + 20
        z = y + y
    return print(z)


bolsa()


