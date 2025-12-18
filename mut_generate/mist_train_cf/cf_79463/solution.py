"""
QUESTION:
Write a Python function named `master_theorem(a, b, f)` that solves recurrence relations of the form T(n) = aT(n/b) + f(n). The function should take as input the values of `a`, `b`, and the function `f`, and return the solution to the recurrence relation. The function should only work when `a >= 1`, `b > 1`, and `f(n)` is a function which can be assumed to be positive for n bigger than `n0`.
"""

def master_theorem(a, b, f):
    def f_n(n):
        return f(n)

    def T(n):
        if n == 1:
            return f_n(1)
        else:
            return a * T(n // b) + f_n(n)

    return T