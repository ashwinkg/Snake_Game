from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import ScoreBoard
import time

my_screen = Screen()
my_screen.setup(width=600, height=600)
my_screen.bgcolor("black")
my_screen.title("My Snake Game")
my_screen.tracer(0)

game_is_on = True
snake = Snake()
food = Food()
scoreboard = ScoreBoard()

my_screen.listen()
my_screen.onkey(key="Up", fun=snake.move_up)
my_screen.onkey(key="Down", fun=snake.move_down)
my_screen.onkey(key="Left", fun=snake.move_left)
my_screen.onkey(key="Right", fun=snake.move_right)

while game_is_on:
    my_screen.update()
    time.sleep(0.2)
    snake.move()
    # detecting collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend_snake()
        scoreboard.update_score()
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        game_is_on = False
        scoreboard.display_game_over()

    for segment in snake.segments:
        if segment == snake.head:
            pass
        elif snake.head.distance(segment) < 10:
            game_is_on = False
            scoreboard.display_game_over()

my_screen.exitonclick()
