from math import sin, cos, radians
import turtle

class Triangle:
    default_color = "Grey"

    def __init__(self, x1, y1, x2, y2):
        self._vertex1 = (x1, y1)
        self._vertex2 = (x2, y2)
        self.color = Triangle.default_color
        self.position = (0, 0)
        self.rotation = 0
        self.scale = (1, 1)

    def set_position(self, x, y):
        self.position = (x, y)

    def set_scale(self, scale_x, scale_y):
        self.scale = (scale_x, scale_y)

    def move(self, dx, dy):
        self.position = (self.position[0] + dx, self.position[1] + dy)

    def set_color(self, color):
        self.color = color

    def set_rotation(self, rotation):
        self.rotation = rotation

    def rotation_degree(self, degree):
        self.rotation = radians(degree)

    def rM(self):
        fi = self.rotation
        fiMatrix = [[cos(fi), -sin(fi)],[sin(fi), cos(fi)]]
        return fiMatrix

    @staticmethod
    def multMatrixVector(M, v):
        turnedVertex1 = [0, 0]
        turnedVertex1[0] = M[0][0] * v[0] + M[0][1] * v[1]
        turnedVertex1[1] = M[1][0] * v[0] + M[1][1] * v[1]
        return turnedVertex1

    @staticmethod
    def scaleVertex(vertex, scale):
        return (scale[0] * vertex[0],
                scale[0] * vertex[1])

    def calc_abs_pos(self):
        scaledVertex1 = Triangle.scaleVertex(self._vertex1, self.scale)
        scaledVertex2 = Triangle.scaleVertex(self._vertex2, self.scale)
        M = self.rM()
        turnedVertex1 = Triangle.multMatrixVector(M, scaledVertex1)
        turnedVertex2 = Triangle.multMatrixVector(M, scaledVertex2)

        v1 = (self.position[0] + turnedVertex1[0],
              self.position[1] + turnedVertex1[1])
        v2 = (self.position[0] + turnedVertex2[0],
              self.position[1] + turnedVertex2[1])
        return v1, v2

    def draw(self):
        v1, v2 = self.calc_abs_pos()
        turtle.color(self.color)
        turtle.up()
        turtle.setpos(*self.position)
        turtle.down()
        turtle.goto(*v1)
        turtle.goto(*v2)
        turtle.setpos(*self.position)
        turtle.up()
        turtle.color(Triangle.default_color)



if __name__ == '__main__':
    turtle.speed(10)
    triangle = Triangle(150, 150, 150, 0)
    triangle.draw()
    for degree in range(3, 363, 3):
        triangle.rotation_degree(degree)
        triangle.set_scale(1, abs(sin(radians(degree))))
        triangle.draw()
turtle.mainloop()