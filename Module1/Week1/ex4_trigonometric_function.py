def factorial(x):
    if x == 0 or x == 1:
        return 1
    return x * factorial(x - 1)


def approx_xin(x, n):
    res = 0
    for i in range(n):
        res += (-1) ** i * x ** (2 * i + 1) / factorial(2 * i + 1)
    print(res)


def approx_cos(x, n):
    res = 0
    for i in range(n):
        res += (-1) ** i * x ** (2 * i) / factorial(2 * i)
    print(res)


def approx_sinh(x, n):
    res = 0
    for i in range(n):
        res += x ** (2 * i + 1) / factorial(2 * i + 1)
    print(res)


def approx_cosh(x, n):
    res = 0
    for i in range(n):
        res += x ** (2 * i) / factorial(2 * i)
    print(res)


approx_xin(x=3.14, n=10)
approx_cos(x=3.14, n=10)
approx_sinh(x=3.14, n=10)
approx_cosh(x=3.14, n=10)
