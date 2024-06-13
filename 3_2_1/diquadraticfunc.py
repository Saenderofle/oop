from besquarefunc import QuadraticEquation

class diquadratic(QuadraticEquation):

    def __str__(self):
        return f"{self.a}x^4 + {self.b}x^2 + {self.c} = 0"

    def solve(self):
        set_soltions = set()
        soltions_quadratic = super().solve()
        if soltions_quadratic == diquadratic.INF:
            return diquadratic.INF
        for solution  in soltions_quadratic:
            t1 = solution ** 0.5
            t2 = -t1
            set_soltions.add(t1)
            set_soltions.add(t2)

        return tuple(set_soltions)