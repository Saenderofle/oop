from Figure import Figure
class Triangle(Figure):
    def __init__(self, a, b, c):
        my_list = [a, b, c]
        my_list.sort()
        a, b, c = my_list
        assert a + b > c and a>0 and b>0 and c>0
        self.a = a
        self.b = b
        self.c = c
    def dimension(self):
        return 2
    def semiperimeter(self):
        return self.perimeter() / 2
    def perimeter(self):
        return (self.a + self.b + self.c)
    def square(self):
        result = (self.semiperimeter() * (self.semiperimeter() - self.a) * (self.semiperimeter() - self.b) * (self.semiperimeter() - self.c)) ** 0.5
        return (result)
    def volume(self):
        return self.square()
    def __str__(self) -> str:
        return f"Triangle: a={self.a} b={self.b} c={self.c}"



