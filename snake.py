"""Snake, classic arcade game.

Exercises

1. How do you make the snake faster or slower?
2. How can you make the snake go around the edges?
3. How would you move the food?
4. Change the snake to respond to mouse clicks.
"""

from random import randrange
from turtle import *

from freegames import square, vector

food = vector(0, 0)
snake = [vector(10, 0)]
aim = vector(0, -10)
score = 0

def restart_game():
    global food, snake, aim, score
    food = vector(0, 0)
    snake = [vector(10, 0)]
    aim = vector(0, -10)
    score = 0
    move()

def change(x, y):
    aim.x = x
    aim.y = y

def inside(head):
    return -200 < head.x < 190 and -200 < head.y < 190

def move():
    global score
    head = snake[-1].copy()
    head.move(aim)

    if not inside(head) or head in snake:
        square(head.x, head.y, 9, 'red')
        update()
        write("Game Over. Score: {}. Press 'r' to restart.".format(score), align="center", font=("Courier", 20, "normal"))
        return

    snake.append(head)

    if head == food:
        score += 1
        food.x = randrange(-15, 15) * 10
        food.y = randrange(-15, 15) * 10
    else:
        snake.pop(0)

    clear()

    for body in snake:
        square(body.x, body.y, 9, 'black')

    square(food.x, food.y, 9, 'green')

    update()
    ontimer(move, 100)

# Set up the turtle screen
setup(420, 420, 370, 0)
hideturtle()
tracer(False)
listen()

# Set up key bindings
onkey(lambda: change(10, 0), 'Right')
onkey(lambda: change(-10, 0), 'Left')
onkey(lambda: change(0, 10), 'Up')
onkey(lambda: change(0, -10), 'Down')

# Bind the 'r' key to restart the game
onkey(restart_game, 'r')

# Start the game
move()
done()


