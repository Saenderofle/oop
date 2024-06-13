import turtle
import math
from digit import Digit

class Dial:
    def __init__(self):
        self.digits = []
        self.turtle = turtle.Turtle()
        self.turtle.hideturtle()
        self.turtle.speed(0)
        self.create_dial()

    def create_dial(self):
        self.draw_border()
        radius = 200
        for i in range(12):
            angle = i * 30
            x = radius * math.cos(math.radians(angle))
            y = radius * math.sin(math.radians(angle))
            digit = Digit((x, y - 10), i + 1)
            self.digits.append(digit)

    def draw_border(self):
        self.turtle.penup()
        self.turtle.goto(0, -220)
        self.turtle.pendown()
        self.turtle.circle(220)

    def draw(self):
        self.draw_border()
        for digit in self.digits:
            digit.draw()
