from pygame.draw import *


class Beetle:
    counter = 0

    def __init__(self, sc,  x, y, img):
        self.sc = sc
        self.img = img
        self.hitpoint = 10
        self._color = [255, 255, 255]
        self._size = [20, 21]
        self.x = x
        self.y =y

    def beetle_draw(self):
        self.counter += 1
        self.sc.blit(self.img, (self.x, self.y))
        # rect(self.sc, self._color, (self.x, self.y, self._size[0], self._size[1]))
