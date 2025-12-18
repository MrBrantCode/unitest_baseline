"""
QUESTION:
Implement a function `calculate_fibonacci` that takes an integer `limit` as input and returns a list of Fibonacci numbers up to the limit (inclusive). The Fibonacci sequence starts with 0 and 1, and each subsequent number is the sum of the previous two. If the limit is less than or equal to 0, the function should return an empty list.
"""

from typing import List

def calculate_fibonacci(limit: int) -> List[int]:
    if limit <= 0:
        return []
    fibonacci_sequence = [0, 1]
    while True:
        next_fib = fibonacci_sequence[-1] + fibonacci_sequence[-2]
        if next_fib > limit:
            break
        fibonacci_sequence.append(next_fib)
    return fibonacci_sequence