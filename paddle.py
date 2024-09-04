from turtle import Turtle


class Paddle(Turtle):

    def __init__(self):
        super().__init__()
        self.shape('square')
        self.color('blue')
        self.shapesize(stretch_wid=1, stretch_len=10)
        self.penup()
        self.goto(0, -275)

    def move_right(self):
        if self.xcor() < 370:
            new_x = self.xcor() + 20
            self.goto(new_x, self.ycor())

    def move_left(self):
        if self.xcor() > -370:
            self.backward(20)
