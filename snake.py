from turtle import Turtle
COORDINATES = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0
class Snake:
    def __init__(self):
        self.save_all_turtles = []
        self.create_snake()
        self.head = self.save_all_turtles[0]


    def create_snake(self):
        for turtle_index in COORDINATES:
            self.add_segment(turtle_index)


    def add_segment(self, position):
        ariela = Turtle(shape="square")
        ariela.penup()
        ariela.color("white")
        ariela.goto(position)
        self.save_all_turtles.append(ariela)

    def reset(self):
        for seg in self.save_all_turtles:
            seg.goto(1000, 1000)
        self.save_all_turtles.clear()
        self.create_snake()
        self.head = self.save_all_turtles[0]

    def extend(self):
        self.add_segment(self.save_all_turtles[-1].position())

    def snake_move(self):
        for seg_num in range(len(self.save_all_turtles) - 1, 0, -1):
            new_x = self.save_all_turtles[seg_num - 1].xcor()
            new_y = self.save_all_turtles[seg_num - 1].ycor()
            self.save_all_turtles[seg_num].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def turn_up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def turn_down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def turn_left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def turn_right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

