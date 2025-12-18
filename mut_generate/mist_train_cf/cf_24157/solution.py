"""
QUESTION:
Write a function named `fibonacci(x)` that generates a list of Fibonacci numbers up to the given number `x`. The function should return an empty list if `x` is less than 0. It should also handle the cases when `x` is 0 or 1, returning 0 and [0, 1] respectively. For any other value of `x`, the function should return a list of Fibonacci numbers that are less than `x`.
"""

def fibonacci(x):
    """
    Generate a list of Fibonacci numbers up to the given number x.
    
    Args:
        x (int): The upper limit for the Fibonacci sequence.
    
    Returns:
        list: A list of Fibonacci numbers less than x.
    """
    a = 0
    b = 1
    if x < 0:
        return []
    elif x == 0:
        return [0]
    elif x == 1:
        return [0, 1]
    else:
        c = a + b
        res = [a, b]
        while c < x:
            res.append(c)
            a = b
            b = c
            c = a + b
        return res