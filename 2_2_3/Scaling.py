import turtle

from random import randint
from math import sin, cos,  radians, asin, atan2

import numpy as np



class Triangle:


    def __init__(self, x1, y1, x2, y2, x3, y3):

        self.x1 = x1
        self.x2 = x2
        self.x3 = x3
        self.y1 = y1
        self.y2 = y2
        self.y3 = y3


        self.point_turtle = turtle.Turtle()

        self.position = (0, 0)
    def set_pivot(self, pivot_xy):
        self.pivot=(pivot_xy)
        self.pivot=self.median()
    def scale(self, sc_x, sc_y):
        scalescalar = (sc_x, sc_y)
        scaledvector1 = ((self.x1 - self.pivot[0]) * scalescalar[0], scalescalar[1] * (self.y1-self.pivot[1]))
        scaledvector2 = (scalescalar[0] * (self.x2-self.pivot[0]), scalescalar[1] * (self.y2-self.pivot[1]))
        scaledvector3 = (scalescalar[0] * (self.x3-self.pivot[0]), scalescalar[1] * (self.y3-self.pivot[1]))
        scv1 = (scaledvector1[0] + self.pivot[0], scaledvector1[1] + self.pivot[1])
        scv2 = (scaledvector2[0] + self.pivot[0], scaledvector2[1] + self.pivot[1])
        scv3 = (scaledvector3[0] + self.pivot[0], scaledvector3[1] + self.pivot[1])
        return [scv1[0] ,scv1[1], scv2[0], scv2[1], scv3[0], scv3[1]]
    def drawer(self):
        sc_x=1
        sc_y=1
        #self.scale(sc_x, sc_y)
        for i in range(0, 100):
            sc_x=sc_x*1.25
            sc_y = sc_y * 1.25
            scaledata=self.scale(sc_x, sc_y)
            self.point_turtle.penup()
            self.point_turtle.goto(scaledata[0], scaledata[1])
            self.point_turtle.pendown()
            self.point_turtle.goto(scaledata[2], scaledata[3])
            self.point_turtle.goto(scaledata[4], scaledata[5])
            self.point_turtle.goto(scaledata[0], scaledata[1])
            self.point_turtle.penup()
    def median(self):

        point_median=[(self.x1+self.x2+self.x3)/3, (self.y1+self.y2+self.y3)/3]
        return point_median
if __name__ == '__main__':
    a = randint(-10, 10)
    b = randint(-10, 10)
    c = randint(-10, 10)
    d = randint(-10, 10)
    e = randint(-10, 10)
    f = randint(-10, 10)
    triangle = Triangle(a, b, c, d, e, f)
    data=triangle.median()
    triangle.set_pivot(data)
    triangle.drawer()





