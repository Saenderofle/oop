class Rational:
    def __init__(self, num, den=1):
        self.num = num
        self.den = den
        self.reduce()

    def __str__(self):
        if self.den == 1:
            return f"{self.num}"
        else:
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

    def __eq__(self, other):
        if isinstance(other, Rational):
            return self.num == other.num and self.den == other.den
        return False

    def __hash__(self):
        return hash((self.num, self.den))


class RationalList:
    def __init__(self, elements=None):
        self.elements = []
        self.elements_set = set()
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
        if value not in self.elements_set:
            self.elements_set.add(value)
            self.elements[index] = value

    def append(self, value):
        if not isinstance(value, Rational):
            raise ValueError()
        if value not in self.elements_set:
            self.elements.append(value)
            self.elements_set.add(value)

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

    def __iter__(self):
        # Sorting the elements first by denominator in descending order,
        # and then by numerator in descending order if denominators are equal
        sorted_elements = sorted(self.elements, key=lambda r: (r.den, r.num), reverse=True)
        return iter(sorted_elements)


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
        rational_list = RationalList(sequence)
        output_filename = f"output_{filename}"
        with open(output_filename, 'w') as outfile:
            outfile.write(f"Rational sequence for {filename}:\n")
            for rational in rational_list:
                outfile.write(str(rational) + "\n")
        print(f"Results for {filename} have been written to {output_filename}")


if __name__ == "__main__":
    main()
