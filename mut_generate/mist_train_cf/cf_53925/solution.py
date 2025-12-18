"""
QUESTION:
Define a function `power_M(s, M)` that takes a string `s` and an integer `M` as input, and returns the string `s` repeated `M` times. Evaluate which of the following expressions hold true for all non-empty strings `a`, `x`, and `y`, and single character string `a`: A) `a^M = a`, B) `(ax)^M = (xa)^M`, C) `(xy)^M = y^Mx^M`, or D) None of the above. Assume `^M` denotes the defined operation.
"""

def power_M(s, M):
    return s * M