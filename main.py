import pygame
import objct

from pygame.draw import *
pygame.init()
point_start = 100
speed = 1

screen = pygame.display.set_mode((1000, 600))


user_snake = objct.SnakeUser(screen, 100, 100)


clock = pygame.time.Clock()
flag = True
point = point_start
speed_game = speed

while flag:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            flag = False
    screen.fill((0, 255, 255))

    user_snake.snake_move(point)
    point = point + speed_game

    pygame.display.flip()
    clock.tick(30)

pygame.quit()



