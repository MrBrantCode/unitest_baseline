"""
QUESTION:
Create a Python generator function named `pentagonal_numbers(n)` that yields the first n non-consecutive pentagonal numbers. The function should take an integer n as input and return a warning message if n is not a positive integer. The generator should produce pentagonal numbers using the formula `pentagonal = x*(3*x - 1) // 2` and ensure non-consecutive numbers by incrementing x by 2 in each iteration.
"""

def pentagonal_numbers(n):
    # Check if 'n' is integer and positive
    if not isinstance(n, int) or n < 1:
        return "Warning: Invalid input. 'n' should be a positive integer."
    
    # Generator
    x = 1
    count = 0
    while count < n:
        pentagonal = x*(3*x - 1) // 2
        yield pentagonal
        x += 2  # To get non-consecutive pentagonal numbers
        count += 1