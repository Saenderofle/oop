from Figure import Figure
from math import pi
class Ball(Figure):
    def __init__(self, r):
        assert r > 0
        self.r = r
    def dimension(self):
        return 3
    def squareSurface(self):
        kost=round(pi, 4)
        result = round(4 * kost * self.r ** 2, 4)
        return result
    def height(self):
        return self.r*2
    def volume(self):
        result = (4/3) * pi * self.r ** 3
        return result
    def __str__(self) -> str:
        return f"Ball: r={self.r}"