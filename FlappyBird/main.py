import pygame
import const
from random import randrange
from time import sleep
pygame.init()

# 定义帧率
frame = 0
# [x坐标， 开口位置]
pipes = [[const.PIPE_SPACE, 4]]
bird = [const.BIRD_INIT_X, const.MAP_HEIGHT // 2 - 50]
bird_down_velocity = 0

clock = pygame.time.Clock()
gameScreen = pygame.display.set_mode((const.MAP_WIDTH, const.MAP_HEIGHT))

background = pygame.image.load(const.BACKGROUND)
bird_wing_up = bird_wing_up_copy = pygame.image.load(const.BIRD_WING_UP)
bird_wing_down = bird_wing_down_copy = pygame.image.load(const.BIRD_WING_DOWN)
pipe_body = pygame.image.load(const.PIPE_BODY)
pipe_end = pygame.image.load(const.PIPE_END)

def draw_pipes():
    global pipes
    for i in range(len(pipes)):
        for j in range(pipes[i][1]):
            gameScreen.blit(pipe_body, (pipes[i][0], j * 32))
        for j in range(pipes[i][1] + 6, 16):
            gameScreen.blit(pipe_body, (pipes[i][0], j * 32))
        gameScreen.blit(pipe_end, (pipes[i][0], pipes[i][1] * 32))
        gameScreen.blit(pipe_end, (pipes[i][0], (pipes[i][1] + 5) * 32))
        pipes[i][0] -= 1

def draw_birds(x, y):
    global frame
    if 0 <= frame <= 30:
        gameScreen.blit(bird_wing_up, (x, y))
        frame += 1
    elif 30 < frame <= 60:
        gameScreen.blit(bird_wing_down, (x, y))
        frame += 1
        if frame == 60:
            frame = 0

def add_pipes():
    if len(pipes) < 4:
        x = pipes[-1][0] + const.PIPE_SPACE
        open_pos = randrange(1, 9)
        pipes.append([x, open_pos])
    if (pipes[0][0]) < -100:
        pipes.pop(0)

def bird_down():
    global bird, bird_down_velocity, bird_wing_down, bird_wing_up
    bird_down_velocity += const.GRAVITY
    bird[1] += bird_down_velocity
    bird_wing_down = pygame.transform.rotate(bird_wing_down_copy, -90 * (bird_down_velocity / 15))
    bird_wing_up = pygame.transform.rotate(bird_wing_up_copy, -90 * (bird_down_velocity / 15))

def safe():
    if bird[1] > const.MAP_HEIGHT - 35:
        return False
    if bird[1] < 0:
        return False
    if pipes[0][0] - 30 < bird[0] < pipes[0][0] + 79:
        if (bird[1] < (pipes[0][1] + 1) * 32 or bird[1] > (pipes[0][1] + 4) * 32):
            return False
    return True

def reset():
    global frame, pipes, bird, bird_down_velocity
    # 定义帧率
    frame = 0
    # [x坐标， 开口位置]
    pipes.clear()
    bird.clear()
    pipes = [[const.PIPE_SPACE, 4]]
    bird = [const.BIRD_INIT_X, const.MAP_HEIGHT // 2 - 50]
    bird_down_velocity = 0

def gameLoop():
    while True: 
        add_pipes()

        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                global bird_down_velocity
                bird[1] -= const.BIRD_FLY
                bird_down_velocity = 0
            if event.type == pygame.QUIT:
                pygame.quit()
                return

        bird_down()
        gameScreen.blit(background, (0, 0))
        draw_birds(bird[0], bird[1])
        draw_pipes()
        pygame.display.update()
        if not safe():
            sleep(0.5)
            reset()

        clock.tick(const.FPS)

if __name__ == '__main__':
    gameLoop()