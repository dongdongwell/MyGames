from turtle import *
from gamebase import square
# 导入random库的randrange函数
from random import randrange
from time import sleep

# randrange函数用法
# randrange(start, end) 在[start, end)范围内取出一个整数
# random函数用法
# random(start, end) 在[start, end)范围内取出一个一位浮点数
apple_x = randrange(-20, 18) * 10
apple_y = randrange(-19, 19) * 10
# 蛇头是最后一个元素
snake = [[0, 0], [10, 0], [20, 0], [30, 0], [40, 0], [50, 0]]
# 方向 x增长10 y不变 (向右移动)
aim_x = 10
aim_y = 0
# 游戏难度等级
game_level = 200

# 初始化
def init():
    global apple_x, apple_y, snake, aim_x, aim_y, game_level
    apple_x = randrange(-20, 18) * 10
    apple_y = randrange(-19, 19) * 10
    snake = [[0, 0], [10, 0], [20, 0], [30, 0], [40, 0], [50, 0]]
    aim_x = 10
    aim_y = 0
    game_level = 200

# 改变运动方向
def change(x, y):
    global aim_x, aim_y
    aim_x = x
    aim_y = y

# 加个新苹果
def addApple():
    global apple_x, apple_y
    apple_x = randrange(-20, 18) * 10
    apple_y = randrange(-19, 19) * 10

# 判断是否撞墙
def inside():
    if (-200 <= snake[-1][0] <= 180 and -190 <= snake[-1][1] <= 190):
        return True
    else :
        return False

# 判断是否撞到自己
def insideSnake():
    for n in range(len(snake) - 1):
        if (snake[-1][0] == snake[n][0] and snake[-1][1] == snake[n][1]):
            return True
    return False

# 画边框
def drawSide():
    square(-210, -200, 410, 'black')
    square(-200, -190, 390, 'white')

# 游戏循环
# 先移动再绘制 原因：按下键盘300ms后才移动，影响体验
# 先clear 再画苹果 最后画蛇
def gameLoop():
    # 函数内部引用外部变量
    global apple_x, apple_y, game_level, snake

    # 移动蛇
    # append函数 向末尾插入一个元素
    snake.append([snake[-1][0] + aim_x, snake[-1][1] + aim_y])
    # pop函数 弹出编号为0的元素
    # 吃到苹果就不用删
    if snake[-1][0] != apple_x or snake[-1][1] != apple_y:
        snake.pop(0)
    else :
        addApple()

    # 判断是否在画布内 和 是否撞到自己
    if (not inside()) or insideSnake():
        square(snake[-1][0], snake[-1][1], 10, 'red')
        update()
        sleep(2)
        init()

    #清除上次的残留
    clear()

    # 绘制边框
    drawSide()

    # 绘制蛇
    for n in range(len(snake)):
        square(snake[n][0], snake[n][1], 10, 'black')
    
    # 绘制苹果
    square(apple_x, apple_y, 10, 'red')

    # 每隔300ms执行一次gameLoop
    ontimer(gameLoop, game_level)
    # 把画好的东西放到画布上
    update()

if __name__ == '__main__':
    print("\n")
    print("##############################\n")
    print("【贪吃蛇】\n")
    print("WASD 控制移动\n")
    print("作者：朱韵冬")
    print("QQ:108759113")
    print("##############################\n")
    print("\n")
    sleep(3)

    # setup构建出的画布原点在正中心
    setup(420, 420, 0, 0)
    hideturtle()
    tracer(False)

    # 监听
    listen()
    # 按到键盘执行change函数
    onkey(lambda: change(0, 10), 'w')
    onkey(lambda: change(0, -10), 's')
    onkey(lambda: change(-10, 0), 'a')
    onkey(lambda: change(10, 0), 'd')

    gameLoop()
    done()