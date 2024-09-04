from turtle import Turtle


class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.color('White')
        self.score = 0
        self.life = 4
        self.update_score()

    def update_score(self):
        self.clear()
        self.goto(420, 250)
        self.write(f"Score: {self.score}", align='right', font=('arial', 20, 'normal'))
        self.goto(-420, 250)
        self.write(f"Life: {self.life}", align='right', font=('arial', 20, 'normal'))

    def count_score(self):
        self.score = self.score + 10
        self.update_score()

    def subtract_life(self):
        self.life = self.life - 1
        self.update_score()

    def game_over(self):
        self.goto(200, 0)
        self.write(f"GAME OVER!!", align='right', font=('arial', 50, 'bold'))
