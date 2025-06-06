from turtle import Turtle

class Ball(Turtle):

    def __init__(self):
        super().__init__(shape="circle")
        self.color("white")
        self.penup()
        self.goto(0, 0)
        self.x_move = 10
        self.y_move = 10
        self.move_speed = 0.05
        self.hit_count = 0 # Must be here

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce_y(self):
        self.y_move *= -1

    def bounce_x(self):
        self.x_move *= -1
        if self.move_speed > 0.01:
            self.move_speed *= 0.9
        self.hit_count += 1 # Must be here

    def reset_position(self):
        self.goto(0, 0)
        self.move_speed = 0.05
        self.hit_count = 0 # Must be here
        self.bounce_x()