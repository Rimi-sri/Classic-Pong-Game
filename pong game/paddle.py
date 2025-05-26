from turtle import Turtle
from random import choice # To pick random colors

class Paddle(Turtle):
    def __init__(self, position):
        super().__init__(shape="square")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.original_color = "white" # Store the default color
        self.color(self.original_color)
        self.penup()
        self.goto(position)
        self.move_speed = 40

        # Define a list of alternative colors for impact
        self.impact_colors = ["red", "orange", "yellow", "cyan", "magenta", "lime green"]

    def go_up(self):
        new_y = self.ycor() + self.move_speed
        self.goto(self.xcor(), new_y)

    def go_down(self):
        new_y = self.ycor() - self.move_speed
        self.goto(self.xcor(), new_y)

    def flash_color(self):
        """Changes the paddle's color to a random impact color."""
        self.color(choice(self.impact_colors))

    def reset_color(self):
        """Resets the paddle's color to its original color."""
        self.color(self.original_color)