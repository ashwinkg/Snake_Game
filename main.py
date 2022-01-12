from turtle import Screen
from snake import Snake
import time

my_screen = Screen()
my_screen.setup(width=600, height=600)
my_screen.bgcolor("black")
my_screen.title("My Snake Game")
my_screen.tracer(0)

game_is_on = True
snake = Snake()

my_screen.listen()
my_screen.onkey(key="Up", fun=snake.move_up)
my_screen.onkey(key="Down", fun=snake.move_down)
my_screen.onkey(key="Left", fun=snake.move_left)
my_screen.onkey(key="Right", fun=snake.move_right)

while game_is_on:
    my_screen.update()
    time.sleep(0.1)
    snake.move()

my_screen.exitonclick()
