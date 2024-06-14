from Figure import Figure
class Trapeze(Figure):
    def __init__(self, a, b, c, d):
        assert a > 0 and b > 0 and c > 0 and d > 0 and a + b > c and a + b > d and a!=b

        self.a = a
        self.b = b
        # бічні
        self.c = c
        self.d = d
    def dimension(self):
        return 2
    def perimeter(self):
        result = self.a + self.b + self.c + self.d
        return (result)

    def square(self):
        result = ((round(self.a + self.b) / 2) * (self.c ** 2 - (
                    ((self.a - self.b) ** 2 + self.c ** 2 - self.d ** 2) / (2 * (self.a - self.b))) ** 2) ** 0.5)
        if isinstance(result, complex):

            result_list = [round(result.real, 2), round(result.imag, 2)]
            ressy=max(result_list)
            return ressy
        else:

            return round(result, 2)
    def volume(self):
        return self.square()
    def __str__(self) -> str:
        return f"Trapeze: a={self.a} b={self.b} c={self.c} d={self.d}"