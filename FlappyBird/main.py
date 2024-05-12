import pygame
import const
pygame.init()

gameScreen = pygame.display.set_mode((const.MAP_WIDTH, const.MAP_HEIGHT))
background = pygame.image.load(const.BACKGROUND)
bird_wing_up = pygame.image.load(const.BIRD_WING_UP)

def draw_birds(x, y):
    gameScreen.blit(bird_wing_up, (x, y))

def gameLoop():
    while True:
        gameScreen.blit(background, (0, 0))
        draw_birds(20, const.MAP_HEIGHT // 2)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return

        pygame.display.update()

if __name__ == '__main__':
    gameLoop()