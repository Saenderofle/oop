def det_c(n):
    d1 = 3
    d2 = 7
    for i in range(3, n+1):
        dn = 3*d2 - 2*d1
        d1 = d2
        d2 = dn
    return d2


def det_d(n):
    d1 = 0
    d2 = 1
    for i in range(3, n+1):
        dn = -d1
        d1 = d2
        d2 = dn
    return d2


def det_e(n, a):
    d1 = a
    d2 = a**2 - 1
    for i in range(3, n+1):
        dn = d2*a - d1
        d1 = d2
        d2 = dn
    return d2


n = 4

print(det_c(n))
print(det_d(n))
print(det_e(n, 1))