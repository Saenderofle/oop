from Triangle import Triangle
class TriangularPrism(Triangle):
    def __init__(self, a, b, c, l):
        assert l > 0
        super().__init__(a, b, c)
        self.l = l
    def dimension(self):
        return 3
    def semiperimeter(self):
        return super().perimeter() / 2
    def perimeter_bone(self):
        return super().perimeter()
    def squareBase(self):
        return super().square()
    def squareSurface(self):
        result_tr = super().square()
        result_re = (self.a * self.l + self.b * self.l + self.c * self.l)
        result = (result_tr * 2 + result_re)
        result = round(result.real, 2) + round(result.imag, 2) * 1j
        result_list = [round(result.real, 2), round(result.imag, 2)]
        ressy = max(result_list)
        return ressy

    def volume(self):
        result_tr = super().square()
        return result_tr * self.l
    def height(self):
        return self.l
    def __str__(self) -> str:
        return f"TriangularPrism: a={self.a} b={self.b} c={self.c} l={self.l}"