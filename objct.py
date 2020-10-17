import pygame
from pygame.draw import *


class SnakeUser:
    def __init__(self, sc, x, y, speed=1, level=1, color=(0, 0, 0)):
        self.color = color
        self.length = 3
        self.speed = speed
        self.level = level
        self.sc = sc
        self.coordinate_x = x
        self.coordinate_y = y
        self.size_h = [
            [0, 0, 6, 22],
            [-2, 0, 2, 5],
            [6, 0, 2, 5],
            [[-5, 9], [-1, 9], [-1, 5]],
            [[10, 9], [6, 9], [6, 5]],
            [-5, 9, 5, 4],
            [6, 9, 5, 4],
            [-4, 11, 4, 4],
            [6, 11, 4, 4],
            [[-4, 15], [-1, 15], [-1, 18]],
            [[9, 15], [6, 15], [6, 18]]
        ]

    def head(self):
        rect(self.sc, self.color, (self.coordinate_x + self.size_h[0][0],
                                   self.coordinate_y + self.size_h[0][1],
                                   self.size_h[0][2],
                                   self.size_h[0][3]
                                   ))
        rect(self.sc, self.color, (self.coordinate_x + self.size_h[1][0],
                                   self.coordinate_y + self.size_h[1][1],
                                   self.size_h[1][2],
                                   self.size_h[1][3]
                                   ))
        rect(self.sc, self.color, (self.coordinate_x + self.size_h[2][0],
                                   self.coordinate_y + self.size_h[2][1],
                                   self.size_h[2][2],
                                   self.size_h[2][3]
                                   ))
        lines(
            self.sc,
            self.color,
            True,
            [[self.coordinate_x + self.size_h[3][0][0], self.coordinate_y + self.size_h[3][0][1]],
             [self.coordinate_x + self.size_h[3][1][0], self.coordinate_y + self.size_h[3][1][1]],
             [self.coordinate_x + self.size_h[3][2][0], self.coordinate_y + self.size_h[3][2][1]]],
            3)
        lines(
            self.sc,
            self.color,
            True,
            [[self.coordinate_x + self.size_h[4][0][0], self.coordinate_y + self.size_h[4][0][1]],
             [self.coordinate_x + self.size_h[4][1][0], self.coordinate_y + self.size_h[4][1][1]],
             [self.coordinate_x + self.size_h[4][2][0], self.coordinate_y + self.size_h[4][2][1]]],
            3)
        rect(self.sc, self.color, (self.coordinate_x + self.size_h[5][0],
                                   self.coordinate_y + self.size_h[5][1],
                                   self.size_h[5][2],
                                   self.size_h[5][3]
                                   ))
        rect(self.sc, self.color, (self.coordinate_x + self.size_h[6][0],
                                   self.coordinate_y + self.size_h[6][1],
                                   self.size_h[6][2],
                                   self.size_h[6][3]
                                   ))
        rect(self.sc, self.color, (self.coordinate_x + self.size_h[7][0],
                                   self.coordinate_y + self.size_h[7][1],
                                   self.size_h[7][2],
                                   self.size_h[7][3]
                                   ))
        rect(self.sc, self.color, (self.coordinate_x + self.size_h[8][0],
                                   self.coordinate_y + self.size_h[8][1],
                                   self.size_h[8][2],
                                   self.size_h[8][3]
                                   ))
        lines(
            self.sc,
            self.color,
            True,
            [[self.coordinate_x + self.size_h[9][0][0], self.coordinate_y + self.size_h[9][0][1]],
             [self.coordinate_x + self.size_h[9][1][0], self.coordinate_y + self.size_h[9][1][1]],
             [self.coordinate_x + self.size_h[9][2][0], self.coordinate_y + self.size_h[9][2][1]]],
            2)
        lines(
            self.sc,
            self.color,
            True,
            [[self.coordinate_x + self.size_h[10][0][0], self.coordinate_y + self.size_h[10][0][1]],
             [self.coordinate_x + self.size_h[10][1][0], self.coordinate_y + self.size_h[10][1][1]],
             [self.coordinate_x + self.size_h[10][2][0], self.coordinate_y + self.size_h[10][2][1]]],
            2)

    def body(self):
        for el in range(self.length + 1):
            rect(self.sc, self.color, (self.coordinate_x - 2, self.coordinate_y - (1 + el * 10), 10, 10))

    def tail(self):
        lines(
            self.sc,
            self.color,
            True,
            [[self.coordinate_x - 2, self.coordinate_y - (self.length * 10 + 2)],
             [self.coordinate_x + 2, self.coordinate_y - (self.length * 10 + 13)],
             [self.coordinate_x + 6, self.coordinate_y - (self.length * 10 + 2)]],
            6)

    def draw_snake(self):
        self.head()
        self.body()
        self.tail()

    def snake_move(self, a):
        self.coordinate_y = a
        self.draw_snake()

    def turn_right(self):
        self.size_h = [
            [-22, 0, 22, 6],
            [15, -2, 5, 2],
            [15, 6, 5, 2],
            [[11, -5], [11, -1], [14, -1]],
            [[11, 10], [11, 7], [14, 7]],
            [9, -5, 4, 5],
            [9, 6, 4, 5],
            [6, -4, 4, 4],
            [6, 6, 4, 4],
            [[2, -1], [5, -1], [5, -4]],
            [[2, 6], [5, 6], [5, 9]]
        ]
