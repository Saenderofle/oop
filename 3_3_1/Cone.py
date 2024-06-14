from Circle import Circle
import math
class Cone(Circle):
    def __init__(self, r, h):
        super().__init__(r)
        assert h > 0
        
        self.h = h
    def dimension(self):
        return 3
    def volume(self):
        l = ((self.r ** 2 + self.h ** 2) ** 0.5)
        return math.pi*self.r*(self.r+l)
    def squareSurface(self):
        l=((self.r**2+self.h**2)**0.5)
        kost = round(math.pi, 4)
        return (kost*self.r*(self.r+l))+(kost*self.r**2)
    def squareBase(self):
       return super().square()
    def height(self):
        return self.h
    def __str__(self) -> str:
        return f"Cone: r={self.r} h={self.h}"