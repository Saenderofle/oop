EPSILON = 1e-10
X = 4

def sequence_a(x):
    a = 1
    s = 1
    k = 0
    while True:
        k += 1
        a *= (x**2) / (2 * k)
        s += a

        if abs(a) < EPSILON:
            return [s, k]


solution = sequence_a(X)
print(f'Solution is {solution[0]}, and number of iterations is {solution[1]}')


def sequence_b(x):
    a = x
    s = x
    k = 0
    while True:
        k += 1
        a *= (-(x**2) * (2*k - 1)) / (k * (2*k + 1))
        s += a

        if abs(a) < EPSILON:
            return [s, k]

solution = sequence_b(X)
print(f'Solution is {solution[0]}, and number of iterations is {solution[1]}')
x = X
