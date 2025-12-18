"""
QUESTION:
Implement a recursive function named `fibonacci` that takes an integer `num` as input and returns a list of Fibonacci numbers up to the `num`-th number in the sequence. The function should handle cases where `num` is less than or equal to 0, 1, or 2. The Fibonacci sequence is defined such that each number is the sum of the two preceding ones, usually starting with 0 and 1.
"""

def fibonacci(num):
    if num <= 0:
        return []
    elif num == 1:
        return [0]
    elif num == 2:
        return [0, 1]
    else:
        fib = fibonacci(num-1)
        fib.append(fib[-1]+fib[-2])
        return fib