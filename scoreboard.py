from turtle import Turtle

SCORE_TEXT = "Score:"
ALIGNMENT = "center"
FONT = ("Courier", 20, "normal")


class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.color("white")
        self.penup()
        self.setpos(0, 270)
        self.current_score = 0
        self.display_score()

    def display_score(self):
        self.write(f"{SCORE_TEXT} {self.current_score}", move=False, align=ALIGNMENT, font=FONT)

    def update_score(self):
        self.current_score += 1
        self.clear()
        self.display_score()

    def display_game_over(self):
        self.goto(0, 0)
        self.write(f"GAME OVER", move=False, align=ALIGNMENT, font=FONT)
