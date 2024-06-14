EPSILON = 1e-10


def sh_a(x):
    s = x
    a = x
    n = 0
    while True:
        n += 1
        a = a * (x**2) / ((2 * n) * (2*n + 1))
        s += a
        if abs(a) < EPSILON:
            return s


def ln_b(x):
    s = x
    a = x
    n = 0
    while True:
        n += 1
        a = a * (-x / n)
        s += a
        if abs(a) < EPSILON:
            return s


def sequence_c(x):
        s = 1
        a = 1
        n = 0
        while True:
            n += 1
            a = a * (-x)
            s += a
            if abs(a) < EPSILON:
                return s


def ln_d(x):
    s = x
    a = x
    n = 0
    while True:
        n += 1
        a = a * x**2
        b = a / (2*n + 1)
        s += b
        if abs(b) < EPSILON:
            return 2*s


def sequence_e(x):
    s = 1
    a = 1
    n = 0
    while True:
        n += 1
        a = a * (-x) * (n + 1) / n
        s += a
        if abs(a) < EPSILON:
            return s


def sequence_f(x):
    s = 1
    a = 1
    n = 0
    while True:
        n += 1
        a = a * (-x**2)
        s += a
        if abs(a) < EPSILON:
            return s


def sequence_g(x):
    s = 1
    a = 1
    n = 0
    while True:
        n += 1
        a = a * x * (0.5 - (n - 1)) / n
        s += a
        if abs(a) < EPSILON:
            return s