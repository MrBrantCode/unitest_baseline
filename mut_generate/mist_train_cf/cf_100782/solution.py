"""
QUESTION:
Write a function `perfect_squares_with_same_units_digit` that takes a list of non-negative integers as input and returns a new list containing only the numbers that are perfect squares and whose units digits are the same when read from left to right and right to left. The function should not use Python's built-in perfect square function.
"""

def perfect_squares_with_same_units_digit(numbers):
    result = []
    for num in numbers:
        root = num ** 0.5
        if int(root + 0.5) ** 2 != num:
            continue
        square = str(num ** 2)
        if square[0] == square[-1]:
            result.append(num)
    return result