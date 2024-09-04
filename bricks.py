from turtle import Turtle

PALETTE = ['brown', 'red', 'orange', 'green', 'yellow']


class Bricks:

    def __init__(self):
        self.x = -420
        self.y = 260
        self.brick_ls = []
        self.bake()
        self.arrange_obj()

    def create_bricks(self, color):
        obj = Turtle()
        obj.penup()
        obj.shape('square')
        obj.color(color)
        obj.shapesize(stretch_wid=1, stretch_len=5)
        self.brick_ls.append(obj)

    def bake(self):
        x = 0
        for n in range(64):
            if n % 16 == 0:
                x += 1

            self.create_bricks(PALETTE[x])

    def positioning(self):
        self.x = -420
        self.y = self.y - 30

    def arrange_obj(self):
        for ob in range(0, len(self.brick_ls)):

            if ob % 8 == 0:g
                self.positioning()

            self.brick_ls[ob].goto(self.x, self.y)

            self.x += 120

    def remove_brick(self, m):
        for n in self.brick_ls:

            if m == n:
                self.brick_ls.remove(n)
