class Equation:

    def __init__(self, b, c):
        self.b = b
        self.c = c

    def __str__(self):
        return f"{self.b}x + {self.c} = 0"

    def show(self):
        # print(f"{self.b}x + {self.c} = 0")
        print(self)

    INF = "infinity" # означає, що в нас нескінченна кількість розвʼязків

    def solve(self):
        if self.b == 0:
            if self.c == 0:
                return Equation.INF
            else: # c != 0
                return ()
        else:  # b != 0
            return (-self.c / self.b,)