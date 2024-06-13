import turtle

class Hand:
    def __init__(self, length, width, color):
        self.length = length
        self.width = width
        self.color = color
        self.turtle = turtle.Turtle()
        self.turtle.shape("arrow")
        self.turtle.shapesize(stretch_wid=width, stretch_len=length)
        self.turtle.color(color)
        self.turtle.speed(0)

    def update(self, angle):
        self.turtle.clear()
        self.turtle.setheading(90)
        self.turtle.right(angle)
        self.turtle.stamp()
