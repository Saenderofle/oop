from besquarefunc import QuadraticEquation
from diquadraticfunc import diquadratic
from squarefunc import Equation

class Solver:
    def __init__(self, argu):
        self.argu = argu

    @staticmethod
    def from_input_file(filename):
        with open(filename, 'r') as f:
            lines = f.readlines()

        all_comp = []
        for line in lines:
            arguments = [float(x) for x in line.strip().split()]
            all_comp.append((arguments))

        return all_comp

    @staticmethod
    def solve_equation(equation):
        e = Equation(*equation)
        return e.solve()

    @staticmethod
    def solve_quadratic_equation(equation):
        e = QuadraticEquation(*equation)
        return e.solve()

    @staticmethod
    def solve_diquadratic_equation(equation):
        k = list(equation)
        k.pop(3)
        k.pop(1)
        e = diquadratic(*k)
        return e.solve()

    @staticmethod
    def sort_argu(all_comp):
        ALL_AMOUNT = {
            0: [],
            1: [],
            2: [],
            3: [],
            4: [],
            'infinity': [],
        }

        maxs = float()
        mins = float()
        for i in all_comp:
            if len(i) == 2:
                m = Solver.solve_equation(i)
            elif len(i) == 3:
                m = Solver.solve_quadratic_equation(i)
            elif len(i) == 5:
                m = Solver.solve_diquadratic_equation(i)

            amount = len(m)
            if amount in ALL_AMOUNT:
                ALL_AMOUNT[amount].append(i)
            elif m == 'infinity':
                ALL_AMOUNT['infinity'].append(i)

            if m == 'infinity':
                continue
            else:
                for k in m:
                    if isinstance(k, complex):
                        continue  # Skip infinity or complex solutions
                    elif float(k) > maxs:
                        maxs = float(k)
                    elif float(k) < mins:
                        mins = float(k)

        return ALL_AMOUNT, mins, maxs

