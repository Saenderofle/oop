class Rational:
    def __init__(self, num, den=1):
        self.num = num
        self.den = den
        self.reduce()

    def __str__(self):
        return f"{self.num}/{self.den}"

    def __repr__(self):
        return f"Rational({self.num}, {self.den})"

    def reduce(self):
        common_divisor = self.nsd(self.num, self.den)
        self.num //= common_divisor
        self.den //= common_divisor

    @staticmethod
    def nsd(a, b):
        while b:
            a, b = b, a % b
        return a

    def __add__(self, other):
        if isinstance(other, Rational):
            new_num = self.num * other.den + other.num * self.den
            new_den = self.den * other.den
            return Rational(new_num, new_den)
        elif isinstance(other, int):
            return Rational(self.num + other * self.den, self.den)
        else:
            raise ValueError()

    def __sub__(self, other):
        if isinstance(other, Rational):
            new_num = self.num * other.den - other.num * self.den
            new_den = self.den * other.den
            return Rational(new_num, new_den)
        elif isinstance(other, int):
            return Rational(self.num - other * self.den, self.den)
        else:
            raise ValueError()

    def __mul__(self, other):
        if isinstance(other, Rational):
            new_num = self.num * other.num
            new_den = self.den * other.den
            return Rational(new_num, new_den)
        elif isinstance(other, int):
            return Rational(self.num * other, self.den)
        else:
            raise ValueError()

    def __truediv__(self, other):
        if isinstance(other, Rational):
            new_num = self.num * other.den
            new_den = self.den * other.num
            return Rational(new_num, new_den)
        elif isinstance(other, int):
            return Rational(self.num, self.den * other)
        else:
            raise ValueError()

    def __round__(self, ndigits=None):
        return round(self.num / self.den, ndigits)

    def __getitem__(self, item):
        if item == 'n':
            return self.num
        elif item == 'd':
            return self.den
        else:
            raise KeyError(f"Invalid key: {item}")

    def __setitem__(self, key, value):
        if key == 'n':
            self.num = value
        elif key == 'd':
            self.den = value
        else:
            raise KeyError(f"Invalid key: {key}")


def main():

    filenames = ["input01"]
    for filename in filenames:
        with open(filename, 'r') as file:
            for line in file:
                expression = line.strip().split()
                result = evaluate_expression(expression)
                print(f"Result for {line.strip()}: {result}")



def evaluate_expression(expression):
    result = Rational(0)
    operator = "+"
    for token in expression:

        if token in "+-*/":
            operator = token
            continue

        rational_number = parse_rational(token)

        if operator == "+":
            result += rational_number
        elif operator == "-":
            result -= rational_number
        elif operator == "*":
            result *= rational_number
        elif operator == "/":
            result /= rational_number
    return result



def parse_rational(token):
    if "/" in token:
        num, den = map(int, token.split("/"))
        return Rational(num, den)
    else:
        return Rational(int(token))


if __name__ == "__main__":
    main()
    r1 = Rational(1,5)
    print(r1['n'])

