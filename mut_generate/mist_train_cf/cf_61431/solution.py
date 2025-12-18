"""
QUESTION:
Write a function `is_even(hexadecimal)` that determines whether a given hexadecimal number is even or odd. The function should handle very large hexadecimal numbers efficiently, with a time complexity of O(1), and validate the input for potential edge cases such as empty or null values. The function should return `True` for even numbers, `False` for odd numbers, and `None` for invalid inputs.
"""

def is_even(hexadecimal):
    if not hexadecimal:
        return None
    last_digit = hexadecimal[-1].lower()
    if last_digit in ['0', '2', '4', '6', '8', 'a', 'c', 'e']:
        return True  # even
    else:
        return False  # odd