"""
QUESTION:
Create a function `fibonacci_sum_greater_than(n)` that generates a Fibonacci sequence of even numbers until the sum of the sequence exceeds a given number `n`. The function should take an integer `n` as input and return a list of even Fibonacci numbers. The sequence should start with the first two even Fibonacci numbers, 0 and 2.
"""

def fibonacci_sum_greater_than(n):
    sequence = [0, 2]  # Initial sequence with first two even numbers
    while sum(sequence) <= n:
        next_num = sequence[-1] + sequence[-2]  # Compute next Fibonacci number
        if next_num % 2 == 0:  # Only add even numbers to the sequence
            sequence.append(next_num)
        else:  # Skip odd numbers
            sequence.append(next_num + 1)
    return sequence