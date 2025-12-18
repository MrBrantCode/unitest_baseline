"""
QUESTION:
Write a function `f` that takes an integer `n` as input and returns a list of `n` elements. The element at position `i` (1-indexed) should be the factorial of `i` if `i` is even, and the sum of numbers from 1 to `i` if `i` is odd.
"""

def f(n):
    result = []
    for i in range(1, n+1):
        if i % 2 == 0:
            factorial = 1
            for j in range(1, i+1):
                factorial *= j
            result.append(factorial)
        else:
            sum_ = 0
            for j in range(1, i+1):
                sum_ += j
            result.append(sum_)
    return result