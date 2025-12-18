"""
QUESTION:
Implement the `trapezoidal_rule` function, which takes in a function `f`, the start and end points `a` and `b`, and the number of sub-intervals `N`, and returns an approximation of the definite integral of `f` from `a` to `b` using the trapezoidal method.
"""

def trapezoidal_rule(f, a, b, N):
    h = (b - a) / N
    return (h / 2) * (f(a) + f(b) + 2*sum(f(a + i*h) for i in range(1, N)))