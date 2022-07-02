from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self, x, y):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.color("black")
        self.goto(x, y)
        self.score = 1
        with open("data.txt", mode="r") as file:
            self.highscore = int(file.read())
        self.write(f"Level: {self.score} High Score: {self.highscore}", align="center", font=FONT)

    def level_up(self):
        self.score += 1
        self.clear()
        self.write(f"Level: {self.score} High Score: {self.highscore}", align="center", font=FONT)

    def restart(self):
        if self.score > self.highscore:
            with open("data.txt", mode="w") as file:
                file.write(str(self.score))
            with open("data.txt", mode="r") as file:
                self.highscore = int(file.read())
        self.score = 0
        self.level_up()

    def game_over(self):
        self.write("GAME OVER", align="center", font=FONT)
