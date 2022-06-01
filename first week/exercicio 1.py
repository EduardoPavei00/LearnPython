import random
import turtle as t


t.pensize(2)
t.speed(1)


def variaçao():
    amplitude = random.random() * 35 + 1
    sentido = random.choice([1, -1])
    return amplitude * sentido


def bolsa():
    y = random.randint(-200, 200)
    x = 0
    z = 0

    for _ in range(200):
        ajuste = variaçao()
        y = y + ajuste


        if ajuste >= 0:
            t.color("green")
            t.goto(x, y)
        else:
            t.color("red")
            t.goto(x, y)
        z = ajuste + ajuste
        x = x + 4
    return z


print(bolsa())
bolsa()


