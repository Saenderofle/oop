import math


EPSILON = 1e-2


def sequence_a(x):
    a1 = x
    while True:
        an = math.sqrt(abs(4 * a1**2 - 2*x))
        if abs(an - a1) < EPSILON:
            return an
        a1 = an


def sequence_b(x):
    a1 = x
    while True:
        an = (16 + x) / (1 + abs(a1**3))
        if abs(an - a1) < EPSILON:
            return an
        a1 = an


def sequence_a_modified(x, n):
    a1 = x
    for _ in range(2, n+1):
        an = math.sqrt(abs(4 * a1**2 - 2*x))
        a1 = an
    return a1


def sequence_b_modified(x, n):
    a1 = x
    for _ in range(2, n+1):
        an = (16 + x) / (1 + abs(a1**3))
        a1 = an
    return a1



