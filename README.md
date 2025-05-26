# Pong Game 🎮

A classic Pong game implemented in Python using the `turtle` graphics module. This project demonstrates fundamental game development concepts, object-oriented programming (OOP) principles, and real-time animation.

## ✨ Features

* **Classic Pong Gameplay:** Engage in timeless 1v1 action.
* **Dynamic Ball Speed:** The ball's speed progressively increases with each paddle hit, creating a more challenging experience as the rally extends. (Speed resets after a point is scored).
* **Responsive Paddles:** Fast and smooth paddle movement for precise control.
* **Traditional Scoring:** Points are awarded to a player when their opponent fails to return the ball.
* **Clear Game Over Screen:** Displays "GAME OVER!", the final score, and announces the winner.
* **Modular Design:** Code is organized into separate classes (`Paddle`, `Ball`, `Scoreboard`) for better readability and maintainability.
* **Visual Feedback:** Paddles flash a random color upon hitting the ball.



## 🕹️ Controls

* **Left Paddle (Paddle 1):**
    * **W** : Move Up
    * **S** : Move Down
* **Right Paddle (Paddle 2):**
    * **Up Arrow** : Move Up
    * **Down Arrow** : Move Down

## 🎯 Scoring

* A point is awarded to a player when their opponent fails to return the ball and the ball goes off their side of the screen.
* The first player to reach **5 points** wins the game.

## 🏁 Game Over

When a player reaches the score limit (5 points):
* "GAME OVER!" will be displayed on the screen.
* The final score will be shown.
* The winner (Paddle 1 or Paddle 2) will be announced.
* The game window will remain open for 3 seconds before waiting for a click to close.

## 🛠️ Technologies Used

* **Python 3**
* **Turtle Graphics Module** (standard library)

## 📁 File Structure

* `main.py`: The main game loop, initializes game objects, handles collision detection, scoring logic, and game state.
* `paddle.py`: Defines the `Paddle` class, including its shape, color, and movement methods.
* `ball.py`: Defines the `Ball` class, controlling its movement, bouncing logic, and speed adjustments.
* `scoreboard.py`: Defines the `Scoreboard` class, responsible for displaying and updating scores on the screen.
