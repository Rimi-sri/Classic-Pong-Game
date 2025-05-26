from turtle import Turtle

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("yellow")
        self.penup()
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self.update_scoreboard() # Call this once at the start to draw 0-0

    def update_scoreboard(self):
        self.clear() # Clears everything this turtle has drawn
        self.goto(-100, 200)
        self.write(self.l_score, align="center", font=("Courier", 80, "normal"))
        self.goto(100, 200)
        self.write(self.r_score, align="center", font=("Courier", 80, "normal"))

    def l_point(self):
        self.l_score += 1
        self.update_scoreboard() # Redraws the scores after incrementing

    def r_point(self): # <--- Make sure you have this method!
        self.r_score += 1
        self.update_scoreboard() # Redraws the scores after incrementing