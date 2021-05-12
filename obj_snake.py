from pygame.draw import *


class Snake:
    def __init__(self, sc, imgs):
        self.sc = sc
        self.imgs = imgs
        self.count = 1
        self.hitpoint = 100
        self._color = [255, 0, 0]
        self._size = [[20, 16], [20, 25], [20, 19]]
        self.x_head = 100
        self.y_head = 100
        self.x_head_new = 0
        self.y_head_new = 0
        self.length = [[self.x_head, self.y_head],
                       [self.x_head - 20, self.y_head],
                       [self.x_head - 40, self.y_head]]

    def cat_length(self):
        while self.length[0][0] - self.length[-1][0] > 20:
            self.length.pop()
        while self.length[0][1] - self.length[-1][1] > 20:
            self.length.pop()
        while self.length[-1][0] - self.length[0][0] > 20:
            self.length.pop()
        while self.length[-1][1] - self.length[0][1] > 20:
            self.length.pop()

    def set_length(self):
        self.length.insert(0, [self.x_head_new, self.y_head_new])
        self.cat_length()

    def get_img(self):
        if self.count == 4:
            self.count = 0
            self.img = self.imgs[2]
            self.count += 1
        else:
            self.img = self.imgs[0]
            self.count += 1

    def snake_draw(self):
        self.get_img()
        self.sc.blit(self.img,)
        # for el in self.length:
        #     rect(self.sc, self._color, (el[0], el[1], self._size[0], self._size[1]))

    def snake_move(self, x, y):
        self.x_head_new = x
        self.y_head_new = y
        self.set_length()
        self.snake_draw()

    def get_size(self):
        return self._size
