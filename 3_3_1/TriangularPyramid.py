from Triangle import Triangle
class TriangularPyramid(Triangle):
    def __init__(self, a, h):
        assert h>0
        super().__init__(a, a, a)
        self.h = h
    def dimention(self):
        return 3
    def volume(self):
        return (1/3)*super().square()*self.h
    def squareBase(self):
        return super().square()
    def squareSurface(self):
        r = (((3)**0.5)/6) * self.a
        ap = ((self.h)**2 * (r)**2)**0.5
        result = (3/2) * self.a * ap
        return result

    def height(self):
        return self.h
    def __str__(self) -> str:
        return f"TriangularPyramid: a={self.a} h={self.h}"