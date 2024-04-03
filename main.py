import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.title("Road Crossing")
screen.bgcolor("black")
screen.setup(600, 600)
screen.tracer(0)

turtle = Player()
car = CarManager()

screen.listen()
screen.onkeypress(turtle.move, "w")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car.move()
    turtle.finish_line()

    for c in car.all_cars:
        if c.distance(turtle) < 28:
            game_is_on = False

screen.exitonclick()
