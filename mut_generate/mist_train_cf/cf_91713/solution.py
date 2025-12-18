"""
QUESTION:
Create a function named `sum_of_squares` that takes two parameters: `numbers` (a list of numbers) and `exponent` (the power to which each number is raised). The function should return the sum of each number in `numbers` raised to the power of `exponent`.
"""

def sum_of_squares(numbers, exponent):
    sum = 0
    for num in numbers:
        sum += num ** exponent
    return sum