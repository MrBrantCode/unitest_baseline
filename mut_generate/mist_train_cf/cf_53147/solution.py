"""
QUESTION:
Create a function `f` that accepts an integer `n` as its argument. The function should return a list of length `n` where the element at index `i` represents the factorial of `i` if `i` is even, and the summation of numbers from 1 to `i` if `i` is odd. The index `i` starts at 1.
"""

def f(n):
    def factorial(x):
        if x == 1 or x == 0:
            return 1
        else:
            return x * factorial(x - 1)

    def summation(x):
        return (x * (x + 1)) // 2

    result = []
    for i in range(1, n + 1):
        if i % 2 == 0:
            result.append(factorial(i))
        else:
            result.append(summation(i))

    return result