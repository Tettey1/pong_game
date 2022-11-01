from turtle import *


class Paddle(Turtle):
    def __init__(self, item_cor):
        super().__init__()
        self.goto(item_cor)
        self.color('white')
        self.shape('square')
        self.shapesize(stretch_len=1, stretch_wid=5)
        self.penup()

    def move_up(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)

    def move_down(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)



