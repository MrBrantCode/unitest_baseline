"""
QUESTION:
Create a function `f(n)` that takes an integer `n` and returns a list of length `n`. The element at each index `i` (1-indexed) is the factorial of `i` if `i` is even, or the sum of integers from 1 to `i` if `i` is odd.
"""

def f(n):
    """
    Returns a list of length n where the element at each index i (1-indexed) 
    is the factorial of i if i is even, or the sum of integers from 1 to i if i is odd.

    Args:
    n (int): The length of the output list.

    Returns:
    list: A list of length n with the specified elements.
    """
    result = []
    for i in range(n):
        if (i + 1) % 2 == 0:
            factorial = 1
            for j in range(1, i + 2):
                factorial *= j
            result.append(factorial)
        else:
            summation = 0
            for j in range(1, i + 2):
                summation += j
            result.append(summation)
    return result