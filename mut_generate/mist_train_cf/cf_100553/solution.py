"""
QUESTION:
Write a function `subtract_vectors(x, y)` that takes two vectors `x` and `y` as input and returns a new vector `result` where each element of `result` is the difference of the corresponding elements in `x` and `y`. The vectors `x` and `y` have the same length.
"""

def subtract_vectors(x, y):
    result = []
    for i in range(len(x)):
        result.append(x[i] - y[i])
    return result