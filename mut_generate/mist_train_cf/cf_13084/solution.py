"""
QUESTION:
Create a function named `get_square_numbers` that takes two integers, `start` and `end`, as input. The function should return a list of square numbers between `start` and `end` (inclusive) and handle cases where `start` is greater than `end` or where the input integers are negative.
"""

def get_square_numbers(start, end):
    if start > end:
        start, end = end, start  # swap the values if start > end

    square_numbers = []
    for i in range(start, end+1):
        if i >= 0:
            square_numbers.append(i**2)

    return square_numbers