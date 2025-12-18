"""
QUESTION:
Create a function called `fibonacci(n)` that generates the Fibonacci sequence up to the nth number using recursion. The function should return a list of integers representing the Fibonacci sequence. The input `n` is a positive integer that specifies the length of the Fibonacci sequence to be generated. The function should not include any numbers in the sequence beyond the nth number.
"""

def fibonacci(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    else:
        sequence = fibonacci(n - 1)
        sequence.append(sequence[-1] + sequence[-2])
        return sequence