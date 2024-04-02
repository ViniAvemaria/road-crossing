from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self) -> None:
        super().__init__()
        self.shape("turtle")
        self.color("white")
        self.penup()
        self.setheading(90)
        self.initial_pos()

    def initial_pos(self):
        self.goto(STARTING_POSITION)

    def move(self):
        self.fd(MOVE_DISTANCE)

    def finish_line(self):
        if self.ycor() == FINISH_LINE_Y:
            self.initial_pos()
