# A
def sum_a(n):
    b1 = 1
    b2 = 1
    a1 = 0
    a2 = 1
    for k in range(3, n + 1):
        bk = b2 + a2
        b1 = b2
        b2 = bk
        ak = a2 / k + a1 * bk
        a1 = a2
        a2 = ak
        yield ak

for sol in sum_a(33):
    print(sol)

def sum_b(n):
    a1 = 1
    a2 = 1
    for k in range(3, n + 1):
        ak = a2 / k + a1
        a1 = a2
        a2 = ak
        yield ak

def sum_c(n):
    a1 = 1
    a2 = 1
    for k in range(3, n + 1):
        ak = a2 + a1 / 2**k
        a1 = a2
        a2 = ak
        yield ak