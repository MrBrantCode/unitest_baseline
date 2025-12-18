"""
QUESTION:
Write a function `add_numbers` that calculates the sum of all numbers in a given list without using the `+`, `-`, `*`, `/`, `%`, or any bitwise operators. The function should return the total sum.
"""

def add_numbers(numbers):
    total = 0

    # Iterate through the list of numbers
    for num in numbers:
        # Use recursion to increment the total by the current number
        total = sum([total, num])
    
    return total