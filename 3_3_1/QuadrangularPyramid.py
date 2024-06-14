from Rectangle import Rectangle
class QuadrangularPyramid(Rectangle):
    def __init__(self, a, b, h):
        super().__init__(a, b)
        self.h = h
    def dimension(self):
        return 3
    def squareBase(self):
        return super().square()
    def squareSurface(self):
        half_diagonal = ((self.a ** 2 + self.b ** 2) ** 0.5) / 2
        bone = (half_diagonal ** 2 + self.h ** 2) ** 0.5
        halfperimeter1 = bone * 2 + self.a
        halfperimeter2 = bone * 2 + self.b
        triangle1 = (halfperimeter1 * (halfperimeter1 - self.a) * (halfperimeter1 - bone) * (
                    halfperimeter1 - bone)) ** 0.5
        triangle2 = (halfperimeter2 * (halfperimeter2 - self.b) * (halfperimeter2 - bone) * (
                    halfperimeter2 - bone)) ** 0.5
        return triangle1 * 2 + triangle2 * 2 + super().square()
    def volume(self):
        return super().square()*(1/3)*self.h
    def height(self):
        return self.h
    def __str__(self) -> str:
        return f"QuadrangularPyramid: a={self.a} b={self.b} h={self.h}"