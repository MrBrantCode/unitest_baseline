"""
QUESTION:
Implement the function `golden_section_search` that takes a function `f`, lower bound `a`, upper bound `b`, and tolerance as parameters. The function should return the value of `x` at which the minimum value of the function occurs and the minimum value itself. Assume that the function `f` is a continuous, unimodal function within the interval `[a, b]`.
"""

def golden_section_search(f, a, b, tolerance):
    golden_ratio = (5 ** 0.5 - 1) / 2
    c = b - golden_ratio * (b - a)
    d = a + golden_ratio * (b - a)
    while abs(c - d) > tolerance:
        if f(c) < f(d):
            b = d
        else:
            a = c
        c = b - golden_ratio * (b - a)
        d = a + golden_ratio * (b - a)
    return (c + d) / 2, f((c + d) / 2)