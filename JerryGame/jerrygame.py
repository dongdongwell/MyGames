from turtle import *
from gamebase import line
from random import randrange, choice

balloons = []
color_select = [
    'black', 'green', 'red', 'blue', 
    'pink', 'purple', 'yellow', 'orange',
    'light green', 'light blue', 'dark blue'
    ]
size = 50

# x, y 为鼠标坐标 a, b为圆心坐标
def distance(x, y, a, b):
    return ((a - x) ** 2 + (b - y) ** 2) ** 0.5

# 点击气球
def tap(x, y):
    global balloons

    for i in range(len(balloons)):
        if distance(x, y, balloons[i][0], balloons[i][1]) < (size / 2):
            balloons.pop(i)
            return
def draw():
    global balloons, size

    clear()
    for i in range(1, len(balloons) + 1):
        theballx = balloons[-i][0]
        thebally = balloons[-i][1]
        line(theballx, thebally, theballx, thebally - size * 1.5)
        up()
        goto(theballx, thebally)
        # 画圆 (大小-直径 颜色)
        dot(size, balloons[-i][2])
        balloons[-i][1] += 1
    update()

def gameLoop():
    global size, color_select, balloons

    if (randrange(1, 51) == 1):
        x = randrange(-200 + size, 200 - size)
        colors = choice(color_select)
        balloons.append([x, -200 - size, colors])
    draw()
    ontimer(gameLoop, 20)

if __name__ == '__main__':
    setup(420, 420, 0, 0)
    hideturtle()
    tracer(False)

    listen()
    onscreenclick(tap)

    gameLoop()
    done()