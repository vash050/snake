import pygame
from pygame.draw import *

pygame.init()

FPS = 30
screen = pygame.display.set_mode((600, 400))
screen.fill((0,0,255))

circle(screen, (255, 255, 0), (300, 200), 150)
circle(screen, (255, 0, 0), (225, 150), 25)
circle(screen, (0, 0, 0), (225, 150), 10)
circle(screen, (255, 0, 0), (375, 150), 20)
circle(screen, (0, 0, 0), (375, 150), 10)
polygon(screen, (0, 0, 0), [(145, 75), (140, 85), (260, 140), (265, 130)])
polygon(screen, (0, 0, 0), [(340, 132), (345, 142), (450, 85), (445, 75)])
rect(screen, (0, 0, 0), (230, 270, 150, 40))

pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()
