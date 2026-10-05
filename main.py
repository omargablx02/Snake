from turtle import Screen

from Snakes import Snake
from Food import Food
from Scores import Scoreboards

import time
import random

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
#! لوضع عنوان للشاشه
screen.title('Snake Game')

screen.tracer(0)

snake = Snake()
food = Food()
score = Scoreboards()

screen.listen()
screen.onkey(snake.Up, "Up")
screen.onkey(snake.Down, "Down")
screen.onkey(snake.Left, "Left")
screen.onkey(snake.Right, "Right")

game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        score.increase_level()
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        game_is_on = False
        score.game_over()

    for segment in snake.segments:
        if segment == snake.head:
            pass
        elif snake.head.distance(segment) < 10:
            game_is_on = False
            score.game_over()


screen.exitonclick()
