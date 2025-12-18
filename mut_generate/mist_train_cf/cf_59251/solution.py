"""
QUESTION:
Create a function named `fibonacci(n)` that generates the Fibonacci sequence up to the nth term, where n is a positive integer. The function should be efficient and readable, and it should handle cases where n is less than or equal to 0 by providing a descriptive message.
"""

def fibonacci(n):
    if n <= 0:
        print("Input should be a positive integer.")
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    else:
        sequence = [0, 1]
        while len(sequence) < n:
            sequence.append(sequence[-1] + sequence[-2])
        return sequence