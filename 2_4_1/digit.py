import turtle

class Digit:
    def __init__(self, position, number):
        self.position = position
        self.number = number
        self.turtle = turtle.Turtle()
        self.turtle.hideturtle()
        self.turtle.penup()
        self.turtle.goto(position)
        self.turtle.write(str(number), align="center", font=("Arial", 18, "normal"))

    def draw(self):
        self.turtle.clear()
        self.turtle.goto(self.position)
        self.turtle.write(str(self.number), align="center", font=("Arial", 18, "normal"))
