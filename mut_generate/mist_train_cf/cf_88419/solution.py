"""
QUESTION:
Write a function `detect_even_odd` that determines whether a given integer is even or odd. The function should accept a single argument `number` and return a string indicating whether the number is even, odd, or invalid input. The input `number` is guaranteed to be an integer between 1 and 1000 (inclusive), but the function should still handle cases where the input is not a positive integer within this range and return "Invalid Input" in such cases.
"""

def detect_even_odd(number):
    if not isinstance(number, int) or number <= 0 or number > 1000:
        return "Invalid Input"
    elif number % 2 == 0:
        return "Even"
    else:
        return "Odd"