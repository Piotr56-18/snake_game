from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard
screen = Screen()
food = Food()
scoreboard = Scoreboard()
screen.setup(width=680, height=600)
screen.bgcolor("black")
screen.title("Snake")
screen.tracer(0)
snake = Snake()
screen.listen()
screen.onkey(snake.up, key="Up")
screen.onkey(snake.down, key="Down")
screen.onkey(snake.left, key="Left")
screen.onkey(snake.right, key="Right")
game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()
    #Detect collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()
    #Detect Collision with wall
    if snake.head.xcor() > 330 or snake.head.xcor() < -3340 or snake.head.ycor() > 300 or snake.head.ycor() < -300:
        scoreboard.reset()
        snake.reset()
    #detect collision with tail
    for segment in snake.snake[1:]:
        if segment == snake.snake:
            pass
        elif snake.head.distance(segment) < 10:
            scoreboard.reset()
            snake.reset()
screen.exitonclick()

























