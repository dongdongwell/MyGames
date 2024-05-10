# 导入海龟图的所有函数
from turtle import *

# 画正方形
def square(x, y, size, color_name):
    # 把乌龟拿起来
    up()
    # 把乌龟转移到(x, y)的位置
    goto(x, y)
    # 把乌龟丢下来
    down()
    # 给乌龟涂上color_name的颜色
    color(color_name)
    # 开始让乌龟爬
    begin_fill()

    # 直走size个单位长度
    forward(size)
    # 左转90度
    left(90)
    forward(size)
    left(90)
    forward(size)
    left(90)
    forward(size)
    left(90)

    # 不让乌龟爬
    end_fill()

# 设置一个大小420 * 420的画布
# setup(420, 420, 0, 0)
# 隐藏乌龟
# hideturtle()
# 延迟调0 不看乌龟爬的过程
# tracer(False)
# 调用square函数
# square(50, 50, 10, 'red')
# 画布停留
# done()