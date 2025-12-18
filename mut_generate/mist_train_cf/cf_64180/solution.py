"""
QUESTION:
Construct a function named `generate_fibonacci` that accepts a single parameter `n` representing the count of elements and returns a list containing the Fibonacci series up to the specified count. The function should generate `n` Fibonacci numbers, where the first two numbers are 0 and 1, and each subsequent number is the sum of the previous two. If `n` is 0, the function should return an empty list.
"""

def generate_fibonacci(n):
    if n == 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    else:
        fibonacci = [0, 1]
        for i in range(n - 2):
            fibonacci.append(fibonacci[-1] + fibonacci[-2])
        return fibonacci