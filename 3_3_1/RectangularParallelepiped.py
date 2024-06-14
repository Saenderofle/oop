from Rectangle import Rectangle
class RectangularParallelepiped(Rectangle):
    def __init__(self, a, b, c):
        assert c > 0
        super().__init__(a, b)
        self.c = c
    def dimension(self):
        return 3
    def volume(self):
        return super().square() * self.c
    def squareBase(self):
        return super().square()
    def squareSurface(self):
        return (2 * super().square() + 2 * self.a * self.c + 2 * self.b * self.c)
    def height(self):
        return self.c
    def __str__(self) -> str:
        return f"RectangularParallelepiped: a={self.a} b={self.b} c={self.c}"