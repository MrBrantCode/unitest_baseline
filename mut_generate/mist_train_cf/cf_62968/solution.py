"""
QUESTION:
Write a function called `generate_fibonacci(n)` that generates and returns an array containing the initial n numbers in the Fibonacci sequence, where n is an integer. The Fibonacci sequence starts with 0 and 1, and every next number is the sum of the two preceding ones. If n is less than or equal to 0, the function should return an empty list.
"""

def generate_fibonacci(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    else:
        fibonacci = [0, 1]
        for i in range(2, n):
            fibonacci.append(fibonacci[i-1] + fibonacci[i-2])
        return fibonacci