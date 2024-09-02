from turtle import Turtle


class Bricks:

    def __init__(self):
        self.brick_ls = []
        self.bake()
        self.arrange_obj()

    def create_bricks(self):
        obj = Turtle()
        obj.penup()
        obj.shape('square')
        obj.color('red')
        obj.shapesize(stretch_wid=1, stretch_len=4)
        self.brick_ls.append(obj)

    def bake(self):
        for n in range(16):
            self.create_bricks()

    def arrange_obj(self):
        x = -420
        y = 280
        for ob in range(0, len(self.brick_ls)):
            if ob == 8:
                x = -420
                y = 250
            elif ob == 15:
                x = 420
                y = 250
            self.brick_ls[ob].goto(x, y)

            x += 120


