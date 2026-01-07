from turtle import Turtle
ALIGNMENT = "center"
FONT = ('Arial', 20, 'normal')
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.score = 0
        with open(file="data.txt", mode="r") as file:
            self.high_score = int(file.read())
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}", move=False, align=ALIGNMENT, font=FONT)

    def reset(self):
        if self.score > self.high_score:
            with open(file="data.txt", mode="w") as file:
                file.write(f"{self.score}")
            self.high_score = self.score
        self.score=0
        self.update_scoreboard()

    # def game_over(self):
    #     self.goto(0,0)
    #     self.write("GAME OVER", move=False, align=ALIGNMENT, font=FONT)


    def  add_score(self):
        self.score+=1
        self.update_scoreboard()