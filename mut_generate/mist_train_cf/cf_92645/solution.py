"""
QUESTION:
Create a function named `get_square_numbers` that takes two integers as input: a starting number and an ending number. The function should return a list of square numbers between the two input integers (inclusive), where both negative and non-negative integers are handled, and the function should work regardless of the order of the input integers.
"""

def get_square_numbers(start, end):
    if start > end:
        start, end = end, start  

    square_numbers = [i**2 for i in range(start, end+1) if i >= 0]

    return square_numbers