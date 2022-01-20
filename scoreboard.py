from turtle import Turtle

SCORE_TEXT = "Score:"
ALIGNMENT = "center"
FONT = ("Courier", 20, "normal")


class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.color("white")
        self.high_score = 0
        self.read_high_score_from_file()
        # self.high_score =0
        self.penup()
        self.setpos(0, 270)
        self.current_score = 0
        self.display_score()

    def display_score(self):
        self.clear()
        self.write(f"{SCORE_TEXT} {self.current_score} High Score: {self.high_score}", move=False, align=ALIGNMENT, font=FONT)

    def update_score(self):
        self.current_score += 1
        self.display_score()

    def reset_score(self):
        if self.high_score < self.current_score:
            self.high_score = self.current_score
            self.write_high_score_to_file()
        self.current_score = 0
        self.display_score()

    # def display_game_over(self):
    #     self.goto(0, 0)
    #     self.write(f"GAME OVER", move=False, align=ALIGNMENT, font=FONT)

    def read_high_score_from_file(self):
        with open(file="data.txt", mode="r") as file:
            content = file.read()
            self.high_score = int(content)

    def write_high_score_to_file(self):
        with open(file="data.txt", mode="w") as file:
            file.write(str(self.high_score))

