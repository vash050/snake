import random

import pygame
from obj_snake import Snake
from obj_beetle import Beetle

pygame.init()
width = 1000
height = 600

list_beet = []

start_x = 100
start_y = 100

start_snake_speed = 1
img = pygame.image.load('img/beetle.png')
img_snake = [pygame.image.load('img/head_snake.png'),
             pygame.image.load('img/body_snake_r.png'),
             pygame.image.load('img/body_snake_l.png'),
             pygame.image.load('img/tail_snake_r.png'),
             pygame.image.load('img/tail_snake_l.png'),
             ]

display = pygame.display.set_mode((width, height))

user_snake = Snake(display, img_snake)

clock = pygame.time.Clock()


def beetles(list_beetles):
    for el in range(11):
        list_beetles.append(Beetle(display, random.randint(0, width + 1), random.randint(0, height + 1), img))
    return list_beetles


def draw_beetles(list_beetles):
    for beetle in list_beetles:
        beetle.beetle_draw()


def run_game(x, y, snake_speed, d_x=1, d_y=0, direction=''):
    game = True
    count_beet = beetles(list_beet)
    background = pygame.image.load(r'img/background.jpg')

    while game:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            #######################################################################################
            # управление змейкой
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    if direction != 'RIGHT':
                        direction = 'LEFT'
                        print(direction)
                        d_x = -snake_speed
                        d_y = 0
                elif event.key == pygame.K_RIGHT:
                    if direction != 'LEFT':
                        direction = 'RIGHT'
                        print(direction)
                        d_x = snake_speed
                        d_y = 0

                elif event.key == pygame.K_UP:
                    if direction != 'DOWN':
                        direction = 'UP'
                        print(direction)
                        d_x = 0
                        d_y = -snake_speed
                elif event.key == pygame.K_DOWN:
                    if direction != 'UP':
                        direction = 'DOWN'
                        print(direction)
                        d_x = 0
                        d_y = snake_speed
        #####################################################################################################
        display.blit(background, (0, 0))
        draw_beetles(count_beet)

        x += d_x
        y += d_y
        #####################################################################################################

        # выход за границы игрового поля

        s_x, s_y = user_snake.get_size()

        if x < -s_x:
            x = width
        elif x > width:
            x = 0
        elif y < -s_y:
            y = height
        elif y > height:
            y = 0
        ######################################################################################################
        user_snake.snake_move(x, y)

        pygame.display.update()
        clock.tick(60)


run_game(start_x, start_y, start_snake_speed)
