from Triangle import Triangle
from Rectangle import Rectangle
from Cone import Cone
from Circle import Circle
from TriangularPyramid import TriangularPyramid
from Parallelogram import Parallelogram
from Trapeze import Trapeze
from Ball import Ball
from QuadrangularPyramid import QuadrangularPyramid
from RectangularParallelepiped import RectangularParallelepiped
from TriangularPrism import TriangularPrism
class FigureReader:
    def __init__(self, file_name):
        self.file_name = file_name
    def read(self):
        figures = []
        with open(self.file_name) as f:
            for line in f:
                data = line.split()
                #print(data)
                type = data[0]
                try:
                    if type == "Triangle":
                        a, b, c = [float(el) for el in data[1:]]
                        triangler = Triangle(a, b, c)
                        figures.append(triangler)
                    elif type == "Rectangle":
                        a, b = [float(el) for el in data[1:]]
                        rectangler = Rectangle(a, b)
                        figures.append(rectangler)
                    elif type == "Parallelogram":
                        a, b, h = [float(el) for el in data[1:]]
                        paralelogrammy = Parallelogram(a, b, h)
                        figures.append(paralelogrammy)
                    elif type == "Circle":
                        r = float(data[1])
                        circussy = Circle(r)
                        figures.append(circussy)
                    elif type == "Trapeze":
                        a, b, c, d = [float(el) for el in data[1:]]
                        trapezy = Trapeze(a, b, c, d)
                        figures.append(trapezy)
                    elif type == "Cone":
                        r, h = [float(el) for el in data[1:]]
                        conny = Cone(r, h)
                        figures.append(conny)
                    elif type == "TriangularPyramid":
                        a, h = [float(el) for el in data[1:]]
                        triangularprismy = TriangularPyramid(a, h)
                        figures.append(triangularprismy)
                    elif type == "Ball":
                        r = float(data[1])
                        bally = Ball(r)
                        figures.append(bally)
                    elif type == "RectangularParallelepiped":
                        a, b, c = [float(el) for el in data[1:]]
                        rectangularparalelepipeddy = RectangularParallelepiped(a, b, c)
                        figures.append(rectangularparalelepipeddy)
                    elif type == "TriangularPrism":
                        a, b, c, l = [float(el) for el in data[1:]]
                        triangularprismy = TriangularPrism(a, b, c, l)
                        figures.append(triangularprismy)
                    elif type == "QuadrangularPyramid":
                        a, b, h = [float(el) for el in data[1:]]
                        quadrangularpyramiddy = QuadrangularPyramid(a, b, h)
                        figures.append(quadrangularpyramiddy)
                except AssertionError:
                    pass
        return figures