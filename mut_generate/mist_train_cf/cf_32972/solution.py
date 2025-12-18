"""
QUESTION:
Implement a function `_reduce` that takes a list `x` and a binary reduction function as input and returns a single value. The reduction function should be applied cumulatively to the elements of the list, from left to right, so as to reduce the list to a single output value. The function should return this output value. The `_reduce` function should not use Python's built-in `reduce` function or any other built-in functions that perform a similar operation. The reduction function should be applied to the first two elements of the list first, then to the result and the next element, and so on.
"""

def _reduce(x, reduction):
    result = x[0]
    for i in range(1, len(x)):
        result = reduction(result, x[i])
    return result