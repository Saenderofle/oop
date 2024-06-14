class Rational:
    def __init__(self, num, den=1):
        self.num = num
        self.den = den
        self.reduce()

    def __str__(self):
        return f"{self.num}/{self.den}"

    def __add__(self, other):
        return Rational(self.num * other.den + other.num * self.den, self.den * other.den)

    def __repr__(self):
        return f"Rational({self.num}, {self.den})"

    def reduce(self):
        common_divisor = self.gcd(self.num, self.den)
        self.num //= common_divisor
        self.den //= common_divisor

    @staticmethod
    def gcd(a, b):
        while b:
            a, b = b, a % b
        return a


class RationalList:
    def __init__(self, elements=None):
        self.elements = []
        if elements:
            for element in elements:
                self.append(element)

    def __str__(self):
        return str(self.elements)

    def __repr__(self):
        return repr(self.elements)

    def __len__(self):
        return len(self.elements)

    def __getitem__(self, index):
        return self.elements[index]

    def __setitem__(self, index, value):
        if not isinstance(value, Rational):
            raise ValueError()
        self.elements[index] = value

    def append(self, value):
        if not isinstance(value, Rational):
            raise ValueError()
        self.elements.append(value)

    def extend(self, values):
        for value in values:
            self.append(value)

    def __add__(self, other):
        if isinstance(other, Rational):
            return RationalList(self.elements + [other])
        elif isinstance(other, RationalList):
            return RationalList(self.elements + other.elements)
        elif isinstance(other, int):
            return RationalList(self.elements + [Rational(other)])
        else:
            raise ValueError("Unsupported operand type for +")

    def __iadd__(self, other):
        if isinstance(other, Rational):
            self.append(other)
        elif isinstance(other, RationalList):
            self.extend(other.elements)
        elif isinstance(other, int):
            self.append(Rational(other))
        else:
            raise ValueError("Unsupported operand type for +=")
        return self

    def sum_elements(self):
        total = Rational(0)
        for element in self.elements:
            total += element
        return total


def read_rational_sequence(filename):
    with open(filename, 'r') as file:
        sequence = []
        for line in file:
            parts = line.strip().split()
            for part in parts:
                if '/' in part:
                    num, den = map(int, part.split('/'))
                    sequence.append(Rational(num, den))
                else:
                    sequence.append(Rational(int(part)))
    return sequence


def main():
    filenames = ["input01.txt", "input02.txt", "input03.txt"]
    for filename in filenames:
        sequence = read_rational_sequence(filename)
        total = RationalList(sequence)
        print(f"Total for {filename}: {total.sum_elements()}")


if __name__ == "__main__":
    main()
