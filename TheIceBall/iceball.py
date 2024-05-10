from turtle import *
from random import random, choice

player = [0, -140]
ball = [0, 140]
direction = [choice([-2, -1, 1, 2]), choice([-2, -1])]
ball_velocity = 1.5
ball_size = 10
bounce_times = 0

def move(distance):
    if (player[0] >=290 - 70 and distance > 0) or (player[0] <= -300 and distance < 0):
        player[0] += 0
    else:
        player[0] += distance

def bounce():
    global bounce_times

    ballX = ball[0]
    ballY = ball[1]
    if ballX <= -300 or ballX >= 290: 
        direction[0] = -direction[0]
    elif ballY >= 150:
        direction[1] = -direction[1]
    elif ballY <= -140 + 10 + 5 and player[0] <= ballX <= player[0] + 70:
        direction[1] = -direction[1]
        bounce_times += 1

def outside():
    if ball[1] < -140 + 10 + 5 and (player[0] > ball[0] or ball[0] > player[0] + 70):
        return True
    return False

def rectagle(x, y, width, height):
    up()
    goto(x, y)
    down()
    color('black')
    begin_fill()
    for i in range(2):
        forward(width)
        left(90)
        forward(height)
        left(90)
    end_fill()

def score():
    up()
    goto(280, 130)
    down()
    color('black')
    write(bounce_times, font = ("Consolas", 10, "bold"))

def draw():
    clear()
    up()
    goto(ball[0], ball[1])
    down()
    dot(ball_size, 'red')
    rectagle(player[0], player[1], 70, 10)
    score()
    update()

def gameover():
    up()
    goto(-125, 0)
    down()
    color('red')
    write("GAME OVER!", font = ("Consolas", 40, "normal"))

    up()
    goto(-125, 50)
    down()
    color('red')
    write("YOUR SCORE:   " + str(bounce_times), font = ("Consolas", 20, "normal"))

def gameLoop():
    bounce()
    ball[0] += direction[0] * ball_velocity
    ball[1] += direction[1] * ball_velocity
    draw()
    if outside():
        gameover()
        return
    ontimer(gameLoop, 30)

if __name__ == '__main__':
    setup(620, 320, 200, 0)
    hideturtle()
    tracer(False)
    title('ICE BALL')

    listen()
    onkey(lambda: move(20), 'd')
    onkey(lambda: move(-20), 'a')
    onkey(lambda: move(20), 'Right')
    onkey(lambda: move(-20), 'Left')

    gameLoop()
    done()