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
    def set_pivot(self, pivot_x, pivot_y):
        self.pivot=(pivot_x, pivot_y)
        self.pivot=self.bi()
    def circle(self, radius): # рисует кружок, на котором будет храниться вершина треугольника
        t = turtle.Turtle()

        t.speed(0)
        t.penup()
        t.goto(self.pivot[0], self.pivot[1]-radius) #конкретна точка буде встановлена пізніше
        t.pendown()
        t.circle(radius) #намалювали коло


    def calculator(self, radius):
        self.point_turtle.shape("circle")
        self.point_turtle.penup()

        for angle in range(0, 360):


            point_x = self.pivot[0] + radius * cos(radians(angle))
            point_y = self.pivot[1] + radius * sin(radians(angle))


            self.point_turtle.goto(point_x, point_y)


            self.x1, self.y1 = self.rotate_point(self.x1, self.y1, self.pivot[0], self.pivot[1], 1)
            self.x2, self.y2 = self.rotate_point(self.x2, self.y2, self.pivot[0], self.pivot[1], 1)
            self.x3, self.y3 = self.rotate_point(self.x3, self.y3, self.pivot[0], self.pivot[1], 1)


            self.point_turtle.penup()
            self.point_turtle.goto(self.x1, self.y1)
            self.point_turtle.pendown()
            self.point_turtle.goto(self.x2, self.y2)
            self.point_turtle.goto(self.x3, self.y3)
            self.point_turtle.goto(self.x1, self.y1)
            self.point_turtle.penup()

    def rotate_point(self, x, y, cx, cy, angle):

        angle_rad = radians(angle)
        new_x = cx + (x - cx) * cos(angle_rad) - (y - cy) * sin(angle_rad)
        new_y = cy + (x - cx) * sin(angle_rad) + (y - cy) * cos(angle_rad)
        return new_x, new_y

    def radius(self):
        radius1=(((self.pivot[0]-self.x1))**2+(self.pivot[1]-self.y1)**2)**0.5
        radius2 = ((self.pivot[0]-self.x2)**2+(self.pivot[1]-self.y2)**2)**0.5
        radius3 = ((self.pivot[0]-self.x3)**2+(self.pivot[1]-self.y3)**2)**0.5
        pust=[]
        difpust=[]
        if isinstance(radius1, complex):

            result_list = [round(radius1.real, 8), round(radius1.imag, 8)]
            res=max(result_list)
            pust.append(res)
        else:

            difpust.append(round(radius1, 8))
        if isinstance(radius2, complex):

            result_list = [round(radius2.real, 8), round(radius2.imag, 8)]
            ress=max(result_list)
            pust.append(ress)
        else:

            difpust.append(round(radius2, 8))
        if isinstance(radius3, complex):

            result_list = [round(radius3.real, 8), round(radius3.imag, 8)]
            ressy=max(result_list)
            pust.append(ressy)
        else:

            difpust.append(round(radius3, 8))
        merged_list=pust+difpust
        return merged_list

    def bi(self):
        vector1 = [self.x1 - self.x2, self.y1 - self.y2 ]
        vector2 = [self.x3 - self.x2, self.y3 - self.y2]
        vector3= [self.x3 - self.x1, self.y3 - self.y1]
        vectormodule1=(vector1[0]**2+vector1[1]**2)**0.5
        vectormodule2 = (vector2[0] ** 2 + vector2[1] ** 2) ** 0.5
        vectormodule3 = (vector3[0] ** 2 + vector3[1] ** 2) ** 0.5
        bi_x=(vectormodule1*self.x1+vectormodule2*self.x2+vectormodule3*self.x3)/(vectormodule1+vectormodule2+vectormodule3)
        bi_y = (vectormodule1 * self.y1 + vectormodule2 * self.y2 + vectormodule3 * self.y3) / (vectormodule1 + vectormodule2 + vectormodule3)
        return [bi_x, bi_y]
    def scale(self):
        scalescalar=(2, 2)
        scaledvector1=(self.x1*scalescalar[0], self.y1*scalescalar[1])
        scaledvector2 = (self.x2 * scalescalar[0], self.y2 * scalescalar[1])
        scaledvector3 = (self.x3 * scalescalar[0], self.y3 * scalescalar[1])
        return scaledvector1, scaledvector2, scaledvector3
if __name__ == '__main__':
    a = randint(-100, 100)
    b = randint(-100, 100)
    c = randint(-100, 100)
    d = randint(-100, 100)
    e = randint(-100, 100)
    f = randint(-100, 100)
    triangle = Triangle(a, b, c, d, e, f)
    res=triangle.bi()
    triangle.set_pivot(res[0], res[1])
    radiant = triangle.radius()
    triangle.circle(radiant[0])
    triangle.circle(radiant[1])
    triangle.circle(radiant[2])
    triangle.calculator(radiant[0])
    triangle.calculator(radiant[1])
    triangle.calculator(radiant[2])
    turtle.mainloop()




