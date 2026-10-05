from turtle import Turtle

Alignment = 'center'
Font = ("courier", 24, 'normal')


class Scoreboards(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color('white')
        self.penup()
        self.goto(0, 265)
        self.hideturtle()
        self.update_scoreboards()

    def update_scoreboards(self):
        self.write(f"Score: {self.score}", align=Alignment, font=Font)

    def game_over(self):
        self.goto(0, 0)
        self.write(f"GAME OVER!", align=Alignment, font=Font)

    def increase_level(self):
        self.score+=1
        self.clear()
        self.update_scoreboards()
