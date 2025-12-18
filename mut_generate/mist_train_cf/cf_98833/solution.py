"""
QUESTION:
Implement a function `f` that takes an input `x` and produces an output, and a function `g` that takes an input `y` and produces an output. The functions `f` and `g` should be related such that for every input `x` in the set `S`, there exists an output `y` in the set `T` such that `f(x)` equals `g(y)`.
"""

def f(x):
    return x**2

def g(y):
    return y + 1