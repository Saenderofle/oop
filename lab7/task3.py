EPSILON = 1e-10

def sequence_a():
    s = 1/2
    a = 1/2
    n = 2
    while a < EPSILON:
        n += 1
        a = 1/((n-1) * n)
        s += a
    return s


print(sequence_a())
def sequence_b():
    s = 1/2
    a = 1/2
    n = 2
    while a < EPSILON:
        n += 1
        a = ((-1)**n * (n - 1)) / n
        s += a
    return s

print(sequence_b())