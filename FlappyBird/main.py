import pygame
import const
pygame.init()

# 定义帧率
frame = 0

clock = pygame.time.Clock()
gameScreen = pygame.display.set_mode((const.MAP_WIDTH, const.MAP_HEIGHT))

background = pygame.image.load(const.BACKGROUND)
bird_wing_up = pygame.image.load(const.BIRD_WING_UP)
bird_wing_down = pygame.image.load(const.BIRD_WING_DOWN)

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

def gameLoop():
    while True:
        gameScreen.blit(background, (0, 0))
        draw_birds(20, const.MAP_HEIGHT // 2)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return

        pygame.display.update()
        clock.tick(const.FPS)

if __name__ == '__main__':
    gameLoop()