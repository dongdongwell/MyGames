from turtle import *
from random import randrange

bird = [-100, 80]
ball = [[240, 0]]
bird_size = 50
ball_size = 80

# draw all balls and birds
def draw():
    global bird, ball, bird_size, ball_size

    clear()

    for i in range(len(ball)):
        up()
        goto(ball[i][0], ball[i][1])
        dot(ball_size, 'green')
        ball[i][0] -= 3
    up()
    goto(bird[0], bird[1])
    dot(bird_size, 'yellow')
    bird[1] -= 5
    update()

# the birds to fly
def up_bird():
    bird[1] += bird_size

# def down_bird():
#     bird[1] -= bird_size

# def left_bird():
#     bird[0] -= bird_size

# def right_bird():
#     bird[0] += bird_size

# (a, b) the balls position
def distance(a, b):
    global bird

    x = bird[0]
    y = bird[1]
    return ((a - x) ** 2 + (b - y) ** 2) ** 0.5

# is the bird hit any balls
def hit_balls():
    global ball, ball_size, bird_size

    for i in range(len(ball)):
        if distance(ball[i][0], ball[i][1]) < (ball_size + bird_size) / 2:
            return True
    return False

# is the bird on the map
def inside():
    global bird, bird_size

    half_size = bird_size / 2

    # y listen
    if (bird[1] < -300 + half_size or bird[1] > 300 - half_size):
        return False
    # x listen
    # if (bird[0] < -200 + half_size or bird[0] > 200 - half_size):
    #     return False
    return True

def gameover():
    info = 'GAME OVER!'
    penup()
    goto(-125, 0)
    pencolor('red')
    write(info, font = ('consolas', 40, 'normal'))
    update()

def gameLoop():
    # 1 / 40 probability
    if randrange(40) == 1:
        ball_x = 240
        ball_y = randrange(-300, 300)
        ball.append([ball_x, ball_y])
    if len(ball) != 0:
        if ball[0][0] <= -220:
            ball.pop(0)
    draw()
    if (not inside() or hit_balls()):
        gameover()
        return
    ontimer(gameLoop, 30)

if __name__ == '__main__':
    setup(420, 620, 0, 0)
    title("Bird Game")
    hideturtle()
    tracer(False)
    bgcolor('light blue')

    listen()
    onkey(lambda: up_bird(), 'Up')
    # onkey(lambda: down_bird(), 'Down')
    # onkey(lambda: left_bird(), 'Left')
    # onkey(lambda: right_bird(), 'Right')

    gameLoop()
    done()