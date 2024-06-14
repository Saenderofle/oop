
def foo_a(x: float, n: int) -> float:
    current_member = x

    for k in range(2, n+1):
        current_member = current_member * ((k * x - x)/k)
    return current_member



print(2**9 / 9)
print(foo_a(2, 9))


#B
def foo_b(x: float, n: int) -> float:
    current_member = -x
    for k in range(2, n + 1):
        current_member = current_member * ((- k * x + x) / k)
    return current_member

#C

def foo_c(x: float, n: int) ->float:
    current_member = 1
    for k in range(1, n + 1):
        a = 1
        k_step = k**2
        for j in range(k_step - k + 1, k_step + k + 1):
            a /= j
        current_member = current_member * (-x)*a

    return current_member
print(foo_c(2, 9))

def foo_d(x: float, n: int) -> float:
    current_member = 1
    for k in range(1, n + 1):
        current_member = current_member * (x**2 / (4 * k**2 - 2*k))
    return current_member


def foo_e(x: float, n: int) -> float:
    current_member = 1
    for k in range(1, n + 1):
        current_member = current_member * -(x ** 2 / (4 * k ** 2 - 2 * k))
    return current_member


def foo_f(x: float, n: int) -> float:
    current_member = x
    for k in range(1, n + 1):
        current_member = current_member * (x**2 / (k + 1))
    return current_member