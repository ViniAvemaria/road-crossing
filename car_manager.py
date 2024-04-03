from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager():
    def __init__(self) -> None:
        self.all_cars = []
        self.speed = STARTING_MOVE_DISTANCE
        for _ in range(30):
            self.create_car()

    def create_car(self):
        c = Turtle("square")
        c.color(random.choice(COLORS))
        c.shapesize(1, 2)
        c.penup()
        c.goto(random.randint(300, 1500), random.randint(-240, 240))
        self.all_cars.append(c)

    def move(self):
        for car in self.all_cars:
            car.bk(self.speed)
            if car.xcor() < -310:
                car.goto(random.randint(300, 1500), random.randint(-240, 240))

    def increase_speed(self):
        self.speed += MOVE_INCREMENT
