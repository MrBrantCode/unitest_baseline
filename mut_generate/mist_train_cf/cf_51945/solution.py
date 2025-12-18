"""
QUESTION:
Create a function named `generate_fibonacci_numbers` that generates a list of the first `n` Fibonacci numbers. The list should start with the initial two Fibonacci numbers, 0 and 1, and each subsequent number should be the sum of the previous two. The function should return the list of Fibonacci numbers. The function will be used to generate up to 1,500 Fibonacci numbers, which may exceed the range of 64-bit integers.
"""

def generate_fibonacci_numbers(n):
    fibonacci_numbers = [0, 1]
    while len(fibonacci_numbers) < n:
        fibonacci_numbers.append(fibonacci_numbers[-1] + fibonacci_numbers[-2])
    return fibonacci_numbers