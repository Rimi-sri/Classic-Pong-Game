from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
from time import sleep
from scoreboard import Scoreboard

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong Game")
screen.tracer(0)

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")

game_is_on = True
while game_is_on:
    sleep(ball.move_speed)
    screen.update()
    ball.move()

    if ball.ycor() > 290 or ball.ycor() < -280:
        ball.bounce_y()

    if ball.distance(r_paddle) < 50 and ball.xcor() > 320:
        ball.bounce_x()
        r_paddle.flash_color()
        screen.ontimer(r_paddle.reset_color, 200)

    if ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()
        l_paddle.flash_color()
        screen.ontimer(l_paddle.reset_color, 200)

    if ball.xcor() > 380:
        scoreboard.l_point()
        ball.reset_position()
        r_paddle.reset_color()
        l_paddle.reset_color()

    if ball.xcor() < -380:
        scoreboard.r_point()
        ball.reset_position()
        r_paddle.reset_color()
        l_paddle.reset_color()

    # Game Over Condition and Winner Display
    if scoreboard.l_score >= 5 or scoreboard.r_score >= 5: # Assuming 5 is the score limit
        game_is_on = False

        scoreboard.goto(0, 0)
        scoreboard.clear()
        scoreboard.write("GAME OVER!", align="center", font=("Courier", 40, "normal"))
        
        # Determine and display the winner
        winner_text = ""
        if scoreboard.l_score >= 5:
            winner_text = "Paddle 1 Wins!" # Left Paddle
        elif scoreboard.r_score >= 5:
            winner_text = "Paddle 2 Wins!" # Right Paddle
        
        scoreboard.goto(0, -50) # Position for winner text
        scoreboard.write(winner_text, align="center", font=("Courier", 30, "bold")) # Bold for emphasis

        scoreboard.goto(0, -100) # Position for final score
        scoreboard.write(f"Final Score: {scoreboard.l_score} - {scoreboard.r_score}", align="center", font=("Courier", 24, "normal"))
        
        screen.update()
        sleep(1)

screen.exitonclick()