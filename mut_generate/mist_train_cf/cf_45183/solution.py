"""
QUESTION:
Construct a function named `cumulative_total(n)` that takes a positive integer `n` as input and returns the cumulative total of all Fibonacci numbers that are less than or equal to `n`. The function should handle non-positive integers by returning an error message.
"""

def cumulative_total(n):
    if n <= 0:
        return "n must be a positive integer"
    else:
        fibonacci_sequence = [0, 1]
        while True:
            next_element = fibonacci_sequence[-1] + fibonacci_sequence[-2]
            if next_element > n:
                break
            fibonacci_sequence.append(next_element)
        return sum(fibonacci_sequence)