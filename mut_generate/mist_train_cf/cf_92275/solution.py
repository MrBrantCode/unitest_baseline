"""
QUESTION:
Implement a function `simpsons_rule(f, a, b, n)` that approximates the definite integral of a given function `f(x)` from `a` to `b` using Simpson's rule with `n` intervals. The function should take as input a function `f`, the lower limit of integration `a`, the upper limit of integration `b`, and the number of intervals `n`, and return the approximate value of the integral. Assume that `n` is an even number.
"""

def simpsons_rule(f, a, b, n):
    h = (b - a) / n
    integral = f(a) + f(b)

    for i in range(1, n):
        x = a + i * h
        if i % 2 == 0:
            integral += 2 * f(x)
        else:
            integral += 4 * f(x)

    integral *= h / 3
    return integral