import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.bgcolor("black")
screen.setup(600, 600)
screen.tracer(0)

turtle = Player()

screen.listen()
screen.onkeypress(turtle.move, "w")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    turtle.finish_line()

screen.exitonclick()
