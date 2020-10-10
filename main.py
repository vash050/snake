import pygame
import os

# Инициализация PyGame

pygame.init()

# Окно игры: размер, позиция

gameScreen = pygame.display.set_mode((400, 300))

# модуль os - позиция окна


x = 100

y = 100

os.environ['Sp_VIDEO_WINDOW_POS'] = "%d,%d" % (x, y)

# параметры окна

size = [1000, 700]

screen = pygame.display.set_mode(size)

pygame.display.set_caption("Test drawings")

gameScreen.fill((0, 0, 255))

pygame.display.flip()

#
# Цикл игры, выход из игры
#
# Цикл игры

runGame = True  # флаг выходв из цикла игры

while runGame:

    # Отслеживание события: "закрыть окно"

    for event in pygame.event.get():
        if event.type == pygame.QUIT: runGame = False

    # Выход из игры: pygame.quit()
