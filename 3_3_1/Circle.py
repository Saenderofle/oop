from Figure import Figure
import math
class Circle(Figure):
    def __init__(self, r):
        assert r > 0
        self.r=r
    def dimension(self):
        return 2
    def perimeter(self):
        kost=round(math.pi, 4)
        return round(2*kost*self.r, 4)
    def square(self):
        kost = round(math.pi, 4)
        return round(kost*(self.r**2), 4)
    def volume(self):
        return self.square()
    def __str__(self) -> str:
        return f"Circle: r={self.r}"