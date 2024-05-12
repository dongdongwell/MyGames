import pygame
import const
pygame.init()

gameScreen = pygame.display.set_mode((const.MAP_WIDTH, const.MAP_HEIGHT))
background = pygame.image.load(const.BACKGROUND)

def gameLoop():
    while True:
        gameScreen.blit(background, (0, 0))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return

        pygame.display.update()

if __name__ == '__main__':
    gameLoop()